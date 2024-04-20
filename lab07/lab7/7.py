def main():
    A = set(input("Nhập các phần tử cho tập hợp A, cách nhau bởi dấu cách: ").split())
    B = set(input("Nhập các phần tử cho tập hợp B, cách nhau bởi dấu cách: ").split())
    
    print("Tập hợp A: ", A)
    print("Tập hợp B: ", B)
    print("Các phần tử chung của A và B: ", A & B)

if __name__ == "__main__":
    main()
