min_val = float(input("Въведи долна граница: "))
max_val = float(input("Въведи горна граница: "))
count = 0
print("Въведи 10 числа:")
for i in range(1,11):
    num=float(input("Въведи число:"))
    if min_val < num < max_val:
        count +=1
print(f"Броя на числата в границата е: {count}")