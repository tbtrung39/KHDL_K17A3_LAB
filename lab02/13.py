x = float(input("Nhập số lượng (gam) Al2O3: "))
y = float(input("Nhập nồng độ (M) của dung dịch NaOH: "))
z = float(input("Nhập nồng độ (M) của dung dịch HCl: "))
so_mol_NaOH = y * 0.1  
so_mol_HCl = z * 0.1
if so_mol_NaOH >= (2 * x / 102):  
    print("Không có kết tủa sau phản ứng.")
else:
    print("Có kết tủa sau phản ứng")