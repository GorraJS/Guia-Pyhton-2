min = []
max = []
def partList(m,n):
    for x in range(0,len(m),1):
        if m[x] <= n:
            min.append(m[x])
        elif m[x] > n:
            max.append(m[x])
    for y in range(0,len(max),1):
            min.append(max[y])
    return min
print(partList([6,3,4,8,2,9],4))