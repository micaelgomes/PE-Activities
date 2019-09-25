# Micael Machado Gomes
## Trabalho de Processos Estocásticos
## Método de Kolmogorov

import numpy as np

class Matriz:
    def __init__(self, steps = 1): 
        self.mat = np.loadtxt('matriz')
        self.vpi = np.loadtxt('vpi')
        self.steps = steps

    def getMatrix(self):
        return self.mat

    def printMat(self):
        print(self.mat)

    def printVpi(self):
        print(self.vpi)

    def isStochastic(self):
        for i in range(len(self.mat)):
            cont = 0
            
            for j in range(len(self.mat[i])):
                cont += self.mat[i][j]
                if cont > 1:
                    return False

        return True

    def Kolmogorov(self, start, end, steps):
        states = len(self.mat)

        if steps == 1:
            return self.mat[start][end]

        value = 0
        for k in range(states):
            value += self.mat[start][k] * self.Kolmogorov(k, end, steps-1)

        return value

# Main
def main():
    steps = int(input("insira a quantidade de Passos:   "))
    start = int(input("insira o estado inicial:   "))
    end = int(input("insira o estado final:   "))

    mat = Matriz(steps)

    if mat.isStochastic():
        resul = mat.Kolmogorov(start, end, steps)
        print("saída:")
        print(resul)

    else:
        print("Não é Estocástico")


# Local Testes
if __name__ == '__main__':
    main()