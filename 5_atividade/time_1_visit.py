# Micael Machado Gomes
## Trabalho de Processos Estocásticos
## Determinação da Tempo de 1ª visita

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


def prob_1_visit(mat, ei, ef, n):
    if n == 1:
        return mat[ei][ef]
    else:
        value = 0
        for k in range(len(mat)):
            if k != ef:
                value += mat[ei][k] * prob_1_visit(mat, k, ef, n-1)

        return value


def time_1_visit(mat, ei, ef, n):
    if n == 0:
        return 1
    elif n == 1:
        return mat[ei][ef]
    else:
        value = 0
        for m in range(1,n+1):
            value += prob_1_visit(mat, ei, ef, m) * time_1_visit(mat, ef, ef, n-m)

        return value

def main():
    matriz = Matriz()
    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        ei = int(input("insira o estado inicial: "))
        ef = int(input("insira o estado final: "))
        n = int(input("insira o Nº de Passos: "))
        print(time_1_visit(mat, ei, ef, n))

    else:
        print("Não é estocástico!")


# Local Testes
if __name__ == '__main__':
    main()
