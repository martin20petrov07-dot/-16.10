n = int(input("Въведи брой числа n: "))
suma = 0
for _ in range(n):
    num = int(input("Въведи число: "))
    suma = suma + num
print("Сумата на числата е:", suma)