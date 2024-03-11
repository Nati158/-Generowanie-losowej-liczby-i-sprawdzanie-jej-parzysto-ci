import random

def czy_parzysta(liczba):
    return liczba % 2 == 0

losowa_liczba = random.randint(1, 10)
print("Wylosowana liczba:", losowa_liczba)

if czy_parzysta(losowa_liczba):
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")
