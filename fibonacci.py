def fibonacci(number):
    if number <= 1:
        # Если число меньше или равно 1, то возвращаем его.
        return number
    else:
        # Если число больше 1, то вычисляем сумму двух предыдущих чисел Фибоначчи.
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(3))
