s = input().lower()
if s == s[::-1]: # срез (slice). В Python срезы записываются так: [начало:конец:шаг]. Шаг -1 означает, что нужно идти от конца к началу. Стандартный срез (идём вперёд) s[::1]
    print("yes")
else:
    print("no")

# GitHub: https://github.com/lanaabozina/Synergy_Tasks