x,y,z = map(int, input("Nhập tọa độ của không gian Oxyz: "). split())
mp_Oxy = (-x ,-y, z)
mp_Oxz = (-x, y, -z)
mp_Oyz = (x, -y, -z)
print("Tọa độ điểm đối xứng của mặt phẳng Oxy là: ", mp_Oxy)
print("Tọa độ điểm đối xứng của mặt phẳng Oxz là: ", mp_Oxz)
print("Tọa độ điểm đối xứng của mặt phẳng Oyz là: ", mp_Oyz)