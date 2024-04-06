input_str = input("Nhập chuỗi ký tự: ")
do_dai_cd = 0  
chuoi_cd = ''  
do_dai_ht = 1 
chuoi_ht = input_str[0]
for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]:
        do_dai_ht += 1
        chuoi_ht += input_str[i]
    else:
        if do_dai_ht > do_dai_cd:
            do_dai_cd = do_dai_ht
            chuoi_cd = chuoi_ht
        do_dai_ht = 1
        chuoi_ht = input_str[i]
if do_dai_ht > do_dai_cd:
    do_dai_cd = do_dai_ht
    chuoi_cd = chuoi_ht
print(f"Chuỗi ký tự con có độ dài cực đại và chứa các phần tử giống nhau: {chuoi_cd}")
