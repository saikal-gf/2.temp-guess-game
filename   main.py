import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Генератор случайных паролей")
length = input("Введите длину пароля (по умолчанию 12): ")

if length.isdigit() and int(length) > 0:
    length = int(length)
else:
    length = 12

password = generate_password(length)
print(f"Ваш новый пароль: {password}")
