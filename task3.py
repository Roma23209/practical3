try:
    num1 = int(input('Enter a number 1: '))
    num2 = int(input('Enter a number 2: '))
    sum = num1 + num2
except ValueError:
    print('Введите корректные данные')
print(sum)