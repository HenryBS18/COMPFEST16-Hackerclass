# Title
Power Prime (500 points)

# Flag
COMPFEST16{genie_genie_a_little_prime_exponent_ez_lah_ya_e78770dfec}

# Description
RSA warmup.

# Author
swusjask

# Solution
given a program that has output n, e, and c value.

its RSA

since its not possible to extract the p and q value, i tried to factor the n value using (https://www.alpertron.com.ar/ECM.HTM).

then i got the phi value.

let calculate the value of d (private key) by mod inverse **e** and **phi**

now we can decrypt the message by: c<sup>d</sup> % n