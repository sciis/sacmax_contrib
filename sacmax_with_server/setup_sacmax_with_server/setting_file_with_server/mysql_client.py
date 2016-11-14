#coding: utf-8

## Please append
##  /home/pi/max/cmd_def.py  -> 'apply_mysql_key_val':[general_def.MYSQL_READ_PORT],
##  /home/pigeneral.conf     -> MYSQL_READ_PORT=PortNumber
##      Port Number(ex. 9009)

import sys, os
dir = os.path.dirname(__file__)
sys.path.append( dir +'/modules')

import read_mysql

import time
import imp
import threading
import socket
import datetime
from queue import Queue

import json

general_def = imp.load_source('general_def', '/home/pi/general.conf')
dev_info = imp.load_source('dev_info', '/home/pi/dev_info.conf')

class MySqlClient:
    def __init__(self):
        self.target_filename = 'mysql_key_val.conf'
        self.target_filepath = '/home/pi/' + self.target_filename
        self.key_list = []
        self.data_list = []

    def apply_mysql_key_val(self, q):
        if os.path.exists(self.target_filepath) == False:
            print('no such file mysql_key_val config_file')
            print('create config_file')
            self.__write_mysql_key_val()
            
        try:
            f= open(self.target_filepath, 'r')
            json_data = json.load(f)
            del json_data["INFO_COMMENT"]
            f.close()
        except Exception as e:
            print('mysql_key_val config_file error')
            print('remake config_file')
            os.remove(self.target_filepath)
            self.__write_mysql_key_val()

#        print("before_list:")
#        print(json_data)

        self.__connect_mysql(json_data)

        # 取得したデータをもとにファイル書き換え
        f= open(self.target_filepath, 'r')
        json_replace_data = json.load(f)
        f.close()
        i=0
        print(self.key_list)
        print(i)
        for keys in self.key_list:
            json_replace_data[keys] = self.data_list[i]
            i += 1
#        print(json_replace_data)

        f= open(self.target_filepath, 'w')
        json.dump(json_replace_data, f, sort_keys=True, indent=4)
        f.close()
        q.put('mysql_key_val update')
        print('mysql_key_val update')
        self.key_list = []
        self.data_list = []
        return

    def __write_mysql_key_val(self):
        conf_inital_val = """{\n    "INFO_COMMENT": "coding: utf-8 json-type",
            \n    "id": 1,
            \n    "integer_1": 0,
            \n    "char_1": ""
            \n}"""
        f = open(self.target_filepath , 'a')
        f.write(conf_inital_val)
        f.close()

    def __connect_mysql(self, data):
        select_string = ""
        dict_keys = data.keys()
        for row in dict_keys:
            select_string = select_string + row + ","
            self.key_list.append(row)
        select_string = select_string[:-1]
        query = "select " + select_string + " from " + dev_info.MYSQL_TABLE + dev_info.QUERY_CONDITIONS

        print("query:")
        print(query)

        # mysql接続し、その内容を反映
        mysql = read_mysql.ReadMysql()

        ret = mysql.dev_setting_read(query)
        if ret == False:
            q.put('mysql error')
            return
        #    mysql.content_list

        if len(mysql.content_list) > 1:
            q.put('select_err')
            return

        self.data_list = list(mysql.content_list[0])
        q.put('mysql request succeeded')
        return

if __name__ == '__main__':
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((general_def.HOST, general_def.MYSQL_READ_PORT))
    srv_sock.listen(10)

    q = Queue()

    mysql_client = MySqlClient()

    while True:
        cli_sock, cli_addr = srv_sock.accept()
        recv = cli_sock.recv(1024).decode('utf-8')
        print('%s: %s' % (__file__, recv))

        if recv != '':
            func = getattr(mysql_client, recv)
            proc = None
            proc = threading.Thread(target=func, args=(q,))
            proc.start()
            mesg = q.get()
            reply = '%s,%s,%s' % (__file__.split('/')[-1], recv, mesg)
            cli_sock.sendall(reply.encode('utf-8'))
            recv = ''
            time.sleep(0.5)
