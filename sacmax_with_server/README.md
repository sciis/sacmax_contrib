  
  
# sacmax. with server 
  Sensor, Actuator and Camera - easy to MAXimum.  
  with server(mysql_connect, ftp download)  
  
## Description  
  sacmax. with server はsacmaxの拡張モジュール群です。sacmaxがインストールされている  
  Raspberry Piで、MySQLとFTPの機能を利用できるようになります。 
  
##Requirement  
 Raspbian jessie lite (ver. September 2016)  
 Raspberry Pi 2 in sacmax_core  
  
##Usage  
 ・ftp_client(コマンドラインから動作確認)  
     まず事前に、dev_info.conf のFTP_CONF、TARGET_FILEを設定してください。設定はファイル内のsamapleを参考にしてください。  
     
     次にターミナルを2つ開くなど、コマンドラインの画面を2つ用意してください(それぞれterminal_a、terminal_b とします)  
     $ cs /home/pi/  
     terminal_a:  
        $ python3 /home/pi/sac/ftp_client.py  
     terminal_b:  
        $ python3 /home/pi/max/dev_ctrl.py dl_file  
  
    成功すれば、TARGET_FILEに指定したファイルが/home/pi 直下にダウンロードされます。
  
 ・ftp_client(Webページから動作確認)  
     dev_info.conf 設定後、コマンドラインから確認の terminal_a のコマンドを打ち込んでから、以下のurlにアクセスしてください  
     http://(Raspberry Pi のIPアドレス)/device/dl_file  
  
 ・mysql_client(コマンドラインから動作確認)  
     まず事前に、dev_info.conf のMYSQL_CONF、MYSQL_TABLE、QUERY_CONDITIONS を設定してください。設定はファイル内のsamapleを参考にしてください。  
     次にmysql_key_val.conf 内の"INFO_COMMENT"以下の値を設定してください。"INFO_COMMENT"以下の値は、mysqlのテーブルのカラム名に相当するものです。
     
     カラム: 値
     
     2ファイルの設定後、ターミナルを2つ開くなど、コマンドラインの画面を2つ用意してください(それぞれterminal_a、terminal_b とします)  
     $ cd /home/pi/  
     terminal_a:  
        $ python3 /home/pi/sac/mysql_client.py  
     terminal_b:  
        $ python3 /home/pi/max/dev_ctrl.py apply_mysql_key_val  
  
    成功すれば、mysql_key_val.confに指定したカラムの値がmysqlに設定されている値に準じて変化します。
  
 ・mysql_client(Webページから動作確認)  
     コマンドラインから確認の terminal_a のコマンドを打ち込んでから、ブラウザのflask_test_page下にある"sacmax."のロゴをクリックしてください  
     あるいは以下のurlにアクセスしてください  
     http://(Raspberry Pi のIPアドレス)/device/apply_mysql_key_val  
  
  
##Install  
  
  ※sacmax.coreのセットアップまでは終了させておいてください  
  ※事前に sudo apt-get update をしておいてください  
  ここではsetup_sacmax_with_server をzipファイル(setup_sacmax_with_server.zip)にした前提で説明をしています。PeaZipなど圧縮解凍アプリをご利用ください。またwin8以降の場合は新規作成から作成可能です。  
  
  1.setup_sacmax_with_server.zipを /home/pi上にダウンロードしてください(zipしていなくとも、ダウンロード先は /home/pi です)  
  2.$ unzip setup_sacmax.zip (zipしてインストールしていなければ不要です)  
  3.$ cd setup_sacmax_with_server  
  4.$ sudo sh install_nginx_sacmax.sh install  
  5.$ sudo sh install_with_server.sh install  
  6./home/pi/sac 内に追加された ftp_client.py、mysql_client.py のコメントに従い、/home/pi/max/cmd_def.py と /home/pigeneral.conf に追記  
  
##Licence  
  
