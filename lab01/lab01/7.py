x = float(input("Nhap mot so: "))
y = float(input("Nhap mot so: "))
z = float(input("Nhap mot so: "))
dx_oxy = [x,y,-z]
dx_oxz = [x, -y, z]
dz_oyz = [-x,y,z]
print("Doi xung qua Oxy la:",dx_oxy)
print("Doi xung qua Oxz la:", dx_oxz)
print("Doi xung qua Oyz la:",dz_oyz)