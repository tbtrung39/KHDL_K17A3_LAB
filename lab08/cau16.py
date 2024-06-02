def even_numbers():
    even_nums = []
    for i in range(1,101):
        if i % 2 ==0:
            even_nums.append(i)
    return even_nums
find_even_nums = even_numbers()
print(find_even_nums)