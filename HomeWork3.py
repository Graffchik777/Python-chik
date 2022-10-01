Digit = int(input("Водим циферку:  "))
if (Digit%5 == 0 or Digit%10 == 0 or Digit%15 == 0) and Digit%30 != 0:
    print("Получилось!!!!")
else:
    print("Не-а")    