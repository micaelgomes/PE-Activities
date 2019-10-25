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


def acessible(mat, visit, start, end):
    path = 0

    if mat[start][end] > 0:
        return 1

    elif not start in visit:
        visit.append(start)

        for j in range(len(mat[start])):
            if mat[start][j] > 0:
                path += acessible(mat, visit, j, end)

    return path

def findClass(mat):
    visit = []
    clss = []  # classes da cadeia

    for i in range(len(mat)):
        tmp = set()
        if not i in visit:
            tmp.add(i)

            for j in range(len(mat[i])):
                if i != j:
                    if acessible(mat, [], i, j) and acessible(mat, [], j, i) > 0 and not j in tmp:
                        tmp.add(j)
                        visit.append(j)

            clss.append(tmp)

    return clss

def main():
    matriz = Matriz()
    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        resul = mat
        
        for _ in range(100):
            resul = np.dot(resul, resul)

        # print(resul, '\n')
        print('Estados Acessíveis: ')
        for i in range(len(resul)):
            for j in range(len(resul[i])):
                if acessible(resul, [], i, j):
                    print(i, ' -> ', j)
        
        print('Estados Comunicantes: ')
        for i in range(len(resul)):
            for j in range(i, len(resul[i])):
                if acessible(resul, [], i, j) and acessible(resul, [], j, i):
                    print(i, ' <-> ', j)

        clss = findClass(resul)
        print('Quantidade de Classes: ', len(clss))

    else:
        print("Não é estocástico!")      

if __name__ == "__main__":
    main()
