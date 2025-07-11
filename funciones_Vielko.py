import os,time

def mostrar_menu(*opcion:str,
                 opcion_inicial = 1,
                 nombreMenu = "MENÚ PRINCIPAL",
                 mensaje_salir = "para salir ingresa ",
                 opcion_salir = 0):
    '''
    muestra un menú personalizado que devuelve la opcion
    seleccionada por el usuario.

    devuelve un int con la opcion del usuario.

    Argumentos
        *opcion -> nombre de cada una de las opciones
        opcion_inicial -> índice de la primera opción
        nombreMenu -> nombre a mostrar en el menú
        mensaje_salir -> comentario de salida
        opcion_salir -> opcion para salir del menú
    '''
    cant_opciones = 0
    print(f"{nombreMenu} ".ljust(len(nombreMenu)+10,"="))
    for i,opcion in enumerate(opcion,start=opcion_inicial):
        print(f"{i}. {opcion}")
        cant_opciones += 1
    print()
    print(f"{mensaje_salir} {opcion_salir}".rjust(len(nombreMenu)+10))
    print("".ljust(len(nombreMenu)+10,"="))
    rango = range(opcion_inicial,opcion_inicial+cant_opciones)

    opcion_valida = False

    while not opcion_valida:
        try:
            respuesta = int(input("Escoge una opción: "))
        except ValueError:
            print("Solo se permiten números.")
        else:
            if respuesta in rango or respuesta == opcion_salir:
                opcion_valida = True
            else:
                chatVPT(f"No hay una opción {respuesta} en el menú.","Intenta de nuevo.",pausa=2)
    print()
    return respuesta

def si_no(pregunta = ""):
    '''
    Devuelve True si el usuario responde
    si o False si responde que no.

    Argumento
        pregunta -> La pregunta a realizar
    '''
    while True:
        try:
            print(pregunta)
            decicion = int(input("1.Si\n2.No\nDecición: "))
        except ValueError:
            print("El valor ingresado no es correcto.")
        else:
            if decicion == 1 or decicion == 2:
                break
            else:
                print("Solo puedes escoger\n1 para si\n2 para no")
    if int(decicion) == 1:
        return True
    return False

def formulario(*datos,nombreFormulario = "REGISTRO"):
    '''
    Devuelve un diccionario con información que solicita
    al usuario. Cada dato que devuelve es str, en caso de
    necesitar otro tipo se debe hacer un casting.

    Argumentos
        *datos -> los datos a solicitar al usuario
        nombreFormulario -> el nombre a mostrar en el titulo por defecto es REGISTRO
    '''


    informacion = {}

    print(f"{nombreFormulario} ".ljust(25,"="))
    for dato in datos:
        informacion[dato] = input(f"• {dato}: ")

    return informacion

def formato_moneda(monto:float,moneda = "RD"):
    '''
    devuelve un valor monetario con formato de moneda

    Parámetros
        :monto -> el monto a formatear
        :moneda -> la denominación a colocar antes de $
    '''

    valor_formateado = f"{moneda}$ "
    cifra_str = "{:.2f}".format(monto)
    tamaño = len(cifra_str)

    if tamaño < 7: #cientos
        valor_formateado += cifra_str
    elif tamaño < 8: #miles
        valor_formateado += cifra_str[0:1] + "," + cifra_str[1:]
    elif tamaño < 9: #decenas miles
        valor_formateado += cifra_str[0:2] + "," + cifra_str[2:]
    elif tamaño < 10: #cientos miles
        valor_formateado += cifra_str[0:3] + "," + cifra_str[3:]
    elif tamaño < 11: #millones
        valor_formateado += cifra_str[0:1] + "," + cifra_str[1:4] + "," + cifra_str[4:]
    elif tamaño < 12: #decenas millones
        valor_formateado += cifra_str[0:2] + "," + cifra_str[2:5] + "," + cifra_str[5:]
    elif tamaño < 13: #centenas millones
        valor_formateado += cifra_str[0:3] + "," + cifra_str[3:6] + "," + cifra_str[6:]
    else:
        valor_formateado += cifra_str
    return valor_formateado

def formato_telefono(tel_param = "null"):
    '''
    Devuelve un número con formato (8x9) xxx-xxxx.
    Si no se le pasa el parámetro lo solicita.

    Parámetros
        :tel_param -> cadena que represente un número telefónico
    '''
    
    tel_formateado = ""

    if tel_param == "null":
        while True:
            digitos = 0
            digitos_introducidos = ""
            telefono = input("Teléfono: ")

            for caracter in telefono:
                if caracter.isnumeric():
                    digitos += 1
                    digitos_introducidos += caracter
                else:
                    if caracter not in "-() ":
                        print("❌  Solo se permiten números enteros, guiones o paréntesis:")
                        print("Ejemplos: 809000000 | 809-000-0000 | (809) 000-0000\n")
                        break
            
            if  digitos != 0:
                if digitos_introducidos[0:3] == "809" or digitos_introducidos[0:3] == "849" or digitos_introducidos[0:3] == "829":
                    if digitos == 10:
                        tel_formateado = "(" + digitos_introducidos[0:3] + ")" + f" {digitos_introducidos[3:6]}-{digitos_introducidos[6:]}"
                        break
                    else:
                        print(f"❌ {digitos_introducidos}! Deben ser 10 números. Intenta de nuevo\n")
                else:
                    print("❌  Error: debe iniciar con 809, 829 u 849")
            else:
                print("❌  Debes ingresar números.")

    else:#Si se recibe un teléfono como parámetro
        digitos = 0
        digitos_introducidos = ""
        for caracter in tel_param:
            if caracter.isnumeric():
                digitos += 1
                digitos_introducidos += caracter
            else:
                if caracter not in "-() ":
                    print("❌  Solo se permiten números enteros, guiones o paréntesis:")
                    print("Ejemplos: 809000000 | 809-000-0000 | (809) 000-0000\n")
                    break

        if  digitos != 0:
            if digitos_introducidos[0:3] == "809" or digitos_introducidos[0:3] == "849" or digitos_introducidos[0:3] == "829":
                if digitos == 10:
                    tel_formateado += "(" + digitos_introducidos[0:3] + ")" + f" {digitos_introducidos[3:6]}-{digitos_introducidos[6:]}"
                else:
                    print(f"❌  {digitos_introducidos}! Deben ser 10 números. Intenta de nuevo\n")
            else:
                print("❌  Error: debe iniciar con 809, 829 u 849")
        else:
            print("❌  Debes ingresar números.")
    return tel_formateado

def chatVPT(texto1,texto2 = "",velocidad = 1,pausa = 4):
    '''
    Vielko's Pre-trained Transformer
    Muestra un texto al estilo de la IA.

    Argumentos
        texto -> texto a mostrar.
        texto2 -> texto2 adicional. Reemplaza a texto1
        velocidad -> cuanto menor el número más rápido. por defecto es 1
        pausa -> tiempo a esperar antes de escribir texto2. por defecto es 4
    '''
    if texto2 == "":
        for l in texto1:
            print(l,end="",flush=True)
            time.sleep(velocidad/len(texto1))
        print()
    else:
        for l in texto1:
            print(l,end="",flush=True)
            time.sleep(velocidad/len(texto1))
        print("\r",end="")

        reemplazo = texto2.ljust(len(texto1)+1)
        time.sleep(pausa)

        for l in reemplazo:
            print(l,end="",flush=True)
            time.sleep(velocidad/len(texto1))
        print()

def pant_carga(texto = "cargando",tiempo = 5.0,velocidad = 0.055):

    '''
    Presenta una pantalla de carga con un reloj dinámico.
    Permite establecer tiempo y velocidad de presentación.

    Argumentos
        texto -> mensaje a mostrar: Por defecto: 'cargando'
        tiempo -> duración de la animación. Por defecto: 5
        velocidad -> cuanto menor más rápido. Por defecto: 0.055
    '''
    for i in range(0,int(tiempo)):
        os.system("cls")
        print(f"🕐 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕑 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕒 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕓 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕔 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕕 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕖 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕗 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕘 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕙 {texto}...")
        time.sleep(velocidad)
        os.system("cls")
        print(f"🕚 {texto}...")
        time.sleep(velocidad)
    os.system("cls")

def mostrar_calc(pantalla="0.00",animacion=False):
    if animacion:
        os.system("cls")
        chatVPT("CASIO vmv16".rjust(25))
        chatVPT("".ljust(25,"="))
        print("||",f"{pantalla}".rjust(19),"||")
        chatVPT("".ljust(25,"="))
        print("".ljust(25,"-"))
        print("|".ljust(2),"7","|".rjust(2),"8".rjust(2),"|".rjust(2),"9".rjust(2),"|".rjust(2),"➕  |".rjust(2))
        print("|".ljust(2),"4","|".rjust(2),"5".rjust(2),"|".rjust(2),"6".rjust(2),"|".rjust(2),"➖  |".rjust(2))
        print("|".ljust(2),"1","|".rjust(2),"2".rjust(2),"|".rjust(2),"3".rjust(2),"|".rjust(2),"✖️   |".rjust(3))
        print("|  0".rjust(16),"|".rjust(2),"➗  |")
        print("".ljust(25,"-"),"\n")
    else:
        os.system("cls")
        print("CASIO vmv16".rjust(25))
        print("".ljust(25,"="))
        print("||",f"{pantalla}".rjust(19),"||")
        print("".ljust(25,"="))
        print("".ljust(25,"-"))
        print("|".ljust(2),"7","|".rjust(2),"8".rjust(2),"|".rjust(2),"9".rjust(2),"|".rjust(2),"➕  |".rjust(2))
        print("|".ljust(2),"4","|".rjust(2),"5".rjust(2),"|".rjust(2),"6".rjust(2),"|".rjust(2),"➖  |".rjust(2))
        print("|".ljust(2),"1","|".rjust(2),"2".rjust(2),"|".rjust(2),"3".rjust(2),"|".rjust(2),"✖️   |".rjust(3))
        print("|  0".rjust(16),"|".rjust(2),"➗  |")
        print("".ljust(25,"-"),"\n")
