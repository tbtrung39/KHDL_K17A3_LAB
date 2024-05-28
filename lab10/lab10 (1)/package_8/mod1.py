def nhap_du_lieu(n):
    a = []
    print("nhap du lieu vao ma tran ")
    for i in range(n):
        hang=[]
        for j in range(n):
            e = int(input(f"nhap pha tu 0 hang thu {i + 1} cot thu {j+1}:"))
            hang.append(e)
        a.append(hang)
    return a 
def in_matrix(a):
    for i in a:
        for j in i:
            print(j , end = " ")
        print()
def ma_tran_chuuyen_vi(a):
    b = [[row[i] for row in a ] for i in range (len(a[0]))]
    print("ma tran chuyen vi la:")
    for i in b:
        for j in i:
            print( j , end = "")
            print()
            return b 
def kiem_tra_doi_xung(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != a[j][i]:
                return False
    return True