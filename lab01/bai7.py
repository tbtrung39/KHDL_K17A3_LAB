#Viết chương trình nhập vào một tọa độ trong không gian Oxyz. Tính tọa độ của điểm đối xứng với nó qua mặt phẳng Oxy, Oxz, Oyz
Ax, Ay, Az = input("nhap toa do dinh A: ").split()
Ax, Ay, Az = float(Ax),float(Ay),float(Az)

print(f"diem dx qua mp Oxy là: {Ax},{Ay},{-Az}")
print(f"diem dx qua mp Oxz là: {Ax},{-Ay},{Az}")
print(f"diem dx qua mp Oyz là: {-Ax},{Ay},{Az}")
