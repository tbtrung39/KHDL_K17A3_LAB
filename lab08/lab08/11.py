def bang_diem():
    ho_ten=input('nhập họ tên:')
    hoa=int(input('nhập điểm hoá:'))
    ly=int(input('nhập điểm lý:'))
    toan=int(input('nhập điểm toán:'))
    diem_tb=(hoa+ly+toan)/3
    print('điêm trung bình của sinh viên', ho_ten, 'là', diem_tb)
    return
bang_diem()

