import random

print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
print("REGLAS DEL JUEGO:")
print("Elemento: Piedra-Tijeras | Piedra-Papel | Papel-Tijeras")
print("Ganador : Piedra         | Papel        | Tijeras")
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")

veces = int(input("Introduce el número de veces que quieres jugar: "))

print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")

repetir = 0

a = "Piedra [🗿]"
b = "Papel [📄]"
c = "Tijeras [✂️]"

def elegir():

    string_aleatorio = random.randint(1, 3)
    
    eleccion_jugador = int(input("Elige un número (1-Piedra | 2-Papel | 3-Tijeras) : "))
    
    if string_aleatorio == 1:
        if eleccion_jugador == 1:
            print("-----------------------------------------------------------------------------")
            print("Empate, has elejido 'Piedra [🗿]' y el script ha elegido " + a)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 2:
            print("-----------------------------------------------------------------------------")
            print("Has ganado, has elegido 'Papel [📄]' y el script ha elegido " + a)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 3:
            print("-----------------------------------------------------------------------------")
            print("Has perdido, has elegido 'Tijeras [✂️]' y el script ha elegido " + a)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador != 1 and eleccion_jugador != 2 and eleccion_jugador != 3:
            print("-----------------------------------------------------------------------------")
            print("¡¡Has puesto un número incorrecto!!")
            print("-----------------------------------------------------------------------------")
    
    if string_aleatorio == 2:
        if eleccion_jugador == 1:
            print("-----------------------------------------------------------------------------")
            print("Has perdido, has elejido 'Piedra [🗿]' y el script ha elegido " + b)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 2:
            print("-----------------------------------------------------------------------------")
            print("Empate, has elegido 'Papel [📄]' y el script ha elegido " + b)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 3:
            print("-----------------------------------------------------------------------------")
            print("Has ganado, has elegido 'Tijeras [✂️]' y el script ha elegido " + b)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador != 1 and eleccion_jugador != 2 and eleccion_jugador != 3:
            print("-----------------------------------------------------------------------------")
            print("¡¡Has puesto un número incorrecto!!")
            print("-----------------------------------------------------------------------------")
    
    if string_aleatorio == 3:
        if eleccion_jugador == 1:
            print("-----------------------------------------------------------------------------")
            print("Has ganado, has elejido 'Piedra [🗿]' y el script ha elegido " + c)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 2:
            print("-----------------------------------------------------------------------------")
            print("Has perdido, has elegido 'Papel [📄]' y el script ha elegido " + c)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador == 3:
            print("-----------------------------------------------------------------------------")
            print("Empate, has elegido 'Tijeras [✂️]' y el script ha elegido " + c)
            print("-----------------------------------------------------------------------------")
            
        if eleccion_jugador != 1 and eleccion_jugador != 2 and eleccion_jugador != 3:
            print("-----------------------------------------------------------------------------")
            print("¡¡Has puesto un número incorrecto!!")
            print("-----------------------------------------------------------------------------")
    
while repetir < veces:
    elegir()
    repetir += 1