a = [1,2,3,4,5,6]
n = len(a)
h = []

for i in range(n-1):
    for j in range(i+1,n):
        if a[j] == a[i]+1:
            h.append((i,j))
print(h)