# import nos permite agregar librerías externas a nuestro código. Y random es para generar números aleatorios.
import random

#Mensaje de bienvenida al usuario
print("Bienvenido al Juego: Piedra, Papel o Tijera")

# Opciones del juego /TUPLA
opciones = ("Piedra", "Papel", "Tijera")

# Opción del jugador
jugador = int(input("Por favor haz tu eleccion: 1-Piedra, 2-Papel, 3-Tijera: "))
computadora = random.randint(1, 3)


# Validar opción del jugador
while jugador < 1 or jugador > 3:
    print("Opción no válida. Por favor elige 1, 2 o 3.")
    jugador = int(input("Por favor haz tu eleccion: 1-Piedra, 2-Papel, 3-Tijera: "))
else:
    # Computadora elige al azar
    computadora

    #se escoge la opción del jugador de la tupla opciones, restando 1 al índice porque las tuplas comienzan en 0.
    print("Tú elegiste:", opciones[jugador - 1])  
    #se escoge la opción de la computadora de la tupla opciones, restando 1 al índice porque las tuplas comienzan en 0.
    print("La computadora eligió:", opciones[computadora - 1]) 
    
# Comparar resultados / logica del juego
if jugador == computadora:
    print("Resultado: Empate")    
# Opciones de victoria del jugador
elif (jugador == 1 and computadora == 3) or \
     (jugador == 2 and computadora == 1) or \
     (jugador == 3 and computadora == 2):
        print("Resultado: ¡Ganaste!")    
# Si ninguna de las condiciones anteriores se cumple, significa que la computadora gana.
else:
     print("Resultado: La computadora gana")



