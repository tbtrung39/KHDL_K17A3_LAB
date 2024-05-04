import math
def chu_vi(x):
    chu_vi = 2*math.pi*x
    return chu_vi
def dien_tich(x):
    dien_tich = math.pi*(x**2)
    return dien_tich

x = float(input('Nhập vào bán kính R: '))
print(f'Chu vi hình tròn là: {chu_vi(x)}')
print(f'Diện tích hình tròn là: {dien_tich(x)}')