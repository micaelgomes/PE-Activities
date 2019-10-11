# Micael Machado Gomes
## Disciplina de Processos Estocásticos
## Atividade de tempo esperado

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

        return True

def main():
    matriz = Matriz()

    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        # ei = 2 # estado inicial
        # ef = 0 # estado final
        ei = int(input("insira o estado inicial:   "))
        ef = int(input("insira o estado final:   "))
        
        # Matriz eleminando estados pertecentes -> I e A
        mat_p = []

        if ei <= len(mat) and ef <= len(mat) and ef >= 0 and ei >= 0:
            for i in range(len(mat)):
                tmp = []
                for j in range(len(mat[i])):
                    if ef != i and ef != j :
                        tmp.append(mat[i][j])

                if tmp:
                    mat_p.append(tmp)

            for i in range(len(mat_p)):
                for j in range(len(mat_p[i])):
                    if i == j :
                        mat_p[i][j] = mat_p[i][j] - 1

                    mat_p[i][j] = mat_p[i][j] * (-1)

        else:
            print("out range")

    if mat_p:
        b = np.ones(len(mat_p))
        x = np.linalg.solve(mat_p, b)
        print(x)


if __name__ == "__main__":
    main()