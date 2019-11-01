# Micael Machado Gomes
## Trabalho de Processos Estocásticos

import numpy as np
import math

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


def func_acc(mat, visit, start, end):
    path = 0

    if mat[start][end] > 0:
        return 1

    elif not start in visit:
        visit.append(start)

        for j in range(len(mat[start])):
            if mat[start][j] > 0:
                path += func_acc(mat, visit, j, end)

    return path
            

def transiente(mat):
    out = []

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i != j and mat[i][j] > 0 and not func_acc(mat, [], j, i): 
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
    trans = transiente(mat)
    absor = absorvente(mat)

    for i in range(len(mat)):
        if func_acc(mat, [], i, i) and i not in trans and i not in absor:
            out.append(i)
    
    return out

def mdc(pss):
    mdc = 1

    for i in range(len(pss)):
        mdc += math.gcd(1, pss[i])    

    return 2

def periodico(mat):
    out = []
    pss = []

    for i in range(len(mat)):
        if func_acc(mat, [], i, i):
            for j in range(len(mat[i])):
                indo = func_acc(mat, [], i, j)
                vltnd = func_acc(mat, [], j, i)
                
                if indo and vltnd:
                    pss.append(indo+vltnd)

            if i not in out and mdc(pss) > 1:
                out.append(i)

    return out

def ergodicos(mat):
    pass

def class_transiente(clss, mat):
    out = []

    for cl in clss:
        for k in cl:
            for i in range(len(mat)):
                if mat[k][i] > 0 and not func_acc(mat, [], i, k):
                    if cl not in out:
                        out.append(cl)

    return out

def class_recorrente(clss, mat):
    out = []
    trans = class_transiente(clss, mat)
    absor = class_absorvente(clss, mat)

    for cl in clss:
        for k in cl:
            for i in range(len(mat)):
                if func_acc(mat, [], k, k):
                    if cl not in out and cl not in trans and cl not in absor:
                        out.append(cl)

    return out
        
def class_absorvente(clss, mat):
    out = []

    for cl in clss:
        for k in cl:
            for i in range(len(mat)):
                if mat[k][i] == 1:
                    if cl not in out:
                        out.append(cl)

    return out

def findClass(mat):
    visit = []
    clss = []  # classes da cadeia

    for i in range(len(mat)):
        tmp = set()
        if not i in visit:
            tmp.add(i)

            for j in range(len(mat[i])):
                if i != j:
                    if func_acc(mat, [], i, j) and func_acc(mat, [], j, i) > 0 and not j in tmp:
                        tmp.add(j)
                        visit.append(j)

            clss.append(tmp)

    return clss

def findZero(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                return True

    return False


def main():
    matriz = Matriz()
    mat = np.array(matriz.getMat())

    if matriz.isStochastic():
        resul = mat.copy()
        # print(resul, '\n')

        for _ in range(100):
            resul = np.dot(resul, mat)

        # print(resul, '\n')
        # print('Estados Transientes: ', transiente(resul))
        # print('Estados Recorrentes: ', recorrente(resul))
        # print('Estados Absorventes: ', absorvente(resul))
        print('Estados Periódicos: ', periodico(resul))
        print('Estados Ergódicos: ', ergodicos(resul))

        clss = findClass(resul)
        
        print('Classes Transientes: ', class_transiente(clss, resul))
        print('Classes Recorrentes: ', class_recorrente(clss, resul))
        print('Classes Absorventes: ', class_absorvente(clss, resul))

        
    else:
        print("Não é estocástico!")      

if __name__ == "__main__":
    main()
