TNCT = int(input("Tháng thâm niên công tác là: "))
if TNCT <12:
  he_so = 2.34
elif TNCT >=12 and TNCT <36:
  he_so = 3.33
elif TNCT >=36 and TNCT <60:
  he_so = 3.66
elif TNCT >=60:
  he_so = 3.99
luong = he_so * 1350000
print("Lương nhân viên là: ", luong)