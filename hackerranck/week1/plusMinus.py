def plusMinus(arr):
    # Write your code here
    cont_negatives = 0
    cont_positives = 0
    cont_zeros = 0
    for i in arr:
        if i < 0:
            cont_negatives+= 1
        elif i > 0:
            cont_positives+= 1
        else:
            cont_zeros += 1
    print("{:.6f}".format(cont_positives / len(arr)))
    print("{:.6f}".format(cont_negatives / len(arr)))    
    print("{:.6f}".format(cont_zeros / len(arr)))

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)