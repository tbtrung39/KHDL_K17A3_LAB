r= float(input('nhap ban kinh= '))
h= float(input('nhap chieu cao= '))
dtxq=round(2*r*h*3.14,2)
stp=round(2*r*h + 2*(3.14*r**2),2)
v=round((3.14*r**2)*h,2)
print('dien tich xung quanh: ',dtxq)
print('dien tich toan phan: ',stp)
print('the tich: ',v)