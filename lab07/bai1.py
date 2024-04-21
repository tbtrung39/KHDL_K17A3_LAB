import keyboard
print("Nhập vào một kí tự (Kết thúc bằng phím ESC): ")
tap_hop = set()
try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nPhát hiện nhấn Ctrl, chương trình kết thúc.")
            break
        else:
            ki_tu = keyboard.read_key()
            tap_hop.add(ki_tu)

except KeyboardInterrupt:
    print("\nBạn đã nhấn ESC, chương trình kết thúc.")
print("Tập hợp ban đầu là:",tap_hop)  
for i in list(tap_hop):
    if i.isdigit():
        tap_hop.remove(i)
print("Tập hợp sau khi xóa các phần tử số là:",tap_hop)     