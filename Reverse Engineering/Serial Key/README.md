# Title
Serial Key (500 points)

# Flag
COMPFEST16{v3rY_st4nd4Rd_k3ygEn_3794611e09}

# Description
Classic reverse, classic serial key

```bash
nc challenges.ctf.compfest.id 20012
```

# Author
Zanark

# Solution
given file **soal**
decompile it
after see how to program works, i found that we should send 100 different serial key to get the flag.
so i make a script to generate the serial keys with format: **XXXX-XXXX-CF16-XXXX-XXXX**, where **X** can be alphabet or number.
then, i make a for loop to send 100 serial keys and get the flag.