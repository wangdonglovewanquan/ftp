import ftplib


def anon(hostname):
    try:
        ftp = ftplib.FTP()
        ftp.connect(hostname, 21)
        ftp.login('anonymous', 'ftp')
        print('success')
        ftp.quit()
        return True
    except Exception as e:
        print('failed')
        raise e
        return False


host = '113.105.164.33'
anon(host)


