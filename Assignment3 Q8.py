import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(random_numbers) / len(random_numbers)
print("Random numbers:", random_numbers)
print("Average:", average)