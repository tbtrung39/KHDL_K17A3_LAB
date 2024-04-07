hang_so = {
    "0": "không",
    "1": "một",
    "2": "hai",
    "3": "ba",
    "4": "bốn",
    "5": "năm",
    "6": "sáu",
    "7": "bảy",
    "8": "tám",
    "9": "chín"
}

so = input("Nhập số nguyên dương từ bàn phím: ")

# In ra số bằng chữ
ket_qua = ""
i = 0
while i < len(so):
    chu_so = so[i]
    ket_qua += hang_so[chu_so] + " "
    i += 1

print("Kết quả:", ket_qua)