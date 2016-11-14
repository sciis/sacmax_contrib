#mysql アクセス
#pip3 install PyMySQL 
#error hundle
# 1045 (28000) ← ユーザが存在しない。以下の容量で作成
#grant all privileges on client_data.* to connect_tester@"192.168.%" identified by
# 'gasys' with grant option;

import imp
import mysql.connector
mysql_info = imp.load_source('dev_info', '/home/pi/dev_info.conf')

mysql_conf = mysql_info.MYSQL_CONF

class ReadMysql:

    def __init__(self):
        self.content_list = []

    def dev_setting_read(self, query):
        try:
            self.connector = mysql.connector.connect(
                user= mysql_conf['user_name'],
                password= mysql_conf['password'],
                host= mysql_conf['host'],
                database= mysql_conf['database'],
                charset= mysql_conf['char'])
            cursor = self.connector.cursor()
            cursor.execute(query)
            self.content_list = cursor.fetchall()
            cursor.close
            self.connector.close

            return True

        except Exception as e:
            print(e)
            return False

