I = float(input("Nhập cường độ âm: "))
import math
L = 10*math.log(I/math.pow(10,-12))
if L >=100:
  print("Người đó có thể nghe được")
else:
  print("Người đó không nghe được")