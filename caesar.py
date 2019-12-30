from cs50 import get_string
from sys import argv


if len(argv)!=2:
    print("Usage: python caesar.py k")
    exit(1)
s = get_string("plaintext: ")
outstr=""

k = int(argv[1])
k=k%26

for i in range(len(s)):
    #for small
    if ord(s[i])>=97 and ord(s[i])<=122:
        if ord(s[i])+k>122:
            outstr += chr(ord(s[i])+k-26)
        else:
            outstr += chr(ord(s[i])+k)

    #for caps
    elif ord(s[i])>=65 and ord(s[i])<=90:
        if ord(s[i])+k>90:
            outstr += chr(ord(s[i])+k-26)
        else:
            outstr += chr(ord(s[i])+k)

    #all rest
    else:
        outstr += s[i]

print("ciphertext: ", end="")
print(outstr)