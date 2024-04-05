m3 = [[],[],[]]

def sumMatrix(m1,m2):
    for a in range(0,len(m1),1):
        for b in range(0,len(m1),1):
                m3[a].append(m1[a][b] + m2[a][b])
    return m3

print(sumMatrix([[1,1,1],[2,2,2],[3,3,3]],[[1,1,1],[2,2,2],[3,3,3]]))