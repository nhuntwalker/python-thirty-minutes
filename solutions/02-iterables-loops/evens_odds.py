"""Generates a dictionary of even and odd numbers."""
import random

numbers = {
    "evens": set(),
    "odds": set()
}

for _ in range(100):
    new_number = random.randint(0, 50)
    if new_number % 2 == 0:
        numbers["evens"].add(new_number)
    else:
        numbers["odds"].add(new_number)

print(numbers)