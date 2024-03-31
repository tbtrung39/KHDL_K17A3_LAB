a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
d = int(input("Nhập hệ số d: "))
r = int(input("Nhập bán kính r: "))
toa_do_IM = ((a-c)**2 + (b-d)**2)**0.5
if toa_do_IM >r:
  print("M nằm ngoài đường tròn")
elif toa_do_IM ==r:
  print("M nằm trên đường tròn")
elif toa_do_IM <r:
  print("M nằm trong đường tròn")
  