chieu_cao = [161,182,161,154,176,170,167,171,170,174,150,1422,148,165,178,178,
             156,145,149,163,162,159,165,170,180,155,159,155,153,152,162,180,168,169,168,167,178]

so_hs = len(chieu_cao)
print("so luong hoc sinh la:", so_hs)
chieu_cao_tb = sum(chieu_cao) / so_hs
print("chieu cao trung bình la:", chieu_cao_tb )
chieu_cao_khac = set(chieu_cao)
print("chieu cao khac nhau la:", chieu_cao_khac) 
chieu_cao_tb_khac = sum(chieu_cao_khac) / so_hs
print("chieu cao trung bình khac nhau la:", chieu_cao_tb_khac)