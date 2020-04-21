from faker import Faker

fake = Faker(['it_IT', 'en_US', 'ja_JP'])

for _ in range(100):
    print(f'name: {fake.name()}')
    print(f'address: {fake.email()}')