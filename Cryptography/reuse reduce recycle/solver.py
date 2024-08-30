from binascii import unhexlify
from pwn import xor, remote

r = remote('challenges.ctf.compfest.id', 20016)
r.sendlineafter(b'>> ', b'1')
r.sendlineafter(b'Message: ', b'COMPFEST is the best ctf ever made in the world')
my_enc = r.recvline().strip().decode().replace('Encrypted Message (hex): ', '')

r.sendlineafter(b'>> ', b'2')
ct = r.recvline().strip().decode().replace('Encrypted Message (hex): ', '')

print(f'{my_enc=}')
print(f'{ct=}')

r.close()

# 65170ee1671e1c6bd57f04f8c0ec4bf2dcb52ae0c2b4725473eeb65f3e7a38f6fa96b6eafa3c854e7fa9873dd27c9624
# 65170ee1671e1c6bc4200c91e2db7cb7cba33ccbaba4597632e5a75f3e3520e4c195a2bba72bc4437cbcc12fd27c9624

ct = unhexlify(ct)
enc_msg = unhexlify(my_enc)

assert len(ct) == len(enc_msg)

blob = xor(enc_msg, ct)
msg = b"COMPFEST is the best ctf ever made in the world"

flag = xor(blob, msg)
print('flag: ' + flag.decode())