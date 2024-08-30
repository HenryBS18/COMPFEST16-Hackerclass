# Flag
COMPFEST16{rfc_3514_security_bit_145eef449d}

# Solution
Evil bit
```bash
tshark -r traffic.pcapng -Y "ip.flags.rb == 0x010" -T fields -e data | xxd -r -p
```