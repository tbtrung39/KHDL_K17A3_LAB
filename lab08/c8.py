#lambda 
def f(x):
    return x+1
# viết từ hàm tt ra lambda
lambda x: x+1  
def f(x,y):
    if x>y:
        return x
    else:
        return y
lambda x,y: x if x>y else y

def f(x,y):
    if x>1:
        return x
    elif y>2:
        return y
    else:
        return x+y
lambda x,y: x if x>1 else y if y>2 else x+y

def f(n):
    result = 0
    for i in range(n):
        result +=i
    return result
lambda n: sum([i for i in range(n)])

def f(x):
    if x>0:
        return True
    else:
        return False 

