from pwn import *
from Crypto.Cipher import DES3
from time import time
from pytimedinput import timedInput
from binascii import unhexlify

host ="dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
port= 9999

r = remote(host,port)

print(r.recvline())
s = r.recvline().decode("utf-8")
num = s[0:-4]
num1 = str(num).partition("*")[0].strip()
num2 = str(num).partition("*")[2].strip()

ans = int(num1) * int(num2)
print("ans = " + str(ans))

r.sendline(str.encode(str(ans)))
print(r.recvline())

encrypted = r.recvline().strip().decode("utf-8")

key = str(int(time())).zfill(16).encode("utf-8")
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
decrypted = cipher.decrypt(bytes.fromhex(encrypted))

print("decrypted = " + str(decrypted))

r.sendline(decrypted)

r.interactive()