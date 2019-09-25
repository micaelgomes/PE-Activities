# Micael Machado Gomes
## Trabalho de Processos Estocásticos
## Método simples ulizando matriz de transição

import numpy as np
import sys

class Matriz:
    def __init__(self, steps = 1): 
        self.mat = np.loadtxt('matriz')
        self.vpi = np.loadtxt('vpi')
        self.steps = steps

    def printMat(self):
        print(self.mat)

    def printVpi(self):
        print(self.vpi)

    # Multiplicação de Matrizes
    def multMratix(self):
        resul = self.mat
        for _ in range(self.steps - 1):
            resul = np.dot(self.mat, resul)

        return resul

    def isStochastic(self):
        for i in range(len(self.mat)):
            cont = 0

            for j in range(len(self.mat[i])):
                cont += self.mat[i][j]
                if cont > 1:
                    return False

        return True

# Main
def main():
    steps = int(input("insira a quantidade de Passos:   "))
    mat = Matriz(steps)

    if mat.isStochastic():
        if len(sys.argv) >= 2:
            if sys.argv[1] == "vpi":
                
                # Pra testar com VPI tem passar 'vpi' como argumento na compilação
                
                print("\nVPI:")
                print(np.dot(mat.multMratix(), mat.vpi))

            else:
                print("Argumento não definido!")

        else:
            print("Matriz de transição:")
            print(mat.multMratix())

    else:
        print("Não é Estocástico")

# Local Testes
if __name__ == '__main__':
    main()