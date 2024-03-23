import math 
print(" Mời bạn nhập các giá trị cần tính ")
x = float(input())
y = float(input())
z = float(input())
print("bạn đã nhập các giá trị cần tính là ", x, y, z)
nAl2o3 = float(x/(27+16*3))
nNaoH = float(y*0.1)
nHcl = float(z*0.1)
# Phương trình đã cho là al203 + 2naoh -> 2naalo2 + h20
if nNaoH/2 <= nAl2o3:
    nNaalo2 = nNaoH
    if nHcl <= nNaalo2:
        print("sau phản ứng có kết tủa")
    else:
        nhcldu = nHcl - nNaalo2 
        if nhcldu >= 3*nNaalo2:
            print("sau phản ứng không có kết tủa do kết tủa bị tan ")
        else:
            print("Sau phản ứng có kết tủa ")
else:
    nNaohdu = nNaoH/2 - nAl2o3
    if nHcl <= nNaohdu:
        print("sau phản ứng không có kết tủa")
    elif nHcl > nNaohdu and nHcl <= nNaohdu + (2*nAl2o3)*3:
        print("sau phản ứng có kết tủa")
    else:
        print("sau phản ứng không có kết tủa")