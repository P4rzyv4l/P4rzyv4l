opcion = 0
while True:
    print("""
    Dime,¿que quieres hacer?
    1 = Sumar los numeros
    2 = Restar los numeros
    3 = multiplicar los numeros 
    4 = Sacar promedio
    5 = Apagar calculadora
    """)
    opcion = int(input("eliga una opciòn: "))

    if opcion == 1:
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        print("")
        print("Resultado: La suma de ", n1, "+", n2, "Es igual a: ", n1+n2)

    elif opcion == 2:
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        print("")
        print("Resultado: La resta de ", n1, "-", n2, "Es igual a: ", n1-n2)

    elif opcion == 3:
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        print("")
        print("Resultado: La multiplicaciòn de ",n1, "*", n2, "es igual a:",n1*n2)

    elif opcion == 4:
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        n3 = float(input("Ingrese el tercer numero: "))
        div = (n1+n2+n3)/3
        if div>6:
            print("Aprovaste con una exelente nota tu promedio es: ",div)
        elif div>4:
            print ("Aprovaste apenas con un promedio de: ",div)
        else:
            print("Reprobo con un promedio de: ",div) 
    elif opcion ==5:
        print("Adios")
        break
    else:
        print("Opciòn incorrecta")