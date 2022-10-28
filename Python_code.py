from math import sqrt


def square_eq_solver(a, b, c):
    result = []
    discriminant = b * b - 4 * a * c

    if discriminant == 0:
        result.append(-b / (2 * a))
    elif discriminant > 0:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))
    return result


def show_result(result):
    if len(result) > 0:
        for index, value in enumerate(result):
            print(f'Корень номер {index+1} равен {value:.02f}')
    else:
        print('Уравнение с заданными параметрами не имеет корней')
    return result

def sum_digit_num(num):
    sum = 0
    num_1 = abs(float(num)) # если введено отрицательное число
    for i in str(num_1):
        if i != '.':
            sum += int(i) 
    return sum       
    
    
print(f'Сумма цифр числа -0.17856 равна {sum_digit_num(-0.17856)}')


