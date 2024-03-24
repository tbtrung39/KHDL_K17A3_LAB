quy_doi = {'A': 10, 'B': 12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20, 'K':21, 'L':23, 'M':24,'N':25, 'O': 26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31, 'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38}
n = input("nhập mã container n: ")
hsn = 1
gtri_ma = 0
for i in n[:4]:
     gtri_ma += quy_doi[i] * hsn
     hsn *= 2
for j in n[4:10]:
     gtri_ma += (int(j) * hsn)
     hsn *= 2
     gia_tri_cuoi = gtri_ma % 11
print("giá trị của của container là: ",gia_tri_cuoi)