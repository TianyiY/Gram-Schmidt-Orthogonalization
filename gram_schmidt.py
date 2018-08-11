import numpy as np

def gram_schmidt(Vectors,n=1):
    Vectors=np.array(Vectors,dtype=float)
    _, col=np.shape(Vectors)
    # GRAM
    if n==col:
        return Vectors
    else:
        for i in range(0,n):
            Vectors[:,n]=Vectors[:,n]-np.dot(np.dot(Vectors[:,i].T,Vectors[:, n])/np.dot(Vectors[:,i].T,Vectors[:,i]),Vectors[:,i])
        Vectors=gram_schmidt(Vectors,n=n+1)
    # SCHMIDT
    for k in range(col):
        Vectors[:,k]=Vectors[:,k]/np.linalg.norm(Vectors[:,k])
    return Vectors

A=[[1,1,0],[0,1,1],[1,0,1]]
B=[[4,-2],[3,1]]
C=[[3,2],[1,2]]
D=[[1,2,3],[2,1,3],[1,1,2],[2,3,1]]
print(gram_schmidt(A))

#OUTPUTS:

#A:[[ 0.70710678  0.40824829 -0.57735027]
#   [ 0.          0.81649658  0.57735027]
#   [ 0.70710678 -0.40824829  0.57735027]]

#B:[[ 0.8 -0.6]
#   [ 0.6  0.8]]

#C:[[ 0.9486833  -0.31622777]
#   [ 0.31622777  0.9486833 ]]

#D:[[ 0.31622777  0.5284982   0.72786026]
#   [ 0.63245553 -0.70466426  0.1119785 ]
#   [ 0.31622777 -0.05872202  0.27994626]
#   [ 0.63245553  0.46977618 -0.61588176]]
