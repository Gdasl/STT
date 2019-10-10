import base64
import string

def b64d(s):
    n = 0
    while n < 6:
        try:
            res = base64.b64decode(s + '='*n)
            return res
        except Exception as e:
            try:
                res = base64.urlsafe_b64decode(s + '='*n)
                return res
            except Exception as e:
                pass
    return None

def rot13(s):
    aLo = string.ascii_lowercase
    aUp = string.ascii_uppercase
    s2 = ''
    for i in s:
        if i in aLo:
            s2 += aLo[(aLo.index(i) + 13)%26]
        elif i in aUp:
            s2 += aUp[(aUp.index(i) + 13)%26]
        else:
            s2 += i
    return s2
            
        
    
