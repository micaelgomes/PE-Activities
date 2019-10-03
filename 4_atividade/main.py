# Micael Machado Gomes
## Disciplina de Processos Estocásticos
## Atividade de tempo esperado

import numpy as np

class Matriz:
    def __init__(self): 
        self.mat = np.loadtxt('matriz')

    def getMat(self):
        return self.mat

    def isStochastic(self):
        for i in range(len(self.mat)):
            cont = 0

            for j in range(len(self.mat[i])):
                cont += self.mat[i][j]
                if cont > 1:
                    return False

        return True

def main():
    matriz = Matriz()

    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        ei = 0
        ef = 1
        mat = np.transpose(mat)
        # Matriz eleminando estados pertecentes -> I e A
        mat_b = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j :
                    mat[i][j] = mat[i][j] + 1

                # if ei == i and ef == j :


    # x = b*A^(-1)
    b = np.ones(len(mat))
    x = np.linalg.solve(mat, b)

    print(x)

if __name__ == "__main__":
    main()