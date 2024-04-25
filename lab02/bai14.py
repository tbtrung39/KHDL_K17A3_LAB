x = float(input("nhập x :"))
y = float(input("nhập y :"))
z = float(input("nhập z :"))
so_mol_naoh = y * 0.1
so_mol_hcl = z * 0.1
so_mol_al2o3 = x / 102
so_mol_naalo2 = 2 * so_mol_al2o3

if so_mol_al2o3 > so_mol_naoh :
    print("có kết tủa xuất hiện(al2o3 dư).")
elif so_mol_naoh == so_mol_hcl :
    print("có kết tủa xuất hiện(aloh3 xuất hiện).")
elif so_mol_al2o3 < so_mol_naoh :
    print("không có kết tủa xuất hiện.")
elif so_mol_hcl > so_mol_naoh :
    print("không có kết tủa xuất hiện.")
elif so_mol_naoh > so_mol_hcl :
    print("không có kết tủa xuất hiện.")
elif so_mol_al2o3 == so_mol_naoh :
    print("không có kết tủa xuất hiện.")

























elif so_mol_al2o3 < so_mol_naoh :
    print("không có kết tủa xuất hiện(hòa tan al2o3).")
elif so_mol_al2o3 == so_mol_naoh :
    print("không có kết tủa xuất hiện(hết al2o3).") 
          
                      









 