chuỗi_đầu_vào = input("nhận chuỗi: ")
độ_dài_tối_đa = 0
chuỗi_con_tối_đa = ''
độ_dài_hiện_tại = 1
chuỗi_con_hiện_tại = chuỗi_đầu_vào[0]

for i in range(1, len(chuỗi_đầu_vào)):
    if chuỗi_đầu_vào[i] == chuỗi_đầu_vào[i-1]:
        độ_dài_hiện_tại += 1
        chuỗi_con_hiện_tại += chuỗi_đầu_vào[i]
    else:
        if độ_dài_hiện_tại > độ_dài_tối_đa:
            độ_dài_tối_đa = độ_dài_hiện_tại
            chuỗi_con_tối_đa = chuỗi_con_hiện_tại
        độ_dài_hiện_tại = 1
        chuỗi_con_hiện_tại = chuỗi_đầu_vào[i]

if độ_dài_hiện_tại > độ_dài_tối_đa:
    độ_dài_tối_đa = độ_dài_hiện_tại
    chuỗi_con_tối_đa = chuỗi_con_hiện_tại

print(chuỗi_con_tối_đa)
