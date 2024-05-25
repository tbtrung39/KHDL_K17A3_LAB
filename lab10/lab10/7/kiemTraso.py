import random
def sinh_ngau_nhien():
    return [random.randint(0,100) for i in range(100)]
def kiem_tra_so_nt_chia_het_cho7(a):
    i=7
    k=[]
    for i in a:
        if i==7:
            k.append(i)
    return k
def tinh_tong_cac_so_le(a):
    k=0
    for i in a:
        if i%2!=0:
            k+=i
    return k
def cac_so_chinh_phuong(a):
    b=[]
    for i in a:
        if int(i**0.5)==i**0.5:
           b.append(i)
    if b==[]:
        return "khong có so chinh phuong trong day"
    else:
        return b