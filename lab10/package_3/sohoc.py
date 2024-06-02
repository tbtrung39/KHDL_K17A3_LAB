def ucln(a,b):
    if a ==0:
        return b
    elif b ==0:
        return a
    else:
        return ucln(b % a, a)
    
def bcnn(a,b):
    return (a // ucln(a,b)) *b

def sum_divisor(n):
    sum = 0
    for j in range(n):
        if n % j ==0:
            sum += j
    return sum
