# SealTeamTools

## Intro and motivation

When I started CTFing on the reg, I quickly saw the potential of automating certain tasks that arise in many, many CTFs. It might be something as dump as opening a connection to some remote server and sending/receiving data. Or quickly converting from one format to another without having to rewrite the code every time. Another example was RSA, I wrote a small wrapper script that quickly gets me a plaintext for a given ```c```, ```q```,```p``` and ```e```. 

At this point the main question that will arise is, why not use [pwntools](https://pypi.org/project/pwntools/)? Well, it turns out that pwntools doesn't really play well with Windows. I love my Kali as much as the next guy for a variety of tasks but I also love my Win10. So I set off to slowly recreate some of the more popular functions. Fact is, the really complex functions of pwntools are not something you encounter often which means a light version fits my purposes.

Now, my motto is Go Big or Go Home. So I decided to build a comprehensive framework for CTFing and general pentesting that covers the most frequent topics: Crypto, Web, Forensics and some misc. I do most of my reversing in IDA/gdb so that category won't be represented much, I think. Additionally I have a general and socket category, the latter to make socket interaction smoother (e.g. I struggled time and again with socket blocking, it would freeze when trying to receive data when none was available), the former aiming to perform helper tasks like transposing arrays, recognizing patterns etc.

I will use this as my MCH (Main Control Hub) for progress and as time progresses, and is permitting, build an orchestrator to bring all partial scripts under one "roof".


### Changelog
24.9: Rearranged file structure. Now all modules will be organized using "STTxxx.filename" where xxx is the overall structure. Makes it easier to import stuff as well.

6.10: STT now available on [pypy] (https://pypi.org/project/SealTeamTools/)

10.10: added various features, started working on Web Package



## Structure 

#### 1. General
- [ ] Pattern recognition
  - [x] Base64 --> STTUtils.StringParser
  - [x] Base32 --> STTUtils.StringParser
  - [x] Hex --> STTUtils.StringParser
  - [x] flags --> STTUtils.StringParser
  - [ ] Words
- [ ] Encodings
  - [ ] all bases
  - [x] rot13 --> STTUtils.encodings
- [x] Socket --> STTSocket.STTSocket
  - [x] recvline
  - [x] recvlines
  - [x] recvutil
  - [x] sendline

#### 3. Crypto
- [ ] AES
  - [ ] CBC
  - [ ] ECB
- [ ] RSA
  - [ ] Factorisation
  - [ ] Common modulus
  - [ ] Fault
  - [ ] Coppersmith
  - [x] General solve --> STTCrypto.STTRSA.RSASolver (Accesible through STTCrypto.STTRSA.Orchestrator)
  - [x] Multi-primes --> STTCrypto.STTRSA.multiPrime (Accesible through STTCrypto.STTRSA.Orchestrator)
  - [x] Wiener --> STTCrypto.STTRSA.wienNerhacker (Accesible through STTCrypto.STTRSA.Orchestrator)
- [ ] ECC
- [ ] DES
- [ ] Common ciphers
  - [ ] Caesar
  - [ ] Railcipher
  - [ ] Vigenere
- [x] Morse --> STTCrypto.morse


#### 4. Web
- [ ] Flask
- [ ] Nodejs
  - [ ] Handlebar
- [ ] XSS
- [ ] WAF Bypass
- [x] LFI --> --> STTWeb.LFITester

#### 5. Forensics
- [ ] Images
  - [ ] LSB
  - [ ] MSB
  - [ ] exiftool
  - [ ] XOR
- [ ] Audio

#### 6. Misc
- [ ] Pyjails
- [ ] Bashjails
- [ ] Esolangs
- [ ] Embedded files
  - [ ] binwalk
- [ ] Memdumps
  - [ ] Vola
- [ ] OCR
- [x] QR --> STTUtils.utils
- [x] Packing --> STTUtils.packing
