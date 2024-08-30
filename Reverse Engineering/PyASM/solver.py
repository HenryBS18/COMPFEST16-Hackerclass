from pwn import remote

r = remote('challenges.ctf.compfest.id', 20011)

password = b'h3ck3rman'

r.sendlineafter(b'Enter THE password: ', password)

flag = r.recvlines(3)[2].strip().decode()
r.close()

print(flag)