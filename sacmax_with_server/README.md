  
  
# sacmax. with server 
  Sensor, Actuator and Camera - easy to MAXimum.  
  with server(mysql_connect, ftp download)  
  
## Description  
  sacmax. with server ��sacmax�̊g�����W���[���Q�ł��Bsacmax���C���X�g�[������Ă���  
  Raspberry Pi�ŁAMySQL��FTP�̋@�\�𗘗p�ł���悤�ɂȂ�܂��B 
  
##Requirement  
 Raspbian jessie lite (ver. September 2016)  
 Raspberry Pi 2 in sacmax_core  
  
##Usage  
 �Eftp_client(�R�}���h���C�����瓮��m�F)  
     �܂����O�ɁAdev_info.conf ��FTP_CONF�ATARGET_FILE��ݒ肵�Ă��������B�ݒ�̓t�@�C������samaple���Q�l�ɂ��Ă��������B  
     
     ���Ƀ^�[�~�i����2�J���ȂǁA�R�}���h���C���̉�ʂ�2�p�ӂ��Ă�������(���ꂼ��terminal_a�Aterminal_b �Ƃ��܂�)  
     $ cs /home/pi/  
     terminal_a:  
        $ python3 /home/pi/sac/ftp_client.py  
     terminal_b:  
        $ python3 /home/pi/max/dev_ctrl.py dl_file  
  
    ��������΁ATARGET_FILE�Ɏw�肵���t�@�C����/home/pi �����Ƀ_�E�����[�h����܂��B
  
 �Eftp_client(Web�y�[�W���瓮��m�F)  
     dev_info.conf �ݒ��A�R�}���h���C������m�F�� terminal_a �̃R�}���h��ł�����ł���A�u���E�U��flask_test_page���ɂ���"sacmax."�̃��S���N���b�N���Ă�������  
     ���邢�͈ȉ���url�ɃA�N�Z�X���Ă�������  
     http://(Raspberry Pi ��IP�A�h���X)/device/dl_file  
  
 �Emysql_client(�R�}���h���C�����瓮��m�F)  
     �܂����O�ɁAdev_info.conf ��MYSQL_CONF�AMYSQL_TABLE�AQUERY_CONDITIONS ��ݒ肵�Ă��������B�ݒ�̓t�@�C������samaple���Q�l�ɂ��Ă��������B  
     ����mysql_key_val.conf ����"INFO_COMMENT"�ȉ��̒l��ݒ肵�Ă��������B"INFO_COMMENT"�ȉ��̒l�́Amysql�̃e�[�u���̃J�������ɑ���������̂ł��B
     
       �J����: �l
     
     2�t�@�C���̐ݒ��A�^�[�~�i����2�J���ȂǁA�R�}���h���C���̉�ʂ�2�p�ӂ��Ă�������(���ꂼ��terminal_a�Aterminal_b �Ƃ��܂�)  
     $ cd /home/pi/  
     terminal_a:  
        $ python3 /home/pi/sac/mysql_client.py  
     terminal_b:  
        $ python3 /home/pi/max/dev_ctrl.py apply_mysql_key_val  
  
    ��������΁Amysql_key_val.conf�Ɏw�肵���J�����̒l��mysql�ɐݒ肳��Ă���l�ɏ����ĕω����܂��B
  
 �Emysql_client(Web�y�[�W���瓮��m�F)  
     �R�}���h���C������m�F�� terminal_a �̃R�}���h��ł�����ł���A�u���E�U��flask_test_page���ɂ���"sacmax."�̃��S���N���b�N���Ă�������  
     ���邢�͈ȉ���url�ɃA�N�Z�X���Ă�������  
     http://(Raspberry Pi ��IP�A�h���X)/device/apply_mysql_key_val  
  
  
##Install  
  
  ��sacmax.core�̃Z�b�g�A�b�v�܂ł͏I�������Ă����Ă�������  
  �����O�� sudo apt-get update �����Ă����Ă�������  
  �����ł�setup_sacmax_with_server ��zip�t�@�C��(setup_sacmax_with_server.zip)�ɂ����O��Ő��������Ă��܂��BPeaZip�Ȃǈ��k�𓀃A�v���������p���������B�܂�win8�ȍ~�̏ꍇ�͐V�K�쐬����쐬�\�ł��B  
  
  1.setup_sacmax_with_server.zip�� /home/pi��Ƀ_�E�����[�h���Ă�������(zip���Ă��Ȃ��Ƃ��A�_�E�����[�h��� /home/pi �ł�)
  2.$ unzip setup_sacmax.zip (zip���ăC���X�g�[�����Ă��Ȃ���Εs�v�ł�)  
  3.$ cd setup_sacmax_with_server  
  4.$ sudo sh install_nginx_sacmax.sh install  
  5.$ sudo sh install_with_server.sh install  
  6. /home/pi/sac ���ɒǉ����ꂽ ftp_client.py�Amysql_client.py �̃R�����g�ɏ]���A/home/pi/max/cmd_def.py �� /home/pigeneral.conf �ɒǋL  
  
##Licence  
  
