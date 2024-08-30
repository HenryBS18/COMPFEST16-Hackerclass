from pwn import remote

pt_1 = b"1111111111111111111111111111111C"
pt_2 = b"OMPFEST16"

r = remote('challenges.ctf.compfest.id', 20015)

r.sendlineafter(b'>> ', b'1')
r.sendlineafter(b'Message: ', pt_1)

ct_1 = r.recvline().decode().replace('Encrypted Message (hex): ', '')[:64]

r.sendlineafter(b'>> ', b'1')
r.sendlineafter(b'Message: ', pt_2)

ct_2 = r.recvline().decode().replace('Encrypted Message (hex): ', '')

ct_full = (ct_1 + ct_2).encode().strip()

r.sendlineafter(b'>> ', b'2')
r.sendlineafter(b'Encrypted Message (hex): ', ct_full)

flag = r.recvline().strip().decode()

r.close()
print(flag)

