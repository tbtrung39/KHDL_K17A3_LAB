chu_ngu = ["Anh","Em"]
dong_tu = ["Chơi","Yêu"]
tan_ngu = ["Bóng đá","Bóng rổ"]
cau = []
for cngu in chu_ngu:
    for dtu in dong_tu:
        for tngu in tan_ngu:
            cau.append(cngu + " " + dtu + " " + tngu)

# In ra tất cả các câu đã tạo
for caus in cau:
    print(caus)