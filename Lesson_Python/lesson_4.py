n = int(input("Введите целое положительное число: "))
max_number = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_number:
        max_number = n % 10
    else:
        print("Максимальное цифра в числе ", max_number)
        break
