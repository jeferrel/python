def diagonalDifference(arr):
    # Write your code here    
    res = 0
    diagonal_principal = 0
    diagonal_secundaria = 0
    for f, fila in enumerate(arr):
        for c, columna in enumerate(arr):
            if f == c:
                if f == int(len(fila) / 2):
                    diagonal_principal += arr[f][c]
                    if len(fila) % 2 == 0:   
                        c = len(columna) - 1 - f
                        diagonal_secundaria += arr[f][c]
                    else:    
                        diagonal_secundaria += arr[f][c]
                else:
                    diagonal_principal += arr[f][c]
                    c = len(columna) - 1 - f
                    diagonal_secundaria += arr[f][c]
                break
    print(f"Diagonal principal: {diagonal_principal}")
    print(f"Diagonal secundaria: {diagonal_secundaria}")
    res = abs(diagonal_principal - diagonal_secundaria)
    return res

# Matriz 3x3
matriz = [[6,8],
          [-6, 9]]
result = diagonalDifference(matriz)
print(result)
