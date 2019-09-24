from STTUtils.utils import socki
import requests

#One of the ideas was to make this as compatible with pwntools as possible, e.g. when executing code from a teammate that uses it
class STTSocket:
    def __init__(self,add):
        self.s = socki(add)
        self.s.settimeout(2)

    def sendline(self, m):
        if type(m) != type(""):
            m = str(m)
        self.s.send(m+'\n')

    def send(self, m):
        if type(m) != type(""):
            m = str(m)

        if m[-1] != '\n':
            m+= '\n'
        self.s.send(m)

    def recv(self,n):
        data = ""
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

