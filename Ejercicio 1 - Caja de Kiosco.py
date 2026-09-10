# Ejercicio 1 - "Caja del Kiosco"

nombre = input("Ingrese el nombre del cliente: ")
while nombre == "" or not nombre.isalpha():
    print("Error: el nombre no puede estar vacio y solo puede contener letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad_input = input("Ingrese la cantidad de productos: ")
while not cantidad_input.isdigit() or int(cantidad_input) <= 0:
    print("Error: ingrese un numero entero mayor a 0.")
    cantidad_input = input("Ingrese la cantidad de productos: ")
cantidad = int(cantidad_input)

total_sin_descuento = 0
total_con_descuento = 0.0

for i in range(1, cantidad + 1):
    precio_input = input(f"Producto {i} - Precio: ")
    while not precio_input.isdigit():
        print("Error: el precio debe ser un numero entero.")
        precio_input = input(f"Producto {i} - Precio: ")
    precio = int(precio_input)

    descuento = input("Tiene descuento) (S/N): ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: responda S o N.")
        descuento = input("Tiene descuento? (S/N): ")

    total_sin_descuento += precio
    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.9
    else:
        precio_con_descuento = precio
    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")