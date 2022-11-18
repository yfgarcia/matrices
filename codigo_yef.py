
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
import numpy as np

   ## Creacion de funciones para calcular las matrices
diagonalIzquierda = lambda m: [m[i][i] for i in range(len(m))] #Diagonal de la matriz

def transitiva(mat): #Calcular si la matriz es transitiva
    #formula Mr = Mr + (Mr*Mr)
    mat = np.matrix(mat)
    resT = mat + (mat*mat)
    resultadoMatriz = (resT == mat).all()
    if resultadoMatriz:
        t = 1
    else:
        t = 0
    return t

def matriz(n): #Genera una matriz automaticamente
    m = [[0] * n for _ in range(n)]
    for fila in range(n):
        for columna in range(fila, n):
            m[columna][fila] = m[fila][columna] = random.randint(0,1)
    return m

def simetrica(mat,cont,n): #calcula la matriz simetrica 

   for fila in range (n):
            for columna in range(n):
                normal=mat[fila][columna]
                traspuesta=mat[columna][fila]
                if normal==traspuesta:
                    cont+=1
        
   if cont==(n*n):
        t=1
        print("su matriz es simetrica")
   else:
        t=0
        print("su matriz no es antisimetrica")
   return t

print("Seleccione como generar la matriz")
print("1. Manual")
print("2. Automatica")

opc=int(input())
contador=0

if opc==1:
    
    print("ingrese el orden de la matriz a calcular")
    n = int(input())
    
    matrizA=[]
    for i in range(n):
        matrizA.append([0]*n)

    #Rellenando la matriz
    for fila in range(n):
        for columna in range(n):
            matrizA[fila][columna]=int(
                input(f"ingrese la posicion del numero {fila},{columna}:"))
    #imprimir matriz
    print("su matriz es la siguiente") 
    for i in matrizA:
        print(i,end="")
        print()
 

    simetrica(matrizA,contador,n) #llamado de la matriz simetrica 
    resultado = matriz(n)  
    matrizA = np.matrix(resultado)       

elif opc==2: 
    
    print("ingrese el orden de la matriz a calcular")
    n = int(input())   
      
    resultado = matriz(n)
    
    matrizA = np.matrix(resultado)

else:
    
    print("Seleccione una opcion correcta")

#Calculando relaciones
Mtransitiva = transitiva(matrizA)
diagonal = diagonalIzquierda(resultado)

if sum(diagonal) == n:
    reflexiva = 1
else:
    reflexiva = 0
    
if sum(diagonal) == 0:
    irreflexiva = 1
else:
    irreflexiva = 0

print(matrizA) #Visualizando la matriz generada

print("Resultado analisis Reflexiva: ",
      reflexiva, ", Irreflexiva: ", irreflexiva,
      ", Transitiva: ", Mtransitiva)


