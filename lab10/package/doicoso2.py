def loai_ki_tu(b):
    a='0123456789ABCDEF'
    k=''
    for i in b:
        if i.upper() in a:
            k+=i
    return k
def he_2_sang_he_10(a):
    return int(a,2)
def he_8_sang_he_10(a):
    return int(a,8)
def he_16_sang_he_10(a):
    return int(a,16)
