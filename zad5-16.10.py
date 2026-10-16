day = int(input("Въведете номер на ден:"))
if day == 1:
    print(f"Ден {day} e Понеделник")
elif day == 2:
    print(f"Ден {day} e Вторник")
elif day == 3:
    print(f"Ден {day} e Сряда")
elif day == 4:
    print(f"Ден {day} e Четвъртък")
elif day == 5:
    print(f"Ден {day} e Петък")
elif day == 6:
    print(f"Ден {day} e Събота")
elif day == 7:
    print(f"Ден {day} e Неделя")
else:
    print(f"Невалиден номер: {day}")