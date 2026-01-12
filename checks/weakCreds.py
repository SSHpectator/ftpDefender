from ftplib import FTP


#TODO insert wordlist from path
COMMON_CREDS = [
    ("admin", "admin"),
    ("test", "test"),
    ("ftp", "ftp"),
]

"""
weakCreds() tests for weak credentials
"""
def weakCreds(host):
    for user, pwd in COMMON_CREDS:
        try:
            ftp = FTP(host)
            ftp.login(user, pwd)
            ftp.quit()
            return (user,pwd)
        except:
            pass
    return None