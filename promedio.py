n1 = float (input("La primera nota es "))
n2 = float (input("La segunda nota es "))
n3 = float (input("La tersera nota es"))

prom = (n1+n2+n3)/3

if(prom>=3):
    print("El promedio es: ",prom,"Aprobo ")
else:    
    print("El promedio es: ",prom,"Reprobo")