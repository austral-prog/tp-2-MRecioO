def change():
    expense = 23.75
    money = 100
    
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\n"+"Vuelto")
    print("\n" + "Pesos:")
    print(int(money - expense))
    print("Centavos:")
    print(int(((money - expense) % 1) *100))

change()
