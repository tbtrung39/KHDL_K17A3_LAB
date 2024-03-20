def doi_xung_qua_oxy(x, y, z):
    return x, y, -z

def doi_xung_qua_oxz(x, y, z):
    return x, -y, z

def doi_xung_qua_oyz(x, y, z):
    return -x, y, z

x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# Tính tọa độ của điểm đối xứng qua các mặt phẳng
doi_xung_oxy = doi_xung_qua_oxy(x, y, z)
doi_xung_oxz = doi_xung_qua_oxz(x, y, z)
doi_xung_oyz = doi_xung_qua_oyz(x, y, z)

print(f"Tọa độ của điểm đối xứng qua mặt phẳng OXY: {doi_xung_oxy}")
print(f"Tọa độ của điểm đối xứng qua mặt phẳng OXZ: {doi_xung_oxz}")
print(f"Tọa độ của điểm đối xứng qua mặt phẳng OYZ: {doi_xung_oyz}")
