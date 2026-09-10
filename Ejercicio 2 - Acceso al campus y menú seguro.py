# Ejercicio 2 - "Acceso al Campus y Menu Seguro"

usuario_correcto = "alumno"
clave_correcta = "python123"

acceso_concedido = False
intentos = 0

while intentos < 3 and not acceso_concedido:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: Usuario y/o clave incorrecto.")

if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    salir = False
    while not salir:
        print()
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        opcion_valida = False
        while not opcion_valida:
            opcion_input = input("Opcion: ")
            if not opcion_input.isdigit():
                print("Error: debe ingresar un numero valido.")
            elif int(opcion_input) < 1 or int(opcion_input) > 4:
                print("Error: la opcion está fuera de rango.")
            else:
                opcion_valida = True
        opcion = int(opcion_input)

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Ingrese su nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: la clave debe contener minimo 6 caracteres.")
                nueva_clave = input("Ingrese su nueva clave: ")

            confirmacion = input("Confirmar clave: ")
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar clave: ")
            print("Clave actualizada con exito.")

        elif opcion == 3:
            print("Los errores de hoy son los aprendizajes del futuro")

        elif opcion == 4:
            print("Hasta luego!")
            salir = True