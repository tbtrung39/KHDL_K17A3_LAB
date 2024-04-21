chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149,
             163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
tong_sinh_vien = len(chieu_cao)
print("Số sinh viên của nhóm là:",tong_sinh_vien)
chieu_cao_trung_binh = (sum(chieu_cao) / tong_sinh_vien)
print("Chiều cao trung bình của các sinh viên trong nhóm là:",chieu_cao_trung_binh)
print("Các chiều cao khác nhau của sinh viên trong nhóm là:")
print(set(chieu_cao))
trung_binh = (sum(set(chieu_cao))/len(set(chieu_cao)))
print("Chiều cao trung bình của nhóm là:",trung_binh)
