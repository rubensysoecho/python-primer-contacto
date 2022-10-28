fin = False

while fin == False:
    print("\nLISTA DE EJERCICIOS")
    print("1.- Suma de dos números")
    print("2.- Resta de dos números")
    print("3.- Multiplicación de dos números")
    print("4.- División de dos números")
    print("5.- Resto de dos números")
    print("6.- Longitud de cadena introducida en pantalla")
    print("7.- Área de triángulo introduciendo base y altura")
    print("8.- Perímetro de circunferencia introduciendo radio")
    print("9.- Conversión de pesetas a euros")
    print("10.- Valor de polinomio")
    print("11.- Salario neto introduciendo salario bruto")
    print("12.- Volumen de cilindro introduciendo altura y radio")
    print("13.- Volumen de esfera introduciendo radio")
    print("Pulse cualquier botón para salir.")
    
    ej_seleccionado = input("\nEjercicio a ejecutar: ")
    
    if ej_seleccionado == "1":
        print("Número 1: ", end="")
        num1 = input()
        print("Número 2: ", end="")
        num2 = input()
        resultado = float(num1) + float(num2)
        print("Suma --> ", resultado)
        
    elif ej_seleccionado == "2":
        num1 = input("Número 1: ")
        num2 = input("Número 2: ")
        print("Resta --> ",(float(num1) - float(num2)))
        
    elif ej_seleccionado == "3":
        num1 = input("Número 1: ")
        num2 = input("Número 2: ")
        print("Producto --> ", float(num1) * float(num2))
        
    elif ej_seleccionado == "4":
        num1 = input("Número 1: ")
        num2 = input("Número 2: ")
        print("División --> ", float(num1) / float(num2))
        
    elif ej_seleccionado == "5":
        num1 = input("Número 1: ")
        num2 = input("Número 2: ")
        print("Resta --> ", float(num1) % float(num2))
        
    elif ej_seleccionado == "6":
        cadena = input("Cadena: ")
        print("Longitud de cadena --> ", len(cadena))
        
    elif ej_seleccionado == "7":
        base = input("Base del triángulo: ")
        base = float(base)
        altura = input("Altura del triángulo: ")
        altura = float(altura)
        area = (base * altura) / 2
        print("El área es de ", area," cm")
        
    elif ej_seleccionado == "8":
        pi = 3.1416
        radio = input("Radio de la circunferencia: ")
        perimetro = 2 * pi * float(radio)
        print("Perímetro --> ", perimetro)
        
    elif ej_seleccionado == "9":
        pesetas = input("Introduzca cantidad en pesetas: ")
        pesetas = float(pesetas)
        euros = pesetas / 166.386
        print(pesetas, " pesetas ==> ", round(euros, 2), " euros")
        
    elif ej_seleccionado == "10":
        x = input("Introduzca el valor de X: ")
        x = float(x)
        resultado = 2*(x*x) + 5*x-3
        print("2*x2+5*x-3 = ", resultado)
        
    elif ej_seleccionado == "11":
        salarioBruto = input("Salario bruto: ")
        salarioBruto = float(salarioBruto)
        irpf = 12/100
        salarioNeto = salarioBruto - (salarioBruto * irpf)
        print("Salario neto --> ", salarioNeto)
        
    elif ej_seleccionado == "12":
        altura = input("Introducza la altura, en metros: ")
        altura = float(altura)
        radio = input("Introduzca el radio, en metros: ")
        radio = float(radio)
        pi = 3.1416
        volumen = pi * (radio**2) * altura
        print("El volumen del cilindro es de ", round(volumen, 2), " metros cúbicos")
        
    elif ej_seleccionado == "13":
        pi = 3.1416
        radio = input("Radio de la esfera: ")
        radio = float(radio)
        volumen = (4 * pi * (radio**3)) / 3
        print("Volumen de la esfera: ", volumen)
        
    else:
        fin = True
        
print("PROGRAMA FINALIZADO")