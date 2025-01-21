leiviska = 13.3 * 32 * 20
naula = 13.3 * 32
luoti = 13.3
leiviskat = float(input("Anna leiviskät: \n"))
naulat = float(input("Anna naulat: \n"))
luodit = float(input("Anna luodit: \n"))

massa_1 = leiviska * leiviskat + naula * naulat + luoti * luodit
massa_2 = int(massa_1 // 1000)
massa_3 = (massa_1 % 1000)
print("Massa nykymittojen mukaan: ")
print(massa_2, "kilogrammaa",f"{massa_3:10.2f}", "grammaa")

