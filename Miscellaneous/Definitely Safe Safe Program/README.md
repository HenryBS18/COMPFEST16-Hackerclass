# Title
Definitely Safe Safe Program (500 points)

# Flag
COMPFEST16{1nd3x_bYt3str1ng_g1v3s_1nT_e732bbe217}

# Description
I have made sure to filter my user inputs! Surely you can't get the flag...

**md5("COMPFEST16{flag_sha256(flag)[:10]}") = 950ff9f6286154973ea41436b0320001**. md5 ini digunakan untuk memvalidasi apakah flag yang kalian dapat sudah sesuai atau belum, jika kalian mengkomputasi md5 dari flag yang kalian dapatkan dan hasilnya tidak sesuai dengan yang diberikan, maka flag kalian belum benar.

```bash
nc challenges.ctf.compfest.id 20004
```

# Author
Zanark

# Solution
part 1:
```python
__doc__[::~False]
```

part 2:
```python
print(safe.__code__.co_consts[True][b'a'[False]^b'q'[False]])
```