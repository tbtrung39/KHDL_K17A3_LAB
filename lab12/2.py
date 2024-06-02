class InvalidCharacterError(Exception):
    pass
class RepeatedCharacterError(Exception):
    pass
class RepeatedFourTimesError(Exception):
    pass
class RepeatedWordsError(Exception):
    pass
def kiem_tra_loi_nhap_lieu (chuoi):
    if not all(c.isalpha() or c.isspace() for c in chuoi):
        raise InvalidCharacterError("loi ky tu!!!")
    for i in range(len (chuoi) -1):
        if chuoi [1] ==chuoi [i+1] and chuoi[1] != ' ':
            raise RepeatedCharacterError("Loi nhap lieu!!!")
    for i in range(len(chuoi) -3):
        if chuoi [1] ==chuoi [i+1] == chuoi[i+2] == chuoi [i+3] and chuoi [1] != ' ':
            raise RepeatedFourTimesError("Loi nhap lap lai!!!")
    tu=chuoi.split()
    if len(tu)>=5:
        for i in range(len(tu)-4):
            if tu[1]==tu[i+1]==tu[i+2]==tu[i+3]==tu[i+4]:
                raise RepeatedWordsError ("Loi nhap trung lap!!!")
def chay_chuong_trinh():
    while True:
            try:
                chuoi=input ("Nhap chuoi ky tu: ")
                kiem_tra_loi_nhap_lieu(chuoi)
                print ("Chuot hop le: ", chuoi) 
            except InvalidCharacterError as e:
                print (e)
            except RepeatedCharacterError as e:
                print (e)
            except RepeatedFourTimesError as e:
                print (e)
            except RepeatedWordsError as e:
                print (e)
chay_chuong_trinh()