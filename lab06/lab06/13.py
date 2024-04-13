chu_ngu = ["anh", "em"]
dong_tu = ["chơi", "yêu"]
tan_ngu = ["bóng đá", "bóng rổ"]
cac_cau = [(ch, dt, tn) for ch in chu_ngu for dt in dong_tu for tn in tan_ngu]
for cau in cac_cau:
    print(f"{cau[0]} {cau[1]} {cau[2]}.")
