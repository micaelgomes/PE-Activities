# Micael Machado Gomes
## Trabalho de Processos Estocásticos
## Método simples ulizando matriz de transição

import numpy as np

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
        for _ in range(self.steps):
            resul = np.dot(self.mat, resul)

        return resul

# Main
def main():
    mat = Matriz(int(input()))

    print(mat.multMratix())
    print('VPI')
    print(np.dot(mat.multMratix(), mat.vpi))

# Local Testes
if __name__ == '__main__':
    main()