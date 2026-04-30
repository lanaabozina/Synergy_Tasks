word = input("Пожалуйста, введите слово из латинских букв: ").lower()

# Определяю списки букв
vowels_list = ['a', 'e', 'i', 'o', 'u']
consonants_list = 'bcdfghjklmnpqrstvwxyz'

vowels_count = 0
consonants_count = 0

# Словарь для подсчёта каждой гласной
vowels_stats = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in vowels_list:
        vowels_count += 1
        vowels_stats[letter] += 1
    elif letter in consonants_list:
        consonants_count += 1

# Вывод общих результатов
print(f"Гласных букв: {vowels_count}")
print(f"Согласных букв: {consonants_count}")

# Вывод статистики по каждой гласной
for v in vowels_list:
    if vowels_stats[v] > 0:
        print(f"Буква '{v}': {vowels_stats[v]}")
    else:
        print(f"Буква '{v}': False")

# GitHub: https://github.com/lanaabozina/Synergy_Tasks