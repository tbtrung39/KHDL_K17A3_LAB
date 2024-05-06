def nam_nhuan(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    return False
def max_days_in_month(m,y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m==2:
        if nam_nhuan(y):
            return 28
        return 29
    return -1
print(max_days_in_month(2,2024))