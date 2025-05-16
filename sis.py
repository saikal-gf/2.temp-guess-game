def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("🌡️ Конвертер температуры")
choice = input("Введите 'C' чтобы перевести из Цельсия в Фаренгейт, или 'F' — наоборот: ").upper()

if choice == 'C':
    temp_c = input("Введите температуру в градусах Цельсия: ")
    if temp_c.replace('.', '', 1).isdigit():
        temp_c = float(temp_c)
        temp_f = celsius_to_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.2f}°F")
    else:
        print("❌ Введите корректное число.")
elif choice == 'F':
    temp_f = input("Введите температуру в градусах Фаренгейта: ")
    if temp_f.replace('.', '', 1).isdigit():
        temp_f = float(temp_f)
        temp_c = fahrenheit_to_celsius(temp_f)
        print(f"{temp_f}°F = {temp_c:.2f}°C")
    else:
        print("❌ Введите корректное число.")
else:
    print("❌ Выберите либо 'C', либо 'F'.")
