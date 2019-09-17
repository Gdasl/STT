from utils import socki
import requests

class STTSocket:
    def __init__(self,add):
        self.s = socki(add)
        self.s.settimeout(2)

    def sendline(self, m):
        self.s.send(m+'\n')

    def recv(self,n):
        try:
            data = self.s.recv(n)
        except Exception as err:
            if 'timed out' in err:
                print 'timeout error'
            else:
                print err
        return data

    def recvline(self):
        try:
            data = ""
            i = self.s.recv(1)
            data += i

            while i != '\n':
                i = self.s.recv(1)
                data += i
        except Exception as err:
            if 'timed out' in err:
                print 'timeout error'
            else:
                print err
        return data

    def recvuntil(self,u):
        data = ""
        try:
            currentWindow = data

            while currentWindow != u:
                i = self.s.recv(1)
                data += i
                currentWindow = data[-(min(len(data),len(u)))]

        except Exception as err:
            if 'timed out' in err:
                print 'timeout error'
            else:
                print err
        return data
