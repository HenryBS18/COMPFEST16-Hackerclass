# Title
Pekan AES (500 points)

# Flag
COMPFEST16{ECB_kurang_bagus_untuk_dipake_bro_gak_jaman_61abdb8843}

# Description
ECB mode is secure right?

```bash
nc challenges.ctf.compfest.id 20015
```

# Author
swusjask

# Solution
we know that AES ECB mode is encrypted independently each block.

so i try i encrypt 2 plaintext and then concat it.

first plaintext is **111111111111111C**, its 16 bytes. the AES uses padding of 16 bytes it will add 16 more bytes of padding.

so if i encrypt 15 bytes plaintext it will add 1 more byte of padding caused of padding rule.

**11111111111111C** (15 bytes) -> **997d50d0cb67c25c6ee3f578debdbb9f**
**111111111111111C** (16 bytes) -> **34b9cd6f87ee17569aeadfc119b01c9544ddecf583190f619e4e5c5b7a87af49**

if i input 16 bytes plaintext, the length of the encrypted plaintext will increase, because it adds 16 bytes of padding.

if we construct the 16 bytes of plaintext + 16 bytes of padding it will be like this:
**11111111 1111111C -------- --------**
**34b9cd6f87ee1756 9aeadfc119b01c95 44ddecf583190f61 9e4e5c5b7a87af49**

the last 2 blocks is just padding, so we can remove it.

so 
**11111111 1111111C** -> **34b9cd6f87ee1756 9aeadfc119b01c95**

second plaintext **OMPFEST16** -> **fe87a1cc315419d075367f0a27451d01**

then concat the first and second ciphertext:
**34b9cd6f87ee17569aeadfc119b01c95** + **fe87a1cc315419d075367f0a27451d01** -> **34b9cd6f87ee17569aeadfc119b01c95fe87a1cc315419d075367f0a27451d01**

then submit it