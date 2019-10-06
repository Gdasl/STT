import string

mc = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----'
    }

mc_inv = {}
for i in mc.keys():
    mc_inv[mc[i]] = i
    

def isValid(i):
    for k in i:
        if k != '.' and k != '-':
            return False
    return True
def toMorse(s):
    return '/'.join(mc[i] for i in s.upper())

def fromMorse(s,separator = ' '):
    return ''.join(mc_inv[i] for i in s.split(separator) if isValid(i))
