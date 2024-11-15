import random

def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'sql', 'react', 'spring', 'flask', 'git']

    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")

    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras en la palabra es:", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha:
            print("Por favor introdusca un caracter valido (sólo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print(f"Ya has utilizado la letra {adivinanza}, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien has acertado, la letra {adivinanza} esta en la palabra")
            else:
                intentos -= 1
                print(f"La letra {adivinanza} no esta en la palabra secreta")
                print(f"Te quedan {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual.capitalize())
        
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Felicidades has ganado el juego! La palabra es: {palabra_secreta.capitalize()}")
    
    if intentos == 0:
        print(f"Has perdido :C, la parabra secreta era: {palabra_secreta.capitalize}")

juego_ahorcado()