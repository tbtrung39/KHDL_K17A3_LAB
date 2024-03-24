num = int(input("nhập vào 1 số(n>0): "))
doc=""
if num<0:
    print("nhập lại số")
    num = int(input("nhập vào 1 số(n>0): "))
else:
    if num==1:
        doc+="một"
    if num==0:
        doc+="không"
    if num==2:
        doc+="hai"
    if num==3:
        doc+="ba"
    if num==4:
        doc+="bốn"
    if num==5:
        doc+="năm"
    if num==6:
        doc+="sáu"
    if num==7:
        doc+="bảy"
    if num==8:
        doc+="tám"
    if num==9:
        doc+="chín"

print(doc)
