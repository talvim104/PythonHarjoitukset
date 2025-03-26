sukupuoli = input("Mikä on sinun biologinen sukupuolesi: ")
hem = int(input("Anna hemoglobiinitasosi: "))
if sukupuoli == "nainen" and 117 <= hem <= 175:
    print("Sinulla on normaali hemoglobiinitaso!")
elif (sukupuoli == "nainen" and 117 > hem):
    print("Sinulla on alhainen hemoglobiinitaso!")
elif sukupuoli == "nainen" and 175 < hem:
    print("Sinulla on korkea hemoglobiinitaso!")
if sukupuoli == "mies" and 134 <= hem <= 195:
    print("Sinulla on normaali hemoglobiinitaso!")
elif sukupuoli == "mies" and 134 > hem:
    print("Sinulla on alhainen hemoglobiinitaso!")
elif sukupuoli == "mies" and 195 < hem:
    print("Sinulla on korkea hemoglobiinitaso!")

