x = float(input("Nhập số lượng (gam) Al2O3: "))
y = float(input("Nhập nồng độ (M) của dung dịch NaOH: "))
z = float(input("Nhập nồng độ (M) của dung dịch HCl: "))
mol_Al2O3 = x / 101.96  # Al2O3 có khối lượng mol là 101.96 g/mol
vol_NaOH = 100 / 1000  # Chuyển ml thành lít
mol_NaOH = y * vol_NaOH
vol_HCl = 100 / 1000  # Chuyển ml thành lít
mol_HCl = z * vol_HCl
mol_NaAlO2 = min(mol_Al2O3 / 1, mol_NaOH / 2) * 2
mol_NaOH -= mol_NaAlO2 * 2
mol_AlOH3 = min(mol_NaAlO2 / 1, mol_HCl / 2) * 1
mol_NaAlO2 -= mol_AlOH3 * 1
mol_HCl -= mol_AlOH3 * 2
vol_total = vol_NaOH + vol_HCl
mol_Al3_plus = mol_AlOH3 / vol_total
mol_OH_minus = mol_NaOH / vol_total
if mol_Al3_plus > 0 and mol_OH_minus > 0:
    print("Sau phản ứng có kết tủa Al(OH)3.")
else:
    print("Sau phản ứng không có kết tủa Al(OH)3.")