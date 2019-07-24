def getAllWindows(L):
    for w in range(1, len(L)+1):
        if L[w] < L[w+1]:
            yield L[w+1]

v = [1, 2, 3]
print(list(getAllWindows(v)))
