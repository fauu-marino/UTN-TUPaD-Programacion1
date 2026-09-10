# Ejercicio 5 - "Escape Room: La Arena del Gladiador"

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Ingrese el nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Ingrese el nombre del Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_pesado = 15
daño_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    turno_gladiador = True
    print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige una accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion_valida = False
    while not opcion_valida:
        opcion_input = input("Opcion: ")
        if not opcion_input.isdigit():
            print("Error: Ingrese un numero valido.")
        elif int(opcion_input) < 1 or int(opcion_input) > 3:
            print("Error: opcion fuera de rango.")
        else:
            opcion_valida = True
    opcion = int(opcion_input)

    if opcion == 1:
        if vida_enemigo < 20:
            daño_final = daño_pesado * 1.5
            print(">> ¡Golpe critico!")
        else:
            daño_final = daño_pesado
        vida_enemigo -= daño_final
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print("Bebiste una pocion y recuperaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")

    turno_gladiador = False

    if vida_enemigo <= 0:
        break

    print(">> ¡El enemigo contraataca por 12 puntos!")
    vida_gladiador -= daño_enemigo

    print("=== NUEVO TURNO ===\n")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
