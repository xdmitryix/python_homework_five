# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵) -> 3*3*3*3*3
# A = 2; B = 3 -> 8



def degree(one, two):
    if two == 1:
        return one
    else:
        return one * degree(one, two-1)

a = int(input('введи число A: '))
b = int(input('введи число B: '))
result = degree(a,b)
print(result)