# Title
PyASM (500 points)

# Flag
COMPFEST16{pYth0n_4sm_1s_3z_r1gtH?_6b6241e4c8}

# Description
Python but assembly. What??

```bash
nc challenges.ctf.compfest.id 20011
```

# Author
Zanark

# Solution
first we got a disassembled python code.

i try to reverse it back to python code.

from the code we know that the program wants us to input an password that match the conditions,
just calculate the equations then convert it to ASCII characters.

the password is ```h3ck3rman```.

submit and retrieve the flag.