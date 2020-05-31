from Clases import Converciones

menu=int(input("Quieres entrar al Menu Principal\n1=SI\n2=NO\n:"))
while menu==1:
    print("*"*20+"Menu Principal"+"*"*20)
    print("1=Quiero de Pesos Mexicanos convertirlo a otro tipo de Moneda")
    print("2=Quiero de Dolares EstadoUnidenses convertirlo a otro tipo de Moneda")
    print("3=Quiero de Euros convertirlo a otro tipo de Moneda")
    submenu=int(input(":"))
    if submenu==1:
        print("1=De pesos Mexicanos a Dolares de Estados Unidos")
        print("2=De pesos Mexicanos a Euros")
        opcion=int(input("Que opciones eliges:"))
        if opcion==1:
            opcionx=1
            contador=0
            while opcionx==1:
                cantidad=int(input("Dime la cantidad en pesos Mexicanos a convertir:"))
                D=Converciones(cantidad)
                print(D.PesosAdolares())
                contador=contador+D.PesosAdolares()
                opcionx=int(input("Deseas seguir conviertiendo pesos a dolares\n1=SI\n2=NO\n:"))
                if opcionx!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Pesos convertidos a Dolares:${contador} Dolares")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)
        
        elif opcion==2:
            opcionx=1
            contador1=0
            while opcionx==1:
                cantidad=int(input("Dime la cantidad en pesos Mexicanos a convertir:"))
                E=Converciones(cantidad)
                print(E.PesosAEuros())
                contador1=contador1+E.PesosAEuros()
                opcionx=int(input("Deseas seguir conviertiendo pesos a Euros\n1=SI\n2=NO\n:"))
                if opcionx!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Pesos convertidos a Euros:€{contador1} Euros")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)
            
                
    
    elif submenu==2:
        print("1=De Dolares a Pesos Mexicanos")
        print("2=De Dolares a Euros")
        opcion=int(input("Que opciones eliges:"))
        opcionz=1
        contador2=0
        if opcion==1:
            opcionz=1
            contador2=0
            while opcionz==1:
                cantidad=int(input("Dime la cantidad de Dolares deseas convertir:"))
                P=Converciones(cantidad)
                print(P.DolarAPesos())
                contador2=contador2+P.DolarAPesos()
                opcionz=int(input("Deseas seguir conviertiendo Dolares a Pesos\n1=SI\n2=NO\n:"))
                if opcionz!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Dolares convertidos a Pesos:${contador2} Pesos")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)
                    
        elif opcion==2:
            opcionw=1
            contador3=1
            while opcionw==1:
                cantidad=int(input("Dime la cantidad de Dolares deseas convertir:"))
                Eu=Converciones(cantidad)
                print(Eu.DolarAEuros())
                contador3=contador3+Eu.DolarAEuros()
                opcionw=int(input("Deseas seguir conviertiendo Dolares a Euros\n1=SI\n2=NO\n:"))
                if opcionw!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Dolares convertidos a Euros:€{contador3} Euros")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)


    elif submenu==3:
        print("1=De Euros a Pesos Mexicanos")
        print("2=De Euros a Dolares")
        opcion=int(input("Que opciones eliges:"))
        opcionxv=1
        contador4=0
        if opcion==1:
            while opcionxv==1:
                cantidad=int(input("Dime la cantidad de Euros deseas convertir:"))
                E=Converciones(cantidad)
                print(E.EurosAPesos())
                contador4=contador4+E.EurosAPesos()
                opcionxv=int(input("Deseas seguir conviertiendo Euros a Pesos\n1=SI\n2=NO\n:"))
                if opcionxv!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Euros convertidos a Pesos:${contador4} Pesos")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)
        
        elif opcion==2:
            opcionxx=1
            contador5=0
            while opcionxx==1:
                cantidad=int(input("Dime la cantidad de Euros deseas convertir:"))
                Ed=Converciones(cantidad)
                print(Ed.EurosADolar())
                contador5=contador5+Ed.EurosADolar()
                opcionxx=int(input("Deseas seguir conviertiendo Euros a Dolares\n1=SI\n2=NO\n:"))

                if opcionxx!=1:
                    print("*"*100)
                    print(f"Esta es la suma de tus Euros convertidos a Dolares:${contador5} Dolares")
                    menu=int(input("Deseas seguir con el Programa\n1=SI\n2=NO\n:"))
                    print("*"*100)





