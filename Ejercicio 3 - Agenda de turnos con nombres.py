#Ejercicio 3 - "Agenda de turnos con nombre"

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")
while operador == "" or not operador.isalpha():
    print("Error: el nombre solo puede contener letras.")
    operador = input("Ingrese el nombre del operador: ")

salir = False
while not salir:
    print()
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion_input = input("Eliga una opcion: ")
    while not opcion_input.isdigit() or int(opcion_input) < 1 or int(opcion_input) > 5:
        print("Error: opcion invalida.")
        opcion_input = input("Eliga un opcion: ")
    opcion = int(opcion_input)
    if opcion == 1:
        dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        while not dia_input.isdigit() or (int(dia_input) != 1 and int(dia_input) != 2):
            print("Error: opcion invalida.")
            dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        dia = int(dia_input)

        paciente = input("Ingrese el nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre solo puede contener letras.")
            paciente = input("Ingrese el nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: el paciente ya tiene un turno el Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado: Lunes - Turno 1.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado: Lunes - Turno 2.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado: Lunes - Turno 3.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado: Lunes - Turno 4.")
            else:
                print("No hay turnos disponibles el Lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: el paciente ya tiene un turno el Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado: Martes - Turno 1.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado: Martes - Turno 2.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado: Martes - Turno 3.")
            else:
                print("No hay turnos disponibles el Martes.")

    elif opcion == 2:
        dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        while not dia_input.isdigit() or (int(dia_input) != 1 and int(dia_input) != 2):
            print("Error: opcion invalida.")
            dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        dia = int(dia_input)

        paciente = input("Ingrese el nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre solo puede contener letras.")
            paciente = input("Ingrese el nombre del paciente: ")

        encontrado = False
        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado con exito.")
        else:
            print("Error: no se encontro un turno con ese nombre en ese dia.")

    elif opcion == 3:
        dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        while not dia_input.isdigit() or (int(dia_input) != 1 and int(dia_input) != 2):
            print("Error: opcion invalida.")
            dia_input = input("Elegir dia (1 - Lunes, 2 - Martes): ")
        dia = int(dia_input)

        if dia == 1:
            print("--- Agenda del Lunes ---")

            if lunes1 != "":
                valor_a_mostrar = lunes1
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 1: {valor_a_mostrar}")

            if lunes2 != "":
                valor_a_mostrar = lunes2
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 2: {valor_a_mostrar}")

            if lunes3 != "":
                valor_a_mostrar = lunes3
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 3: {valor_a_mostrar}")

            if lunes4 != "":
                valor_a_mostrar = lunes4
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 4: {valor_a_mostrar}")
        else:
            print("--- Agenda del Martes ---")

            if martes1 != "":
                valor_a_mostrar = martes1
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 1: {valor_a_mostrar}")

            if martes2 != "":
                valor_a_mostrar = martes2
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 2: {valor_a_mostrar}")

            if martes3 != "":
                valor_a_mostrar = martes3
            else:
                valor_a_mostrar = "(libre)"
            print(f"Turno 3: {valor_a_mostrar}")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        disponibles_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        disponibles_martes = 3 - ocupados_martes

        print("--- Resumen General ---")
        print(f"Lunes:  {ocupados_lunes} ocupados, {disponibles_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con mas turnos ocupados: Martes")
        else:
            print("Empate entre Lunes y Martes.")

    elif opcion == 5:
        print("Cerrando sistema...")
        salir = True
