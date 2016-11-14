#coding: utf-8

## Please append
##  /home/pi/max/cmd_def.py  -> 'dl_file':[general_def.FTP_DOWNLOAD_PORT],
##  /home/pigeneral.conf     -> FTP_DOWNLOAD_PORT=PortNumber
##      Port Number(ex. 9010)

import time
import imp
import threading
import socket
import datetime
from ftplib import FTP
from queue import Queue

general_def = imp.load_source('general_def', '/home/pi/general.conf')
dev_info = imp.load_source('dev_info', '/home/pi/dev_info.conf')

ftp_conf = dev_info.FTP_CONF
target_file = dev_info.TARGET_FILE

class FtpDownloader:
    def __init__(self, ftp_conf):
        self.target_filename = target_file
        self.target_filepath = '/home/pi/' + self.target_filename
        self.ftp_conf = ftp_conf
        self.ftp_dir = ftp_conf['dir']

    def dl_file(self, q):
        try:
            ftp = FTP()
            ret = ftp.connect(
                    ftp_conf['server'],
                    ftp_conf['port'],
                    ftp_conf['timeout'])
            if ret[:3] != '220':
                q.put('ftp.connect failed (not 220)')
                return

            ret = ftp.login(ftp_conf['user'], ftp_conf['pass'])
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

    dl = FtpDownloader(ftp_conf)

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

