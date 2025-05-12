# LISTA DE DICCIONARIOS Y DUPLA:
lista = [
    {"nombre": "Pan",   "precio": 100, "cantidad": 20, "estado": ("Pan", "Disponible")},
    {"nombre": "Arroz", "precio": 200, "cantidad": 30, "estado": ("Arroz", "Disponible")},
    {"nombre": "Huevo", "precio": 50,  "cantidad": 100,"estado": ("Huevo", "Disponible")}
]


#DESCRIPCIÓN DE LA FUNCIÓN: AÑADIR PRODUCTO
'''
Inicia un bucle infinito para permitir el ingreso 
de múltiples productos hasta que el usuario decida salir. =>(break)
En este apartado, se inyectan las opciones de agregar al inventario el nombre, el precio y la cantidad
del producto. 
El valor ingresado se guarda como una cadena de texto (string) en la variable: Nombre, precio y cantidad
Posteriormente se hace la validación de que los datos que se ingresen seas los correctos para trabajar
con números positivos y decimales.
¿Cómo?: -replace(".", "", 1) quita el primer punto decimal (si existe) de la cadena.
        .isdigit() verifica si los caracteres restantes son solo dígitos.
        con una condicional if precio >0 and cantidad >0: se verifica que sea positivo.
        -De la misma forma se valida el estado del producto, si es resultado de las unidades presentes es igual a cero,
        el programa interpreta que NO está disponible y añade el estado a la dupla creadad desde un inicio.
        -Tiene validacíon de datos en caso tal de que no se cumplan las condicionales if//ELSE:
        -El programa cuenta con un operador ternario, que me ayuda a reducir lineas de código (lo vimos en clase)
        - .count() se usa para contar cuántas veces aparece un elemento específico en una secuencia, 

Se agreda un inventario con .append para almacenar los datos ingresados a un diccionario y añadir los datos 
a la lista de diccionarios y dupla.
'''
def añadir_productos():
    while True:
        nombre = input("Ingrese nombre del producto: ").lower()
        precio = input("Ingrese precio del producto: ")
        if precio.replace(".", "", 1).isdigit():
            precio = float(precio)
            cantidad = input("Ingrese la cantidad del producto: ")
            if cantidad.count(".") == 0 and cantidad.isdigit():
                cantidad = int(cantidad)
                if precio >= 0 and cantidad >= 0:
                    print("El producto se añadió correctamente.")
                    estado = "Disponible" if cantidad > 0 else "No disponible"
                    inventario = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad,
                        "estado": (nombre, estado)
                    }
                    lista.append(inventario)
                else:
                    print("Valor inválido.")
            else:
                print("Cantidad inválida.")
        else:
            print("Valor inválido.")

        continuar = input("¿DESEA AÑADIR MÁS PRODUCTOS? (s/n): ")
        if continuar.lower() != "s":
            break


#DESCRIPCIÓN DE LA FUNCIÓN: CONSULTAR PRODUCTOS:
'''
Verifica si la lista lista está vacía (not lista evalúa a True si está vacía).
Recorre cada producto i en la lista. mediante un for
Imprime los valores del producto usando una f-string (cadena formateada).


'''
def consultar_inventario():
    if not lista:
        print("Inventario vacío.")
    else:
        print("INVENTARIO:")
        for i in lista:
            print(f"Nombre: {i['nombre']}, Precio: {i['precio']}, Cantidad: {i['cantidad']}, Estado: {i['estado'][1]}")

# DESCRIPCIÓN DE LA FUNCIÓN: BUSCAR PRODUCTO:
'''
Compara el nombre ingresado con el nombre del producto de la lista, 
ambos en minúscula (.lower()) MEDIANTE el  for(i), condiciona medinate if el elemento igresado con la iteración en la lista


Hacemos uso de una bandera booleana (True / False) 
Se crea la bandera booleana llamada encontrado, que al principio se establece como False.
El cambio de estabandera a true depende si en la iteración del for se ha encontrado similitud con el elemento 
agregado. 

'''
def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ").lower()
    encontrado = False
    for i in lista:
        if nombre == i["nombre"].lower():
            print(f"Producto encontrado: Nombre: {i['nombre']}, Precio: {i['precio']}, Cantidad: {i['cantidad']}, Estado: {i['estado'][1]}")
            encontrado = True
            break
    if not encontrado:
        print(f"{nombre} no fue encontrado.")

# DESCRIPCIÓN DE LA FUNCIÓN: ACTUALIZAR PRODUCTOS:
'''
-while true:1
-ingreso de datos con el propósito de reemplazar/modificar.
-MICRO MENÚ: Navega entre las opciones del cambio del nombre, precio o cantidad de los elementos de la lista.
Esto permite actualizar varios productos uno tras otro, si el usuario lo desea.
Nuevamente se usa una bandera booleana false para determinar el estado de la busqueda. 
se condiciona y no se encuentra similitid, se activará el if not, validando que no se encontró 
el producto.
-Nuevamente hacemos uso del operador ternario para determinar el estado del producto. 
mediente un for si el producto ingresado coincide con la iteración, la bandera cambia a true 
lo que activa una ruta de navegación. (menú)
-CADA elemento actualizado debe de estar sometido a condiciones (int/float) mediante el .isdigit y el replace.
igualmente, los valores numéricos deben ser positivos. (elemento >0) como en la función añadir_producto ():


'''
def actualizar_productos():
    while True:
        producto_updt = input("Ingrese el nombre del producto que desea modificar: ").lower()
        encontrado = False

        for i in lista:
            if producto_updt == i["nombre"].lower():
                encontrado = True
                print("\n¿Qué deseas actualizar del producto?")
                print("1. Nombre")
                print("2. Precio")
                print("3. Cantidad")

                opcion = input("Elige una opción (1-2-3): ")

                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").lower()
                    i["nombre"] = nuevo_nombre
                    print("Nombre actualizado correctamente.\n")

                elif opcion == "2":
                    nuevo_precio = input("Ingrese el nuevo precio: ")
                    if nuevo_precio.replace(".", "", 1).isdigit():
                        nuevo_precio = float(nuevo_precio)
                        if nuevo_precio >0:
                            i["precio"] = nuevo_precio
                            print("Precio actualizado correctamente.\n")
                        else:
                            print("El precio debe ser mayor a 0.\n")
                    else:
                        print("Precio inválido.\n")

                elif opcion == "3":
                    nueva_cantidad = input("Ingrese la nueva cantidad: ")
                    if nueva_cantidad.isdigit():
                        nueva_cantidad = int(nueva_cantidad)
                        if nueva_cantidad >= 0:
                            i["cantidad"] = nueva_cantidad
                            i["estado"] = (i["nombre"], "Disponible" if nueva_cantidad > 0 else "No disponible")
                            print("Cantidad actualizada correctamente.\n")
                        else:
                            print("La cantidad debe ser mayor o igual a 0.\n")
                    else:
                        print("Cantidad inválida.\n")
                else:
                    print("Opción no válida.\n")
                break

        if not encontrado:
            print(f"El producto '{producto_updt}' no fue encontrado.\n")

        continuar = input("¿Deseas seguir actualizando productos? (s/n): ").lower()
        if continuar != "s":
            break

# DESCRIPCIÓN DE LA FUNCIÓN: ELIMINAR PRODUCTOS:
'''
La estructura del bloque consiste en la validación de la bandera booleana mediante el (if not) QUE DEPENDE 
DEL INGRESO DEL ELEMENTO SUINISTRADO EN EL (INPUT)
en el caso de que no se encuentre entre el elemento suministrado por el user y la iteración en la lista.
o directamente si hay similitud en la iteración se activa la bandera true 
mediante el (for) usando (metodos) como enumerate() te da el índice y el elemento a la vez, 
lo que facilita eliminar un elemento directamente de la lista con pop(index).
index= indice

'''
def elimar_productos():
    producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ").lower()
    encontrado = False

    for index, i in enumerate(lista):
        if producto_eliminar == i["nombre"].lower():
            lista.pop(index)
            print(f"El producto '{producto_eliminar}' ha sido eliminado correctamente.\n")
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{producto_eliminar}' no fue encontrado.\n")

# DESCRIPCIÓN: CALCULAR EL VALOR TOTAL DEL INVENTARIO.
'''
Inicialmente, definimos la variable calculo_total que contiene una función lambda, que nos permite dentro 
de ella, hacer una ecuación matemática, (multiplicación) entre el precio y el número de unidades que tiene el 
producto. 
-map (sirve para cambiar todos los elementos de una lista de la misma manera, sin tener que usar un bucle.)
map es básicamente hace sinergia con la función lambda para que lo haga con todos (i) los elemetos que hay dentro de la lista
de diccionarios
-se una sum para que SUME todo lo que hizo map en la lista, es decir, multiplica el precio por la cantidad de cada producto.
'''
def calculo_total():
    calculo_total = lambda nombre: nombre["precio"] * nombre["cantidad"]
    precios = map(calculo_total, lista)
    total = sum(precios)
    print(f"El valor total del inventario es: {total}")

# DESCRIPCIÓN DE LA FUNCIÓN MENÚ PRINCIPAL:
'''
While true para hacer posibile la navegación limitada por el usuario, es decir, 
acaba cuando el usuario lo desee (break) 
uso del match/case para mayor claridad y ahorro de código. 
contiene validación de opciones 
estructura simple. 

'''
def menu():
    while True:
        print("\n------- MENÚ -------")
        print("1. Añadir producto")
        print("2. Consultar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total del inventario")
        print("0. Salir")

        opcion = input("Elige una opción: ")
        match opcion:
            case "1":
                añadir_productos()
            case "2":
                consultar_inventario()
            case "3":
                buscar_producto()
            case "4":
                actualizar_productos()
            case "5":
                elimar_productos()
            case "6":
                calculo_total()
            case "0":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")

# Llamar al menú principal
menu()
