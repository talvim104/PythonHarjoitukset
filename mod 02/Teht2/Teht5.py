leiviska = 13.3 * 32 * 20
naula = 13.3 * 32
luoti = 13.3
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

massa_1 = leiviska * leiviskat + naula * naulat + luoti * luodit
massa_2 = int(massa_1 // 1000)
massa_3 = round(massa_1 % 1000, 2)
print("Massa nykymittojen mukaan: ")
print(massa_2, "kilogrammaa", massa_3, "grammaa")