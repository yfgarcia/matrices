

 

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

print("Seleccione como generar la matriz")
print("1. Manual")
print("2. Automatica")
opc=int(input())

if opc==1:
    print("ingrese el orden de la matriz a calcular")
    n = int(input())
                
    matrizA=[]
    for i in range(n):
        matrizA.append([0]*n)

    #Rellenando la matriz
    for fila in range(n):
        for columna in range(fila,n):
            matrizA[fila][columna]=int(
                input(f"ingrese la posicion del numero {fila},{columna}:"))
    #imprimir matriz
        print("su matriz es la siguiente") 
        for i in matrizA:
            print(i,end="")
            print()           

    

elif opc==2:   

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
else:
     print("Seleccione una opcion correcta")



