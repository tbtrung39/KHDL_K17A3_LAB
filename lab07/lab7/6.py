n=int(input("Nhập số nuyên dương n: "))
nguyen_to={}
so_hien_tai=2
vi_tri=1
while len(nguyen_to)<n:
    la_so_nguyen_to=True
    for i in range(2, int(so_hien_tai**0.5)+1):
        if so_hien_tai%i==0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
            nguyen_to[vi_tri]=so_hien_tai
            vi_tri+=1
    so_hien_tai+=1
print("Đây", n, "số nguyên tố đầu tiên là:")
for vi_tri in nguyen_to:
    print(f"{vi_tri}:{nguyen_to[vi_tri]}")