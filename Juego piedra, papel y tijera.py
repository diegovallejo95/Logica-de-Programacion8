#JUEGO PIEDRA, PAPEL Y TIJERA
print("Bienvenido al juego de piedra, papel y tijera")

opcion_usuario = int(input("Escoja 1 para piedra, 2 para papel o 3 para tijeras: "))
opcion_computadora= int(input("La computadora elige: "))

if opcion_usuario == opcion_computadora:
    print("Empate")
elif (opcion_usuario == 1 and opcion_computadora == 3) or (opcion_usuario == 2 and opcion_computadora == 1) or (opcion_usuario == 3 and opcion_computadora == 2):
    print("Ganaste")
else:  print("Perdiste")



