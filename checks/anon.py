from ftplib import FTP


"""
anon() tries to login anonymously
"""
def anon(host):
    try:
        ftp = FTP(f'{host}')
        ftp.login() # anonymous login, user = anonymous & password = anonymous@
        ftp.quit()

        return True
    except:
        return False