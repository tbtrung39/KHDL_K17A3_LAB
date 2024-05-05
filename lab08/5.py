def tim_ulcn(a,b):
    if b==0:
        return a
    return tim_ulcn(b,a%b)
print(tim_ulcn(4,10))