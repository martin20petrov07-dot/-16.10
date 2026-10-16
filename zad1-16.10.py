n = int(input("Въведи брой числа n: "))
max_num = int(input("Въведи число: "))
for n in range(n-1):
  num = int(input("Въведи число: "))
  if num > max_num:
   max_num = num
print ("Най-голямото число е:", max_num)