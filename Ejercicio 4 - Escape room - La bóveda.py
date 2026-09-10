# Ejercicio 4 - "Escape Room: La Boveda"

print("=== ESCAPE ROOM: LA BOVEDA ===\n")

agente = input("Ingrese el nombre del agente: ")
while agente == "" or not agente.isalpha():
    print("Error: el nombre solo puede contener letras.")
    agente = input("Ingrese el nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar = 0
bloqueado = False

print(f"\nBienvenido/a, agente {agente}.")
print("Objetivo: abrir las 3 cerraduras antes de quedarte sin energia o sin tiempo.\n")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print("-" * 45)
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion_valida = False
    while not opcion_valida:
        opcion_input = input("Eliga una opcion: ")
        if not opcion_input.isdigit():
            print("Error: ingrese un numero valido.")
        elif int(opcion_input) < 1 or int(opcion_input) > 3:
            print("Error: opcion fuera de rango.")
        else:
            opcion_valida = True
    opcion = int(opcion_input)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar += 1

        if forzar == 3:
            alarma = True
            print("La cerradura se trabó por tanto forcejeo. Se activo la alarma!")
            forzar = 0
        elif energia < 40:
            print("Riesgo de alarma: tu pulso esta inestable por el cansancio.")
            numero_valido = False
            while not numero_valido:
                numero_input = input("Eliga un numero (1-3): ")
                if not numero_input.isdigit():
                    print("Error: ingrese un numero valido.")
                elif int(numero_input) < 1 or int(numero_input) > 3:
                    print("Error: opcion fuera de rango.")
                else:
                    numero_valido = True
            numero = int(numero_input)
            if numero == 3:
                alarma = True
                print("Mala suerte... se activo la alarma!")
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con exito.")
        else:
            cerraduras_abiertas += 1
            print("Cerradura forzada con exito.")

    elif opcion == 2:
        forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 - Codigo parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Codigo completo! Se abrio una cerradura automaticamente.")

    elif opcion == 3:
        forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma sigue sonando y te quita energia extra.")
        else:
            print("Descansaste y recuperaste energia.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print("=" * 45)
if cerraduras_abiertas == 3:
    print(f"VICTORIA! Agente {agente} has abierto la boveda a tiempo.")
elif bloqueado:
    print("DERROTA (bloqueo). El sistema se bloqueo por la alarma.")
else:
    print("DERROTA. Te quedaste sin energia o sin tiempo.")