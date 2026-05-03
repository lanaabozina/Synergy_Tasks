n = int(input())
count = 0  # Переменная для подсчёта нулей

for i in range(n):
    n_integer = int(input())
    if n_integer == 0: # Проверка числа на равенство нулю
        count += 1     # Если число равно нулю, прибавляем 1 к счётчику

print(count)  # Вывод итогового количества после завершения цикла

# GitHub: https://github.com/lanaabozina/Synergy_Tasks