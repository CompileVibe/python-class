import math

print(f"pi = {math.pi}")
print(f"e = {math.e}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"pow(2, 10) = {math.pow(2, 10)}")
print(f"ceil(4.3) = {math.ceil(4.3)}")
print(f"floor(4.7) = {math.floor(4.7)}")

import random

random.seed(42)
print(f"random() = {random.random()}")
print(f"randint(1, 10) = {random.randint(1, 10)}")
print(f"choice(['a', 'b', 'c']) = {random.choice(['a', 'b', 'c'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"shuffled = {numbers}")

from datetime import datetime, timedelta

now = datetime.now()
print(f"Now: {now}")

launch = datetime(2026, 10, 3, 12, 0, 0)
print(f"Launch: {launch}")

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
