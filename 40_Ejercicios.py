from fractions import Fraction
import os,random,time
from funciones_Vielko import mostrar_menu,chatVPT,pant_carga,mostrar_calc,formato_moneda

def pausar():
    input("\n⏸️  Presiona enter para continuar...")

salir = False
ejercicios_cargador = False
while not salir: #Bucle de ejecución principal
    os.system("cls")
    respuesta = mostrar_menu("Ejercicios 1 al 10",
                            "Ejercicios 11 al 20",
                            "Ejercicios 21 al 30",
                            "Ejercicios 31 al 40",
                            "salir")

    match respuesta:#MENÚ PRINCIPAL
        
        case 1:#Ejercicios 1 al 10
            
            pant_carga("cargando ejercicios",tiempo=2.5)

            while True:#Bucle de ejercicios del 1 al 10
                os.system("cls")
                ejercicio = mostrar_menu(" 👋  Saludo personalizado",
                                        " 🛣️   Convertir kilometros a millas",
                                        " 🔢  Numero par o impar",
                                        " 📐  Calcular area de un triangulo",
                                        " ✖️   Tabla de multiplicar",
                                        " 2️⃣   Suma de numeros pares del 1 al 100",
                                        " 🔮  Adivina el número",
                                        " 📈  Promedio de números",
                                        " 🔠  Conteo de palabras",
                                        "🧮  Ordenar números",
                                        "↩️   Volver al menú principal",
                                        nombreMenu="Ejercicios 1 al 10")
                
                match ejercicio:#EJERCICIOS 1 AL 10 (DESARROLLO)

                    case 1:#Solicita el nombre del usuario y muestra un saludo personalizado.
                        nombre = input("¿Cúal es tu nombre?: ")
                        chatVPT(f"👋  Hola {nombre.title()}, un placer saludarte.")
                        pausar()

                    case 2:#Convierte una cantidad de kilómetros a millas.
                        try:
                            km = float(input("Kilometros a convertir: "))
                        except ValueError:
                            print(f"❌  Solo se permiten valores numéricos")
                        else:
                            millas = km * 1.18
                            print("🛣️  {:.2f} kilometros equivalen a {:.2f} millas.".format(km,millas))
                        pausar()

                    case 3:#Determina si un número ingresado es par o impar.
                        try:
                            numero = int(input("Ingresa un número: "))
                        except ValueError:
                            print("❌  Solo números enteros\n")
                        else:
                            if numero % 2 == 0:
                                print("El número {} es par.".format(numero))
                            else:
                                chatVPT("El numero {} es impar.".format(numero))
                        pausar()
                        
                    case 4:#Calcula el área de un triángulo a partir de su base y altura.
                        try:
                            base = float(input("Base: "))
                            altura = float(input("Altura: "))
                        except ValueError:
                            print("❌  Solo se permiten valores numéricos.\n")
                        else:
                            area = base*altura/2
                            print("📐  En un triangulo con base {:.2f} y altura {:.2f} el área es: {:.2f}".format(base,altura,area))
                        pausar()

                    case 5:#Muestra la tabla de multiplicar de un número del 1 al 10.
                        while True:
                            try:
                                numero = int(input("Ingresa un número del 1 al 10: "))
                            except ValueError:
                                print("❌  Solo números enteros.\n")
                            else:
                                if numero < 1 or numero > 10:
                                    print(f"{numero} no está permitido, debe ser del 1 al 10. Intenta de nuevo.")
                                else:
                                    chatVPT(f"Tabla del {numero}".ljust(25,"="))
                                    for n in range(1,13):
                                        resultado = numero*n
                                        chatVPT("{} x {} = {}".format(n,numero,resultado),velocidad=0.3)
                                    chatVPT("".ljust(25,"="))
                                    break
                        pausar()

                    case 6:#Calcula la suma de todos los números pares entre 1 y 100.
                        suma = 0
                        tiempo = 0.3
                        for n in range(1,101):
                            if n % 2 == 0:
                                suma += n
                                os.system("cls")
                                print(f"sumando {n}...")
                                if tiempo > 0: time.sleep(tiempo)
                                tiempo -= 0.005
                        chatVPT(f"Los números pares del 1 al 100 suman: {suma}")
                        pausar()

                    case 7:#Crea un programa que adivine un número generado aleatoriamente.
                        numero_aleatorio = random.randint(1,100)
                        numero_usuario = 0
                        intentos = 10
                        while numero_aleatorio != numero_usuario:
                            try:
                                numero_usuario = int(input("Adivina el número: "))
                            except ValueError:
                                chatVPT("❌ Solo números enteros por favor.")
                            else:
                                if intentos == 1: 
                                    chatVPT("El número era {}.".format(numero_aleatorio),
                                            "mejor suerte para la próxima 👋",
                                            pausa=3)
                                    break

                                if numero_usuario in range(1,101):
                                    if numero_usuario == numero_aleatorio:
                                        chatVPT("🥳  !Adivinaste!")
                                        break
                                    else:
                                        intentos -= 1
                                        if intentos > 4: chatVPT("No es {}.".format(numero_usuario))
                                        if intentos > 7: chatVPT("sigue intentando")
                                        if intentos != 3: chatVPT("quedan {} intentos\n".format(intentos))

                                    #ayuda para el usuario
                                    if intentos == 7:
                                        chatVPT("\n😇 ahí te va una ayuda.","" \
                                        "El número que buscas está entre {} y {} 😉".format(numero_aleatorio-random.randint(1,10),numero_aleatorio+random.randint(1,20)),
                                        pausa=2)
                                    elif intentos == 3:
                                        chatVPT("😬  quedan {} intentos.".format(intentos))
                                    elif intentos == 1:
                                        chatVPT("🫣 último intento")
                                else:
                                    chatVPT("Debes ingresar un número entre 1 y 100")
                        pausar()

                    case 8:#Lee una lista de números y muestra el promedio.
                        numeros = []
                        terminar = False
                        chatVPT("Ingresa números para calcular su promedio","ℹ️  Para terminar ingresa 0",pausa=3)
                        while not terminar:
                            try:
                                numero = float(input("Ingresa un número: "))
                            except ValueError:
                                print("Solo valores numéricos por favor.\n")
                            else:
                                if numero != 0:
                                    numeros.append(numero)
                                else:
                                    chatVPT("\nNumeros ingresados: ")
                                    print("".ljust(10,"="))
                                    for i,n in enumerate(numeros,start=1):
                                        chatVPT(f"{i}) {n}",velocidad=0.5)
                                    chatVPT("".ljust(10,"="))

                                    #Calcular promedio
                                    cant_numeros = len(numeros)
                                    promedio = 0
                                    try:
                                        promedio = sum(numeros)/cant_numeros
                                    except ZeroDivisionError as e:
                                        print(f"Error: {e}")
                                    chatVPT("\nRESUMEN:")
                                    chatVPT("".ljust(17,"="))
                                    chatVPT("Cantidad → {:02d}".format(cant_numeros))
                                    chatVPT("    Suma → {:.2f}".format(sum(numeros)))
                                    chatVPT("Promedio → {:.2f}".format(promedio))
                                    print("".ljust(17,"="))
                                    terminar = True
                        pausar()

                    case 9:#Cuenta cuántas veces aparece una palabra en una frase.
                        frase = input("Ingresa una frase: ")
                        palabra = input("Qué palabra quieres buscar en la frase: ").strip()
                        cant_veces = 0
                        palabras = frase.lower().split()
                        chatVPT(f"\nEn tu frase: {frase}",
                                f"la palabra '{palabra}' aparece {palabras.count(palabra)} veces.",
                                velocidad=1.5,pausa=5)
                        pausar()

                    case 10:#Ordena una lista de números ingresados por el usuario.
                        chatVPT(f"Ingresa los números que deseas ordenar","ℹ️  Para salir ingresa 0",velocidad=2,pausa=1)
                        numeros = []
                        while True:
                            try:
                                numero = int(input("Numero: "))
                            except ValueError:
                                print("Solo se permiten números enteros")
                            else:
                                if numero != 0:
                                    numeros.append(numero)
                                else:
                                    numeros.sort()
                                    chatVPT(f"Tus números ordenados:\n")
                                    for n in numeros:
                                        chatVPT(f"{n}")
                                    pausar()
                                    break
                    
                    case 11:#Volver al menú principal
                        break

        case 2:#Ejercicios 11 al 20
           
            pant_carga("cargando ejercicios",tiempo=2.5)

            while True:#Bucle de ejercicios del 11 al 20
                os.system("cls")
                ejercicio = mostrar_menu("🌡️   Convertidor de grados",
                                         "🔢  Calculadora",
                                         "↔️   Verificar palíndromo",
                                         "➰  Sucesión Fibonacci",
                                         "❗  Factorial recursivo",
                                         "🔸  Numero mayor y menor",
                                         "#️⃣   Numero primo",
                                         "🏧  Cajero automático",
                                         "📚  Calificaciones",
                                         "🛍️   Tienda",
                                         "↩️   Volver al menú principal",
                                        nombreMenu="Ejercicios 11 al 20",opcion_inicial=11)
                
                match ejercicio:#EJERCICIOS 11 AL 20 (DESARROLLO)

                    case 11:#Crea un convertidor de grados Celsius a Fahrenheit y viceversa.
                        while True:
                            desicion = mostrar_menu("Celsius",
                                                    "Farenheit",
                                                    nombreMenu="¿Qué convertirás?")
                            
                            if desicion == 1:#Convertir Celsius
                                try:
                                    cant_grados = float(input("Cuántos C° deseas convertir: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten valores numéricos. Intenta otra vez.")
                                else:
                                    resultado = cant_grados * Fraction(9,5) + 32
                                    chatVPT("Convirtiendo {}C° a F°... ⏳".format(cant_grados),
                                            "{}C° = {:.2f}F°".format(cant_grados,resultado), pausa=4)
                                pausar()
                                break
                            elif desicion == 2:#Convertir Farenheit
                                try:
                                    cant_grados = float(input("Cuántos F° deseas convertir: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten valores numéricos. Intenta otra vez.")
                                else:
                                    resultado = (cant_grados - 32) * Fraction(5,9)
                                    chatVPT("Convirtiendo {}F° a C°... ⏳".format(cant_grados),
                                            "{}F° = {:.2f}C°".format(cant_grados,resultado), pausa=4)
                                pausar()
                                break
                            else:#Decisión equivocada
                                print("No hay una opción {} en el menú. Intenta de nuevo.".format(desicion))

                    case 12:#Simula una calculadora básica (+, -, *, /) con menú.
                        mostrar_calc("0.00",animacion=True)
                        
                        operacion = mostrar_menu("Sumar","Restar","Multiplicar","Dividir",nombreMenu="¿Operación?")
                        mostrar_calc(pantalla="0.00")

                        match operacion:
                            
                            case 1:#Sumar
                                try:
                                    op1 = float(input("Primer sumando: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                else:
                                    mostrar_calc(pantalla="{:.2f} +".format(op1),animacion=False)
                                    try:
                                        op2 = float(input("Segundo sumando: "))
                                    except ValueError:
                                        chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                    else:
                                        mostrar_calc(pantalla="{:.2f} + {:.2f}".format(op1,op2),animacion=False)
                                        time.sleep(3)
                                        resultado = op1 + op2
                                        mostrar_calc(pantalla="{:.2f}".format(resultado))

                            case 2:#Restar
                                
                                try:
                                    op1 = float(input("Minuendo: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                else:
                                    mostrar_calc(pantalla="{:.2f} -".format(op1),animacion=False)
                                    try:
                                        op2 = float(input("Sustraendo: "))
                                    except ValueError:
                                        chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                    else:
                                        mostrar_calc(pantalla="{:.2f} - {:.2f}".format(op1,op2),animacion=False)
                                        time.sleep(3)
                                        resultado = op1 - op2
                                        mostrar_calc(pantalla="{:.2f}".format(resultado))

                            case 3:#Multiplicar
                                
                                try:
                                    op1 = float(input("Primer factor: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                else:
                                    mostrar_calc(pantalla="{:.2f} x".format(op1),animacion=False)
                                    try:
                                        op2 = float(input("Segundo factor: "))
                                    except ValueError:
                                        chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                    else:
                                        mostrar_calc(pantalla="{:.2f} x {:.2f}".format(op1,op2),animacion=False)
                                        time.sleep(3)
                                        resultado = op1 * op2
                                        mostrar_calc(pantalla="{:.2f}".format(resultado))

                            case 4:#Dividir
                                try:
                                    op1 = float(input("Dividendo: "))
                                except ValueError:
                                    chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                else:
                                    mostrar_calc(pantalla="{:.2f} /".format(op1),animacion=False)
                                    while True:
                                        try:
                                            op2 = float(input("Divisor: "))
                                        except ValueError:
                                            chatVPT("❌  Solo se permiten números.\n",velocidad=1.3)
                                        else:
                                            if op2 != 0:#divisor correcto
                                                mostrar_calc(pantalla="{:.2f} / {:.2f}".format(op1,op2),animacion=False)
                                                time.sleep(3)
                                                resultado = op1 / op2
                                                mostrar_calc(pantalla="{:.2f}".format(resultado))
                                                break
                                            else:
                                                chatVPT("❌  No se puede dividir entre 0.","Escoge otro divisor",pausa=4)

                        pausar()

                    case 13:#Verifica si una palabra o frase es un palíndromo.
                        frase = input("Ingresa una palabra o frase: ")
                        long = len(frase) - 1
                        frase_invertida = ""
                        for i in range(long,-1,-1):
                            frase_invertida += frase[i:i+1]
                        
                        
                        chatVPT("Tu frase invertida es...",f"{frase_invertida}",pausa=2)
                        if frase.lower() == frase_invertida.lower():
                            chatVPT("✅  es un palíndromo")
                        else:
                            chatVPT("🚫  no es un palíndromo")
                        pausar()
                        
                    case 14:#Genera la sucesión de Fibonacci hasta un número dado.
                        sucecion = [0,1,1]
                        while True:
                            try:
                                numero_limite = int(input("¿Hasta donde quieres la sucesión?: "))
                            except ValueError:
                                chatVPT("❌  Solo puedes ingresar números enteros.")
                            else:
                                for e in sucecion:
                                    nuevo_elem = sucecion[-1] + sucecion[-2]
                                    if nuevo_elem <= numero_limite:
                                        sucecion.append(nuevo_elem)
                                break
                        print(sucecion,"\n")
                        chatVPT(f"¡Listo!, suceción fibonacci sin exceder {numero_limite}")
                        pausar()

                    case 15:#Calcula el factorial de un número utilizando recursividad
                        while True:
                            try:
                                numero = int(input("Ingresa un número: "))
                            except ValueError:
                                chatVPT("❌  Solo números enteros por favor.")
                            else:
                                if numero > 0:
                                    factor_aux = 2
                                    acumulado = 1
                                    for i in range(1,numero):
                                        acumulado *= factor_aux
                                        factor_aux += 1
                                    
                                    resultado = f"!{numero} = "
                                    for i in range(1,numero+1):
                                        if i<numero:
                                            resultado += f"{i} x "
                                        else:
                                            resultado += f"{i} = {acumulado}"
                                    chatVPT(f"{resultado}")
                                    break
                                else:
                                    chatVPT("❌  El número debe ser mayor a 0.")
                        pausar()

                    case 16:#Encuentra el número mayor y menor en una lista.

                        numero = []

                        for i in range(5):
                            n = int(input("Introduce 5 numeros: "))
                            numero.append(n)

                        mayor = max(numero)
                        menor = min(numero)

                        print("El numero mayor es:", mayor)
                        print("El numero menor es:", menor)
                        pausar()

                    case 17:#Verifica si un número es primo.
                        numero = int(input("Introduce un numero: "))

                        if numero <= 1:
                            print("No es primo")
                            pausar()
                        else:
                            es_primo = True
                            for i in range(2, int(numero ** 0.5) + 1):
                                if numero % i == 0:
                                    es_primo = False
                                    break

                            if es_primo:
                                print("Es primo")
                                pausar()
                            else:
                                print("No es primo")
                                pausar()
                        

                    case 18:#Simula un cajero automático con saldo y retiros.
                        saldo = 1000

                        print("Bienvenido al Cajero Automatico")

                        while True:
                            print("\nSaldo disponible: $", saldo)
                            opcion = input("¿Deseas hacer un retiro? (s/n): ").lower()

                            if opcion == "n":
                                print("Gracias por usar el cajero.")
                                break

                            if opcion == "s":
                                try:
                                    monto = float(input("Introduce el monto a retirar: "))
                                    if monto <= 0:
                                        print("El monto debe ser mayor que cero.")
                                    elif monto > saldo:
                                        print("Fondos insuficientes.")
                                    else:
                                        saldo -= monto
                                        print(f"Has retirado ${monto}. Nuevo saldo: ${saldo}")
                                except ValueError:
                                    print("Entrada no valida. Intenta con un numero.")
                            else:
                                print("Opción no reconocida. Escribe 's' o 'n'.")
                        pausar()

                    case 19:#Crea un diccionario de estudiantes con sus calificaciones.
                        estudiantes = {
                            "Ana": 85,
                            "Luis": 92,
                            "Maria": 78,
                            "Carlos": 88,
                            "Sofia": 95
                        }

                        for nombre, calificacion in estudiantes.items():
                            print(f"{nombre} tiene una calificacion de {calificacion}")
                        pausar()

                    case 20:#Simula una tienda que permita agregar productos y calcular el total.
                        carrito = {}
                        print("Bienvenido a la Tienda\n")

                        while True:
                            producto = input("Introduce el nombre del producto (o 'fin' para terminar): ")
                            if producto.lower() == "fin":
                                print("Gracias por usar nuestros servicios")
                                break
                            try:
                                precio = float(input(f"Introduce el precio de '{producto}': "))
                                carrito[producto] = precio
                            except ValueError:
                                print("Precio no valido. Intenta de nuevo.")

                        print("\nProductos en el carrito:")
                        total = 0
                        for producto, precio in carrito.items():
                            print(f"- {producto}: ${precio}")
                            total += precio

                        print(f"\nTotal a pagar: ${total}")
                        pausar()

                    case 21:#Volver al menú principal
                        break

        case 3:#Ejercicios 21 al 30
            
<<<<<<< Updated upstream
            while True:
                ejercicio = mostrar_menu("🔡 cantidad de vocales",
                                        "❌ eliminar duplicados",
                                        "🔑 validación de contraseña",
                                        "📒 agenda de contactos",
                                        "🤖 opciones multiples",
                                        "🧑 clase persona",
                                        "🏦 clase CuentaBancaria",
                                        "🛒 clase Producto",
                                        "🟩 clase Rectangulo",
                                        "📘 clase Libro",
                                        "↩️  Volver al menú principal",
                                        opcion_inicial=21
                                        )
                
                match ejercicio:#Ejercicios del 21 al 30 (DESARROLLO)

                    case 21:#Lee una frase y muestra cuántas vocales tiene
                        pass
                    case 22:#Elimina los duplicados de una lista de números
                        pass
                    case 23:#Valida una contraseña con reglas mínimas (longitud, número, mayúscula)
                        pass
                    case 24:#Crea una agenda de contactos que permita agregar y buscar por nombre
                        pass
                    case 25:#Simula un menú de opciones (saludar, calcular, salir)
                        pass
                    case 26:#Crea una clase Persona con atributos nombre y edad, e imprime sus datos
                        pass
                    case 27:#Implementa una clase CuentaBancaria con métodos para depositar y retirar
                        pass
                    case 28:#Diseña una clase Producto que calcule el total con impuestos
                        pass
                    case 29:#Crea una clase Rectángulo que calcule el área y el perímetro
                        pass
                    case 30:#Implementa una clase Libro con atributos título, autor y año
                        pass
                    case 31:#Volver al menú principal
                        break
                    
        case 4:#Ejercicios 31 al 40

            pant_carga("cargando ejercicios",tiempo=2.5)

            while True:#Bucle de ejercicios del 31 al 40
                os.system("cls")
                ejercicio = mostrar_menu("🏍️  Clase Vehículo",
                                         "📝 Clase Estudiante ",
                                         "🛒 Clase Tienda ",
                                         "💼 Clase Empleado ",
                                         "📄 Clase Factura",
                                         "🛠️  En proceso...",
                                         "🛠️  En proceso...",
                                         "🛠️  En proceso...",
                                         "🛠️  En proceso...",
                                         "🛠️  En proceso...",
                                         "↩️  Volver al menú principal ",
                                        nombreMenu="Ejercicios 31 al 40",
                                        opcion_inicial=31)
                
                match ejercicio:#EJERCICIOS 31 AL 40 (DESARROLLO)

                    case 31:#Diseña una clase Vehículo con subclases Auto y Moto.
                        class Vehiculo:
                            def __init__(self,marca,año):
                                self.marca = marca
                                self.año = año

                            def __str__(self):
                                return f"Vehículo marca {self.marca} fabricado en {self.año}"
                            
                        class Auto(Vehiculo):
                            def __init__(self, marca, año, aire:bool):
                                super().__init__(marca, año)
                                self.aire = aire

                        class Moto(Vehiculo):
                            def __init__(self, marca, año, cc):
                                super().__init__(marca, año)
                                self.cc = cc

                        
                        vehiculo1 = Vehiculo("Toyota",1994)
                        vehiculo2 = Auto("Honda",2012,True)
                        vehiculo3 = Moto("Yamaha",2015,1000)
                        print(f"Vehículo 1: {vehiculo1}")
                        print(f"Vehículo 2: {vehiculo2}")
                        print(f"Vehículo 3: {vehiculo3}")
                        print(f"Aire de vehículo2: {vehiculo2.aire}")
                        
                        pausar()
                                
                    case 32:#Crea una clase Estudiante con método para calcular promedio de notas.
                        class Estudiante:
                            def __init__(self,nombre,notas:list):
                                self.nombre = nombre
                                self.notas = notas

                            def añadir_nota(self,nota):
                                if nota in range(1,101):
                                    self.notas.append(nota)
                                else:
                                    chatVPT(f"{nota} no es un valor válido en añadir_nota()")

                            def calcular_promedio(self):
                                try:
                                    promedio = sum(self.notas) / len(self.notas)
                                except ZeroDivisionError as e:
                                    chatVPT("Se ha producido un error en calcular_promedio()",f"Error: {e}")
                                else:
                                    chatVPT("El promedio de notas de {} es: {:.2f}".format(self.nombre,promedio))

                        estudiante1 = Estudiante("Vielko",[97,91,98])
                        print(f"Notas: {estudiante1.notas}")
                        estudiante1.calcular_promedio()
                        estudiante1.añadir_nota(98)
                        print(f"Nuevas notas: {estudiante1.notas}")
                        estudiante1.calcular_promedio()

                        pausar()

                    case 33:#Implementa una clase Tienda que almacene productos en un diccionario.
                        class Tienda:

                            def __init__(self,nombre,productos:dict):
                                self.nombre = nombre
                                self.productos = productos

                            def __str__(self):
                                info = f"La tienda {self.nombre} tiene:\n"
                                for i,producto in enumerate(self.productos,start=1):
                                    info += f"{i}. {producto} a {self.productos[producto]}\n"
                                return info
                            
                            def añadir_producto(self,producto:str,precio:float):
                                self.productos[producto] = precio

                            def mostrar_productos(self):
                                return self.productos
                            
                        tienda1 = Tienda("Mercadito de Luis",{"Arroz":50,"Huevos":210,"Aceite":325})
                        print(tienda1)
                        tienda1.añadir_producto("Azucar",35)
                        print(tienda1.mostrar_productos())

                        pausar()

                    case 34:#Crea una clase Empleado y calcula su salario neto con descuentos.
                        class Empleado:

                            def __init__(self,nombre,salario:float,empresa):
                                self.nombre = nombre
                                self.__salario = salario
                                self.empresa = empresa

                            def __str__(self):
                                return f"{self.nombre} devenga {formato_moneda(self.__salario)} en {self.empresa}."

                            def realizar_descuento(self):
                                afp = self.__salario*.0287
                                ars = self.__salario*.0304
                                base_impositiva = (self.__salario - afp - ars) * 12


                                if base_impositiva <= 416220.01:
                                    mensaje = f"ISR: La base impositiva no supera los RD$416,220.01\n"\
                                            f"por esta razón, está exento."
                                    retencion_mensual = 0
                                elif base_impositiva <= 624329:
                                    excedente = base_impositiva - 416220.01
                                    base_impositiva -= excedente*.15
                                    mensaje = f"ISR: Se descontó un 15% del excedente de RD$416,220.01\n"\
                                            f"equivalente a {formato_moneda(excedente*.15)}."
                                    retencion_mensual = excedente*.15/12

                                elif base_impositiva <= 867123:
                                    excedente = base_impositiva - 624329.01
                                    base_impositiva -= 31216 + excedente*.2
                                    mensaje = f"ISR: Se descontó RD$31,216 más un 20% del excedente de RD$624,329.01\n"\
                                            f"equivalente a {formato_moneda(excedente*.2)}."
                                    retencion_mensual = (31216 + excedente*.2) /12

                                else:
                                    excedente = base_impositiva - 867123
                                    base_impositiva -= 79776 + excedente*.25
                                    mensaje = f"ISR: Se descontó RD$79,776 más un 25% del excedente de RD$867,123\n"\
                                            f"equivalente a {formato_moneda(excedente*.25)}."
                                    retencion_mensual = (79776 + excedente*.25) /12

                                salario_neto = formato_moneda(base_impositiva/12)

                                resumen = f"{self.nombre} devenga un salario de {formato_moneda(self.__salario)}\n"\
                                        f"Descuentos realizados:\n====================\n"
                                resumen += f"{mensaje}\n"
                                if retencion_mensual != 0: 
                                    resumen += f"Retención mensual: {formato_moneda(retencion_mensual)}\n"
                                resumen += f"AFP: {formato_moneda(afp)} (2.87%)\nARS: {formato_moneda(ars)} (3.04%)\n"\
                                f"💲 salario neto de {empleado1.nombre}: {salario_neto}"

                                chatVPT(resumen,velocidad=3)

                        empleado1 = Empleado("Vielko",100000,"Maviell Comercial SRL")
                        empleado1.realizar_descuento()
                        pausar()

                    case 35:#Diseña una clase Factura que permita registrar productos y calcular el total.
                        class Factura:

                            def __init__(self,cliente:str,articulos:dict = {}):
                                self.cliente = cliente
                                self.articulos = articulos

                            def __str__(self):
                                if len(self.articulos) == 0:
                                    return f"La factura de {self.cliente} aún está vacía.\n"
                                else:
                                    return "La factura de {:s} contiene {:d} artículos.\nTotal: {}"\
                                        "".format(self.cliente,len(self.articulos),formato_moneda(self.calcular_total()))
                                
                            def agregar_productos(self):

                                print("  ℹ️  Para terminar escribe 'salir'")
                                print("".ljust(14,"="),f"Factura: {self.cliente}","".ljust(14,"="))
                                salir = False
                                contador = 1
                                while not salir:
                                    try:
                                        articulo = input(f"Artículo #{contador}: ")
                                        if articulo.lower() != "salir":
                                            precio = float(input("Precio: "))
                                        else:
                                            break
                                    except ValueError:
                                        print("Solo valores numéricos por favor.\n")
                                    else:
                                        self.articulos[articulo] = precio
                                        contador += 1
                            
                            def mostrar_factura(self):

                                if len(self.articulos) != 0:
                                    print("\n"+" Cliente: {}".format(self.cliente).rjust(45,"="))
                                    for i,(articulo,precio) in enumerate(self.articulos.items(),start=1):
                                        print(f" {i}.{articulo}".ljust(20,"."),formato_moneda(precio).rjust(24,"."),sep="")
                                    print("".ljust(45,"="))
                                    print(" Total",formato_moneda(self.calcular_total()).rjust(39,"."),sep="")
                                else:
                                    print(f"No hay artículos en la factura de {self.cliente}.\n")

                            def calcular_total(self):

                                total = 0
                                for precio in self.articulos.values():
                                    total += precio
                                return total
                            

                        factura1 = Factura("Gregory")
                        factura2 = Factura("Victor",{"canela":85,"aguacates":50})
                        factura3 = Factura("Diego")

                        print(factura1,factura2,factura3)

                        factura1.agregar_productos()
                        factura1.mostrar_factura()
                        factura2.agregar_productos()
                        factura2.mostrar_factura()

                        pausar()

                    case 36:#
                        pass
                    case 37:#
                        pass
                    case 38:#
                        pass
                    case 39:#
                        pass
                    case 40:#
                        pass
                    case 41:#Volver al menú principal
                        break

        case 5:#salir
            chatVPT("😊  ¡Hasta pronto!")
            salir = True