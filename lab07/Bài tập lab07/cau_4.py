chieu_cao =  [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
print("Số sinh viên là: ", len(chieu_cao))
chieu_cao_tb = sum(chieu_cao)/len(chieu_cao)
chieu_cao_khac = set(chieu_cao)
print("Các chiều cao khác nhau của sinh viên tring nhóm là: ", chieu_cao_khac)
print("Chiều cao trung bình của nhóm là: ", chieu_cao_tb)
