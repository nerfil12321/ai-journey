# Умный калькулятор
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Выберите операцию из предложенных: + - * / : ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя')
    else:
        print(a / b)
else:
    print('Неизвестная операция')