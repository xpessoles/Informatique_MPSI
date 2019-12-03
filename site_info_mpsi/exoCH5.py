import numpy
M=[[4,7,9],[1,2,6],[3,3,8],[4,1,5]]

def maxi_double(M):
    nligne,ncol=len(M),len(M[0])
    max=M[0][0]
    for i in range(nligne):
        for j in range(ncol):
            if M[i][j]>max:
                max=M[i][j]
    return max

def maxi_double2(M):
    nligne,ncol=np.array(M).shape
    for i in