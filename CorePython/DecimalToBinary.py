num = 17
print(bin(num)[2:])      # remove  0b from "0b10001"

ret = []

def decimal_to_bin(num):
    if num >= 1:
        decimal_to_bin(num // 2)      ## gives whole value after div
        bin =  num % 2
        ret.append(bin)
    return ret



bin_rep = decimal_to_bin(num)
print("".join(str(x) for x in bin_rep))
