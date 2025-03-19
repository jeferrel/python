def miniMaxSum(arr):
    # Write your code here
    sorted_arr = (sorted(arr))
    minimum_sum = 0
    maximum_sum = 0
    for idx, numero in enumerate(sorted_arr):
        if idx == 0:
            minimum_sum += numero
        elif idx == (len(sorted_arr) - 1):
            maximum_sum += numero
        else:
            minimum_sum += numero
            maximum_sum += numero
    print(f"{minimum_sum} {maximum_sum}")

arr = [1,2,3,4,5]
miniMaxSum(arr)