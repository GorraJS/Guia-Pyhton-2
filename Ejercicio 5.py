m = [[],[]]

def Scalar(v1,v2):
    n = len(v1)
    for i in range(n):
        for j in range(n):
            m[i].append((v1[i][j] * v2[i][j]))
    return m
print(Scalar([[1,2],[3,4]],
             [[2,0],[1,2]]))