n=int(input("Nhap vao mot so tu nhien a: "))
a = set()
b = set()
for i in range(1, n+1):
    if n%i == 0:
        nguyen_to = True
        for i in range(2, int(i**0.5)+1):
            if i & j == 0:
                nguyen_to = False
                break
            if nguyen_to:
                a.add(i)
            else:
                nguyen_to = True
                for j in range(2,int(i**0.5)+1):
                    if i% j == 0:
                        break
                    if nguyen_to:
                        b.add(i) 
                        print(f"Tap hop A: {a}")
                        print(f"Tap hop B: {b}")
                           