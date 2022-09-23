from faker import Faker

faker = Faker(['en-GB'])


def load_fake_clients(num):
    print("Feeding database with fake clients...\n")
    reset()
    rows.insert_clients(num)


def load_fake_cars(num):
    pass
