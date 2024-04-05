m3 = [[],[],[]]
n = []
def multMatrix(m1,m2):
    for a in range(0,len(m1),1):
        for b in range(0,len(m1),1):
            m3[a].append(m1[a][b] * m2[b][a])
    return m3
print(multMatrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[9, 3, 2],[5, 8, 1],[6, 4, 7]]))