def lonelyinteger(a):
    # Write your code here
    new_a = sorted(a)
    num = new_a[0]
    i = 1
    while i < len(new_a):
        if num != new_a[i]:
            break
        else:
            i += 1
            num = new_a[i]
            i += 1
    return num

a = [1,2,3,4,3,2,1]
result = lonelyinteger(a)
print(result)