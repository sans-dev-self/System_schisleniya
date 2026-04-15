num = input("Введите число: ")
n = int(input("Введите систему счисления: "))

num = num[::-1]
len_num = len(num) - 1
result = 0

for i in range(len_num,-1,-1):
    char = num[i]

    if char.isdigit():
        result += int(char) * n**i
    elif char.isalpha():
        result += (ord(char) - 55) * n**i
print(result)