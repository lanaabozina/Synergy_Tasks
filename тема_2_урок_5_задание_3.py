x = int(input()) # Минимальная сумма
a = int(input()) # Деньги Майкла
b = int(input()) # Деньги Ивана

if (a >= x) and (b >= x):
    print(2)
elif (a >= x):
    print("Mike")
elif (b >= x):
    print("Ivan")
elif (a + b >= x):
    print(1)
else:
    print(0)

# GitHub: https://github.com/lanaabozina/Synergy_Tasks