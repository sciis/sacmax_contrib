#coding: utf-8

## Please append
##  /home/pi/max/cmd_def.py  -> 'dl_file':[general_def.FTP_DOWNLOAD_PORT],
##  /home/pigeneral.conf     -> FTP_DOWNLOAD_PORT=PortNumber
##      Port Number(ex. 9010)

import sys, os
dir = os.path.dirname(__file__)
sys.path.append( dir +'/modules')

import read_conf

import time
import imp
import threading
import socket
import datetime
from ftplib import FTP
from queue import Queue

general_def = imp.load_source('general_def', '/home/pi/general.conf')
#ftp_conf = dev_info.FTP_CONF
#TARGET_FILE = 'dev_setting.conf'

CONF_PATH = "/home/pi/dev_info.conf"

class FtpClient:
    def __init__(self):
        self.ftp_setting_list = []
        self.ftp_conf = []
        self.ftp_dir = []

        self.target_filename = []
        self.target_filepath = []

    def dl_file(self, q):
        #conf_read
        conf = read_conf.ReadConf()
        conf.config_read(CONF_PATH)
        self.ftp_setting_list = conf.conf_list["FTP"]
        self.ftp_conf = self.ftp_setting_list["FTP_CONF"]
        self.ftp_dir = self.ftp_conf['dir']

        self.target_filename = self.ftp_setting_list['TARGET_FILE']
        self.target_filepath = '/home/pi/' + self.target_filename
        del conf
        
        try:
            ftp = FTP()
            ret = ftp.connect(
                    self.ftp_conf['server'],
                    self.ftp_conf['port'],
                    self.ftp_conf['timeout'])
            print(ret)
            
            if ret[:3] != '220':
                q.put('ftp.connect failed (not 220)')
                return

            ret = ftp.login(self.ftp_conf['user'], self.ftp_conf['pass'])
            if ret[:3] != '230':
                q.put('ftp.login failed')
                return

            ret = ftp.cwd(self.ftp_dir)
            if ret[:3] != '250':
                q.put('ftp.cwd failed (not 250)')
                return

            print(ftp.nlst())
            ret = ftp.retrbinary(
                    "RETR " + self.target_filename,
                    open(self.target_filepath, 'wb').write)
            if ret[:3] != '226':
                q.put('ftp.retrbinary failed (not 226)')
                return

            ftp.quit()
            q.put('download succeeded')
        except Exception as e:
            print(e)
            q.put(e)

if __name__ == '__main__':
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((general_def.HOST, general_def.FTP_DOWNLOAD_PORT))
    srv_sock.listen(10)

    q = Queue()

    dl = FtpClient()

    while True:
        cli_sock, cli_addr = srv_sock.accept()
        recv = cli_sock.recv(1024).decode('utf-8')
        print('%s: %s' % (__file__, recv))

        if recv != '':
            func = getattr(dl, recv)
            proc = None
            proc = threading.Thread(target=func, args=(q,))
            proc.start()
            mesg = q.get()
            reply = '%s,%s,%s' % (__file__.split('/')[-1], recv, mesg)
            cli_sock.sendall(reply.encode('utf-8'))
            recv = ''
            time.sleep(0.5)

