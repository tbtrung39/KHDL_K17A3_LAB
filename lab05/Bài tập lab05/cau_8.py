Str = input("Nhập chuỗi ký tự: ")
do_dai_max = 1
index = 0
do_dai = 1

for i in range(1, len(Str)):
    if Str[i] == Str[i - 1]:
        do_dai += 1
    else:
        if do_dai > do_dai_max:
            do_dai_max = do_dai
            index = i - do_dai_max
        do_dai = 1

if do_dai > do_dai_max:
    do_dai_max = do_dai
    index = len(Str) - do_dai_max

chuoi_con = Str[index:index + do_dai_max]
print("Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau: ", chuoi_con)
