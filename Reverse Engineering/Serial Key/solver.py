import random
import string
from pwn import remote

def generate_serial_key():
  chars = string.ascii_uppercase + string.digits
  key = ''.join(random.choices(chars, k=4)) + '-'
  key += ''.join(random.choices(chars, k=4)) + '-'
  key += 'CF16' + '-'
  key += ''.join(random.choices(chars, k=4)) + '-'
  key += ''.join(random.choices(chars, k=4))
  return key

def generate_serial_keys(n):
  return [generate_serial_key() for _ in range(n)]

serial_keys = generate_serial_keys(100)

r = remote('challenges.ctf.compfest.id', 20012)

for i, key in enumerate(serial_keys):
  r.sendlineafter(f'Serial {i+1} ==> '.encode(), key.encode())

r.interactive()
r.close()