chu_ngu=["Anh", "Em"]
dong_tu=["Chơi", "Yêu"]
tan_ngu=["Bóng đá", "Bóng rổ"]
câu=[(subj, verb, obj) for subj in chu_ngu for verb in dong_tu for obj in tan_ngu]
for subj, verb, obj in câu:
    print(f"{subj} {verb} {obj}")