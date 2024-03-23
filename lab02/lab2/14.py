i = float(input('Nhập cường độ âm: '))
i0= 10**-12
import math
L1 = 10*(math.log((i/i0),10))
if L1 >100 or L1 <=0:
    print(f'Ở ngưỡng {i} W/m^2 người này không nghe thấy.')
else:
    print(f'Ở ngưỡng {i} W/m^2 người này nghe thấy.')