A = set()

print("Nhập các giá trị cho tập hợp A. Nhập 'done' khi hoàn thành.")
while True:
    entry = input("Nhập giá trị (số nguyên, số thực, hoặc chuỗi): ")
    if entry.lower() == 'done':
        break
    # Xử lý số nguyên và số thực
    try:
        # Cố gắng chuyển đổi giá trị nhập vào thành số thực
        float_val = float(entry)
        # Kiểm tra xem có phải là số nguyên bằng cách so sánh với phiên bản int của chính nó
        if float_val == int(float_val):
            # Thêm như số nguyên
            A.add(int(float_val))
        else:
            # Thêm như số thực
            A.add(float_val)
    except ValueError:
        # Nếu không phải số, xử lý như chuỗi
        A.add(entry)

print("Tập hợp A:", A)
