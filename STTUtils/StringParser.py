import string
import subprocess
import base64
import re

def isPrintable(s):
    for i in s:
        if i not in string.printable:
            return False
    return True

b16_charset = string.digits + 'abcdef'
b64_charset = string.ascii_letters + string.digits + '=+/'

class Parser:
    def __init__(self, filer,minLen = 3, maxLen = 100,flag=None,isFIle=True):
        
        if isFile:
            self.lst=subprocess.check_output(('strings','-n', str(minLen), filer)).split('\r\n')[5:]
        else:
            self.lst = filer.split('\n')
        self.lst = [i for i in self.lst if i!= '' and len(i) < maxLen*2]
        self.deco = []
        self.flag = flag

        toExec = [self.getBase64,self.getBase16,self.getBase32]

        for i in toExec:
            try:
                i()
            except Exception as e:
                print e

        try:
            if self.flag is not None:
                    self.potentialRes()
                    print self.maxPotFlags
        except Exception as e:
            print e
            
        
        

    def getBase64(self,minlen = 0, maxLen = 0):
        self.b64s = [i for i in self.lst if isBase64(i)]
        self.deco64 = [i.decode('base64') for i in self.b64s if isPrintable(i.decode('base64'))]
        self.deco.extend(self.deco64)
        


    def getBase32(self,minlen = 0, maxLen = 0):
        self.b32s = [i for i in self.lst if isBase32(i)]
        self.deco32 = [base64.b32decode(i) for i in self.b32s if isPrintable(base64.b32decode(i))]
        self.deco.extend(self.deco32)


    def getBase16(self,minlen = 0, maxLen = 0):
        self.b16s = [i for i in self.lst if isBase16(i)]
        self.deco16 = [i.decode('hex') for i in self.b16s if isPrintable(i.decode('hex'))]
        self.deco.extend(self.deco16)


    def potentialRes(self):
        self.potFlags = []
        if self.flag is None:
            self.flag = raw_input('Whats the flag?')
    
        self.potFlags = list(set([i for i in self.deco if self.flag in i]))
        self.potFlags.extend(list(set([i for i in self.lst if self.flag in i])))

        self.maxPotFlags = []
        
        r = r'%s\{(.*?)\}'%self.flag
        a = re.compile(r)
        for i in self.potFlags:
            tmp =  a.findall(i)
            if tmp:
                self.maxPotFlags.append(i)
        
        
            


def isBase64(s):
    try:
        enc = base64.b64encode(base64.b64decode(s)).strip()
        return enc == s
    except TypeError:
        return False

def isBase32(s):
    try:
        enc = base64.b32encode(base64.b32decode(s)).strip()
        return enc == s
    except TypeError:
        return False

def isBase16(s):
    s = s.upper()
    try:
        enc = base64.b16encode(base64.b16decode(s)).strip()
        return enc == s
    except TypeError:
        return False



def testMe():
    import os
    os.chdir('C:\Users\jeanb\Downloads')
    test = Parser('flagconverter.dmp',minLen=60,flag='ALLES{')
    return test
    
