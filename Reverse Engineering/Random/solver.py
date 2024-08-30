import random

destroyed = b'!vP3\xc2\x91\xc2\x89\x11\x1f\x06C\x17_\x19t)\xc2\x929\x06li\x1d\x1f\xc2\x88*\x19E+4E\x16\x07v1S$\x1a c\x1flcr4> 3vlt\xc2\x85Yj-$0 '.decode('utf-8', errors='ignore')

def reverse_process(destroyed, flag_prefix):
    for i in range(100):
        flag_guess = flag_prefix + str(i).zfill(2)
        random.seed(int(flag_guess[8:10]))
        for c in flag_guess[:8]:
            random.seed(random.randint(1, 0xCF) + ord(c))

        reconstructed_flag = ""

        for char in destroyed:
            if isinstance(char, str):
                char = ord(char)
            offset = random.randint(1, 10)
            MyFriend = random.randint(1, 127)
            result = char
            if random.randint(0, 1):
                result -= 0x16
            original_char = chr((result ^ MyFriend) + offset)
            reconstructed_flag += original_char

        if reconstructed_flag.startswith(flag_prefix):
            print(f"Possible flag: {reconstructed_flag}")
            return reconstructed_flag

    return None

# Contoh prefix flag: "FLAG{" atau yang sesuai dengan format dari CTF
flag_prefix = "COMPFEST16{"
reverse_process(destroyed,flag_prefix)