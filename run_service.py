# coding=utf-8
"""
create:2019/3/8 19:01
author:feiying
describe: this function run only in window, in linux please use script start.sh
"""
import socket
import os
if __name__ == "__main__":
    myname = socket.getfqdn(socket.gethostname())  # get name
    myaddr = socket.gethostbyname(myname)          # get ip
    myaddr = '172.16.83.87'
    command = "python3 manage.py runserver {}:8019".format(myaddr)
    os.system(command)