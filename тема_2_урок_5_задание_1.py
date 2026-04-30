n = int(input("Пожалуйста, введите целое число: "))

if n == 0:
    print("Нулевое число")
elif n % 2 != 0:
    print("Число не является чётным")
else:
    # Если мы здесь, значит, число чётное и не ноль
    if n > 0:
        print("Положительное чётное число")
    else:
        print("Отрицательное чётное число")

# GitHub: https://github.com/lanaabozina/Synergy_Tasks