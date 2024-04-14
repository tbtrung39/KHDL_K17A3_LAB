chu_ngu = ['anh','em']
dong_tu = ['choi','yeu']
tan_ngu = ['bong da','bong ro']
cau_hoi = [f"{cn} {dt} {tn}" for cn in chu_ngu for dt in dong_tu for tn in tan_ngu]
print(cau_hoi)