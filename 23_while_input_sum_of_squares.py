'''Напишите программу, которая считывает с консоли числа (по одному в строке)
до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после
этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется
равной 0, после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент
замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов,
не обращая внимания на то, что остались ещё не прочитанные значения.'''
a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)