"""
Simple util to pack payloads, essentailly a copy of some of the
functions of pwntools utils.packing
"""

def padHex(h):
    return '0' * (len(h)%2) + h

def pad(s,n):
    t=0
    if len(s)%n:
        t = (n-len(s)%n)
    return t*'\x00' + s


def p8(s, endian = 'small'):
    s = pad(padHex(hex(s)[2:].strip('L')).decode('hex'),1)

    if endian == 'small':
        s = s[::-1]
    return s

def p16(s, endian = 'small'):
    s = pad(padHex(hex(s)[2:].strip('L')).decode('hex'),2)
    if endian == 'small':
        s = s[::-1]
    return s

def p32(s, endian = 'small'):
    s = pad(padHex(hex(s)[2:].strip('L')).decode('hex'),4)
    if endian == 'small':
        s = s[::-1]
    return s
    

def p64(s, endian = 'small'):
    s = pad(padHex(hex(s)[2:].strip('L')).decode('hex'),8)
    if endian == 'small':
        s = s[::-1]
    return s
    
