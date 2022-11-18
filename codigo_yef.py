

 

""" M1 = [[0, 1, 0],
           [0,1,0], 
           [0,1,0]]

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i])
 """
import random
import pprint


def matriz(n):
    m = [[0] * n for _ in range(n)]
    for fila in range(n):
        for columna in range(fila, n):
            m[columna][fila] = m[fila][columna] = random.randint(0,1)
    return m

resultado = matriz(4)

diagonalIzquierda = lambda m: [m[i][i] for i in range(len(m))]

relacion = diagonalIzquierda(resultado)

print("diagonal", relacion)
print("")
pprint.pprint(resultado)
print("")



if sum(relacion) == 4:
    print("Es Reflexiva")
elif sum(relacion) == 0:
    print("Es irreflexiva")
else:
    print("No es ninguna")






