posMin = []
posMax = []

def rotateList(arr,n):
    for x in range(0,len(arr),1):
        if x <= n:
            posMin.append(arr[x])
        elif x > n:
            posMax.append(arr[x])
    for y in range(0,len(posMin),1):
        posMax.append(posMin[y])
    return posMax

print(rotateList([1,2,3,4,5],2))