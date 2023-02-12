# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4

def sum(a, b, s):
    if a==0 and b==0:
        return s 
    else:
        if a>0 and b>0:
            s=s+1+1
            return sum(a-1,b-1,s)
        elif a>0 and b==0:
            s+=1
            return sum(a-1,b,s)
        elif a==0 and b>0:
            s+=1
            return sum(a, b-1,s)
a = int(input('введи число А:'))
b = int(input('введи число B:'))
summa = 0
result = sum(a,b,summa)
print(result)