from Crypto.Util.number import *
import gmpy2

from secret import messages, d

def keygen():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    phi = (p-1) * (q-1)
    e = gmpy2.invert(d, phi)
    return (n, int(e))

assert len(messages) == 5

file = open("output", "w")

for message in messages:
    pubkey = keygen()
    m = bytes_to_long(message.encode())
    c = pow(m, pubkey[1], pubkey[0])
    file.write("c: " +  str(c) + "\n")
    file.write("pubkey: " + str(pubkey) + "\n")
