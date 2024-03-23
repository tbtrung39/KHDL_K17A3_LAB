x = float(input(' Nhap vao mo so: '))
import math
f = (-x + math.sqrt(x**2+4))/(x**4+1)**(1/7)
f = round(f,2)
print(f)