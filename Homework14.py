# Задача №32: Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input(f"Создайте список через пробел: \n").split()))
def unical_old(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(unical_old(numbers))