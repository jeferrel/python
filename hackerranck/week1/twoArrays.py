def twoArrays(k, A, B):
    # Write your code here
    A1 = sorted(A, reverse=True)
    B1 = sorted(B)
    i = 0
    while i < len(A1):
        if A1[i] + B1[i] < k:
            return "NO"
        i += 1
    return "YES"

A = [1, 3]
B = [3, 1]
k = 4
result = twoArrays(k, A, B)
print(result)

A = [2, 3, 1, 1, 1]
B = [1, 3, 4, 3, 3]
k = 5
result = twoArrays(k, A, B)
print(result)

A = [1, 5, 1, 4, 4, 2, 7, 1, 2, 2]
B = [8, 7, 1, 7, 7, 4, 4, 3, 6, 7]
k = 9
result = twoArrays(k, A, B)
print(result)

A = [3, 6, 8, 5, 9, 9, 4, 8, 4, 7]
B = [5, 1, 0, 1, 6, 4, 1, 7, 4, 3]
k = 9
result = twoArrays(k, A, B)
print(result)

A = [4, 4, 3, 2, 1, 4, 4, 3, 2, 4]
B = [2, 3, 0, 1, 1, 3, 1, 0, 0, 2]
k = 4
result = twoArrays(k, A, B)
print(result)

A = [2, 1, 3]
B = [7, 8, 9]
k = 10
result = twoArrays(k, A, B)
print(result)

A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 4
result = twoArrays(k, A, B)
print(result)