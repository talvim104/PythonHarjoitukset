import random
koodi = random.randint(100, 999)
print("Kolmenumeroinen koodi:", koodi)

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
num4 = random.randint(1, 6)
print("Neljänumeroinen koodi:" + str(num1) + str(num2) + str(num3) + str(num4))

koodi_2 = random.sample("123456",4)
print("Neljänumeroinen koodi:", koodi_2)
