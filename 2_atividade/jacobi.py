
from numpy import array, zeros, diag, diagflat, dot

def Jacobi(A, b, N, x):
                                                                                                                                                                   
    # (1) Create a vector using the diagonal elemts of A
    D = diag(A)
    # (2) Subtract D vector from A into the new vector R
    R = A - diagflat(D)

    # (3) We must Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[2.0,1.0],[5.0,7.0]])
b = array([11.0,13.0])
x = array([1.0,1.0])

sol = Jacobi(A,b, 25, x)

print("Solution for x is: ", sol)