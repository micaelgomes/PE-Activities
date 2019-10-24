# Micael Machado Gomes
## Trabalho de Processos Estocásticos
## Determinação da probabilidade de 1ª visita

import numpy as np


class Matriz:
    def __init__(self):
        self.mat = np.loadtxt('mat')

    def getMat(self):
        return self.mat

    def isStochastic(self):
        for i in range(len(self.mat)):
            cont = 0

            for j in range(len(self.mat[i])):
                cont += self.mat[i][j]
                if cont > 1:
                    return False
                if self.mat[i][j] < 0:
                    return False

        return True

def transiente(mat):
    out = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i != j and mat[i][j] > 0 : 
                if not i in out:
                    out.append(i)
    
    return out

def absorvente(mat):
    out = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j and mat[i][j] == 1:
                out.append(i)
    
    return out

def recorrente(mat):
    out = []
    tmp = []

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                tmp.append(i)

            if i in tmp and not i in out:
                out.append(i)
    
    return out

def main():
    matriz = Matriz()
    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        resul = mat
        # resul = np.dot(mat, resul)

        print(resul, '\n')
        print('Estados Transientes: ', transiente(resul))
        print('Estados Absorventes: ', absorvente(resul))
        print('Estados Recorrentes: ', recorrente(resul))

    else:
        print("Não é estocástico!")      

if __name__ == "__main__":
    main()