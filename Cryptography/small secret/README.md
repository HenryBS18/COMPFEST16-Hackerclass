# Title
small secret (500 points)

# Flag
COMPFEST16{jUzT_sMaLl_S3cReT_bEtWe3n_uS_ed2c699bb3}

# Description
Hmmm....., There's something fishy about the secret key

# Author
swusjask

# Solution
i try to use https://www.dcode.fr/rsa-cipher, and i found the flag.

i also try to use wiener attack to find **d** value since the **e** value was a large number, then i found the d value.
after found the d value, i immediately decrypted it using the usual formula.