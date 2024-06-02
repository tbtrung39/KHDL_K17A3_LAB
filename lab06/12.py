# Khởi tạo số tiền ban đầu là 0
balance = 0

# Nhập nhật ký giao dịch
transaction_log = input("Nhập nhật ký giao dịch (D/W số_tiền): ")

# Tách các giao dịch thành danh sách
transactions = transaction_log.split()

# Xử lý từng giao dịch
for i in range(0, len(transactions), 2):
    action = transactions[i]  # Lấy D hoặc W
    amount = int(transactions[i + 1])  # Lấy số tiền

    if action == "D":
        balance += amount
    elif action == "W":
        balance -= amount

# In số tiền thực hiện của tài khoản
print(f"Số tiền thực hiện của tài khoản là: {balance}")
