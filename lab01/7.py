# Nhập tọa độ của điểm P từ bàn phím
x, y, z = map(float, input("Nhập tọa độ của điểm P (cách nhau bởi dấu cách): ").split())

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxy
P_Oxy = (x, y, -z)

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
P_Oxz = (x, -y, z)

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
P_Oyz = (-x, y, z)

# In kết quả
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy: ({:.2f}, {:.2f}, {:.2f})".format(*P_Oxy))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz: ({:.2f}, {:.2f}, {:.2f})".format(*P_Oxz))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz: ({:.2f}, {:.2f}, {:.2f})".format(*P_Oyz))