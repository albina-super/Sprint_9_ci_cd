from faker import Faker
import random

fake = Faker('ru_RU')  # Генерация русскоязычных данных


def generate_registration_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}"
    email = f"{username}@{fake.free_email_domain()}"
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email_address": email,
        "password": password
    }
