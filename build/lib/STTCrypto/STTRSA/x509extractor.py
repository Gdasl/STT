import OpenSSL

def extractx509(cert):
     x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
     a = x509.get_pubkey().to_cryptography_key().public_numbers()
     return a.n, a.e
     
