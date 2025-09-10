import random
number = random.randint(-10, 10)
codigo = number
if codigo > 0:
    print("is positive")
elif codigo == 0:
    print("is zero")
else:
    print("is negative")