__author__ = 'xcfree'

import socket
import urllib
import platform


def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    ip_address = "0.0.0.0"
    sysstr = platform.system()
    #print sysstr
    if sysstr == "Windows":
        ip_address = socket.gethostbyname(socket.gethostname())
        print "Windows @ " + ip_address
    elif sysstr == "Linux":
        ip_address = getip()
        print "Linux @ " + ip_address
    elif sysstr == "Darwin":
        ip_address = socket.gethostbyname(socket.gethostname())
        print "Mac @ " + ip_address
    else:
        print "Other System @ some ip"

    f = urllib.urlopen("http://1.rpi2ip.sinaapp.com/upload_ip?ip=" + ip_address)
    if f.readline().lower() == 'ok':
        print 'successfully uploaded ip address'
    else:
        print 'failed to upload ip address'
