def flippingBits(n):
    # Write your code here
    res = ""
    binario = bin(n)[2:].zfill(32)
    for caracter in binario:
        if int(caracter) == 0:
            res += "1"
        else:
            res += "0"
    return int(res, 2)


result = flippingBits(0)
print(result)