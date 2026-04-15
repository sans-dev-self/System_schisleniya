num = int(input("Введите число: "))
n = int(input("В какую систему: "))

result = ""
while num > 0:
    rem = num % n
    if 10 <= rem <= 16:
        result += chr(55 + rem)
    else:
        result += str(rem)
    num //= n
print(result[::-1])
#