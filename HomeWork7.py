# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.



# print("Забей координатки точек А:  ")
# x1 = int(input("Первый X: "))
# y1 = int(input("Первый Y: "))
# print("Введи координаты точек B:")
# x2 = int(input("Второй X: "))
# y2 = int(input("Второй Y: "))

# from math import sqrt
# print("Расстояние определяем по теореме Пифагорыча =",round(sqrt((x1 - x2)**2 + (y1 - y2)**2),2)) 

# Number = int(input('Введите число N: '))

# result = {}
# for key in range(1, Number+1):
#     result[key] = key*3 +1

# print(result)


n = int(input("Введите n: "))

lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')
