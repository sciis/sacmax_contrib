#mysql アクセス
#pip3 install PyMySQL 
#error hundle
# 1045 (28000) ← ユーザが存在しない。以下の容量で作成
#grant all privileges on client_data.* to connect_tester@"192.168.%" identified by
# 'gasys' with grant option;

import imp
import mysql.connector
CONF_PATH = "/home/pi/dev_info.conf"

import read_conf

class ReadMysql:

    def __init__(self):
        self.content_list = []

        self.mysql_conf = []

    def dev_setting_read(self, query):
        #conf_read
        conf = read_conf.ReadConf()
        conf.config_read(CONF_PATH)
        mysql_info = conf.conf_list["MYSQL"]
        self.mysql_conf = mysql_info["MYSQL_CONF"]
        del conf

        try:
            self.connector = mysql.connector.connect(
                user= self.mysql_conf['user_name'],
                password= self.mysql_conf['password'],
                host= self.mysql_conf['host'],
                database= self.mysql_conf['database'],
                charset= self.mysql_conf['char'])
            cursor = self.connector.cursor()
            cursor.execute(query)
            self.content_list = cursor.fetchall()
            cursor.close
            self.connector.close

            return True

        except Exception as e:
            print(e)
            return False

