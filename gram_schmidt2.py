import numpy as np

def gram_schmidt(Vectors):
    Vectors=np.array(Vectors,dtype=float)
    _, col=np.shape(Vectors)
    # GRAM
    for j in range(1,col):
        for i in range(0, j):
            Vectors[:,j]=Vectors[:,j]-np.dot(np.dot(Vectors[:,i].T,Vectors[:,j])/np.dot(Vectors[:,i].T,Vectors[:,i]),Vectors[:,i])
    # SCHMIDT
    for k in range(col):
        Vectors[:,k]=Vectors[:,k]/np.linalg.norm(Vectors[:,k])
    return Vectors

A = [[1,1,0],[0,1,1],[1,0,1]]
print(A)
print(gram_schmidt(A))