#!/bin/bash


do_install(){
set -eu
    #mysql_client
    echo "sacmax with_server install..."
    apt-get install python3-mysql.connector -y

    if test ! -e /home/pi/sac; then
        echo "Please setup sacmax_core"
    else
        cp ./*.conf /home/pi
        cp ./setting_file_with_server/* /home/pi/sac -r
        
        echo "Please read comments in /home/pi/sac/mysql_client.py and ftp_downlorder.py"
    fi
    
    #ramdisk set
    ## path
    readonly RAMDISK_DIR='\/tmp\/ramdisk'
    readonly FSTAB='/etc/fstab'
    ##fstab
    sed -i -e "s/tmpfs.*/tmpfs      ${RAMDISK_DIR}  tmpfs   nodev,nosuid,size=4M 0    0/g" fstab 
    chown root:root fstab
    chmod 644 fstab

    cp -f ${FSTAB} ./fstab.bk
    cp -f ./fstab ${FSTAB}
}

case "$1" in
    install)
    do_install
    echo "installed!"
    ;;

    how_to)
    cat how_to_install.txt
    ;;

    *)
    echo "-------------WARNING!-------------"
    echo "  Mistake in your input." 
    echo "  If you try this shell, you can"
    echo "select these commands"
    echo "  1.install" 
    echo "  2.how_to" 
    exit 1
    ;;
esac


#end