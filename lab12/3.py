import os
def doc_noi_dung_tap_tin(ten_tap_tin):
    with open(ten_tap_tin, 'r') as file:
        noi_dung = file.read()
    return noi_dung
def ghi_noi_dung_vao_tap_tin(ten_tap_tin, noi_dung):
    with open(ten_tap_tin, 'w') as file:
        file.write(noi_dung)
def main():
    ten_tap_tin = input("Nhập tên tập tin cần đọc: ")
    if not os.path.isfile(ten_tap_tin):
        print("Lỗi: Không có tập tin nào giống với tên vừa nhập.")
        return
    try:
        noi_dung = doc_noi_dung_tap_tin(ten_tap_tin)
        ghi_noi_dung_vao_tap_tin('copy.dat', noi_dung)
        print(f"Nội dung của tập tin {ten_tap_tin} đã được sao chép vào tập tin copy.dat.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc hoặc ghi tập tin: {e}")
if __name__ == "__main__":
    main()
