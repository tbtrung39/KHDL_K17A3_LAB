with open("dayso.dat",mode='r') as file:
    nums = [int(line) for line in file]
    sum = 0
    for num in nums:
        if num % 2 !=0:
            sum += num

print(sum, "là tổng số lẻ trong file")
   


