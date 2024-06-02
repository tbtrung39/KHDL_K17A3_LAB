def sum_of_n_numbers(n):
    try:
        if n <= 0:
            raise ValueError("n phải là một số dương")
        s1 = sum(range(1, n + 1))
        s2 = sum([i**2 for i in range(1, n + 1)])
        print("Tổng của {} số là: {}".format(n, s1))
        print("Tổng của bình phương của {} số là: {}".format(n, s2))
    except ValueError:
        print("Lỗi: n phải là một số dương")
    except Exception as e:
        print("Lỗi không mong muốn: ", e)