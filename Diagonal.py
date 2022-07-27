import random as rd
import numpy as np

def random_n_matrix(n): 
    mat = [rd.randint(0,99) for i in range(1,n*n + 1,1)]
    mat = np.reshape(mat,(n,n))
    return mat

def diagonals(m):
    diag = [m.diagonal(0),np.fliplr(m).diagonal()]
    points = abs(np.sum(diag[0]) - np.sum(diag[1]))
    return points

w = random_n_matrix(int(input("Por favor indique el tamaño de la matrix: ")))

print("La diferencia diagonal es de: ",diagonals(w))
