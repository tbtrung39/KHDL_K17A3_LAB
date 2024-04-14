def kiem_tra_mat_khau(mat_khau):
    for i in mat_khau:
        if not i.isupper():
            return False
        elif not i.islower():
            return False
        elif not i.isdigit():
            return False
        elif len(mat_khau) < 6:
            return False
        elif not i in "$#@" :
            return False
        elif len(mat_khau) >12:
            return False
    return True

mat_khau = input('nhap mat khau: ')
if kiem_tra_mat_khau(mat_khau):
    print('mat khau hop le')
else:
    print('mat khau khong hop le')