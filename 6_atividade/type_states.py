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

def acessible(mat):
    qtd = 0

    for i in range(len(mat)):
        print(i, ' é acessível a partir de: {', end='')
        for j in range(len(mat[i])):
            if(mat[i][j] > 0):
                print(j, end=', ')
                qtd = qtd + 1

        print('}') 

    return qtd

def comunicable(mat):
    qtd = 0

    for i in range(len(mat)):
        print(i, ' é comunicante com: {', end='')
        for j in range(len(mat[i])):
            if(mat[i][j] > 0 and mat[j][i] > 0):
                print(j, end=', ')

        print('}')

    return qtd

def main():
    matriz = Matriz()
    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        resul = mat
        resul = np.dot(mat, resul)

        print(resul, '\n')
        acessible(resul)
        comunicable(resul)

    else:
        print("Não é estocástico!")      

if __name__ == "__main__":
    main()
