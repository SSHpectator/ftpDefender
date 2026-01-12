from checks.portCheck import checkPort
from checks.anon import anon
from checks.weakCreds import weakCreds
import sys

def main():
    if len(sys.argv) < 2:
        print("You have to specify an host\ne.g: example.com") 
        return
    
    host = sys.argv[1]
    if(checkPort(host)):
        anon(host)
        weakCreds(host)
    else:
        return "FTP port closed"

if __name__ == "__main__":
    main()