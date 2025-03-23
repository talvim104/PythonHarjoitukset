talvi = (1, 2, 3)
kevat = (4, 5, 6)
kesa = (7, 8, 9)
syksy = (10, 11, 12)

kuukausinumero = int(input("Anna kuukausinumero (1-12): "))
if kuukausinumero in talvi:
    print("Se on talvi!")
elif kuukausinumero in kevat:
    print("Se on kevät!")
elif kuukausinumero in kesa:
    print("Se on kesä!")
elif kuukausinumero in syksy:
    print("Se on syksy!")