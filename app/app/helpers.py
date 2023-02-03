import random

from faker import Faker

fake = Faker()


def generate_person():
    name = fake.name()
    age = random.randint(4, 80)
    return {'name': name, 'age': age}


def generate_people():
    return [generate_person() for _ in range(100)]
