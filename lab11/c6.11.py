# Câu a
with open("filename.txt", "r") as file:
    first_line = file.readline()
    third_line = file.readline()
    print(first_line)
    print(third_line)
#Câu b
with open("filename.txt", "r") as file:
    content = file.readlines()
    print(content)
#Câu c
with open("filename.txt", "r") as file:
    odd_numbers = [int(line) for line in file if line.isodd()]
    with open("ODD.txt", "w") as file:
        for i in range(4):
            for j in range(4):
                if i == 0 and j == 0:
                    file.write(" ")
                else:
                    file.write(" " + str(odd_numbers[i][j]))
#Câu d
with open("ODD.txt", "r") as file:
    last_line = file.readline()
    print(last_line)