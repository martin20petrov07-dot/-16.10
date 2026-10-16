a = float(input("Въведи първо число: "))
b = float(input("Въведи второ число: "))
deistvie = input("Избери действие (+,-, *, /):")
if deistvie == "+":
    print("Резултат: ", a+b)
elif deistvie == "-":
    print("Резултат: ", a-b)
elif deistvie == "*":
    print("Резултат: ", a*b)
elif deistvie == "/":
    if b == 0:
        print("Деление на нула е невъзможно!")
    print("Резултат: ", a/b)
else:
    print("Невалидно действие!!!!!!!!!!!!!!!!!!!!!!!!!")