import sqlite3

from colorama import init, Fore, Style



# Inicializar colorama para compatibilidad multiplataforma

init(autoreset=True)



DB_NAME = 'inventario.db'



def conectar_db():

    """Establece la conexión con la base de datos SQLite."""

    return sqlite3.connect(DB_NAME)



def inicializar_db():

    """Crea la tabla 'productos' si no existe en la base de datos."""

    conexion = conectar_db()

    cursor = conexion.cursor()

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS productos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            descripcion TEXT,

            cantidad INTEGER NOT NULL,

            precio REAL NOT NULL,

            categoria TEXT

        )

    ''')

    conexion.commit()

    conexion.close()



# ==========================================

# FUNCIONALIDADES DE LA APLICACIÓN

# ==========================================



def registrar_producto():

    """Permite al usuario ingresar un nuevo producto al inventario."""

    print(Fore.CYAN + "\n--- Registrar Nuevo Producto ---")

    

    # Validaciones básicas de entrada de datos

    nombre = input("Nombre del producto (Obligatorio): ").strip()

    if not nombre:

        print(Fore.RED + "Error: El nombre no puede estar vacío.")

        return

        

    descripcion = input("Descripción: ").strip()

    

    try:

        cantidad = int(input("Cantidad: "))

        precio = float(input("Precio: "))

    except ValueError:

        print(Fore.RED + "Error: Cantidad debe ser entero y Precio debe ser un número decimal/entero.")

        return

        

    categoria = input("Categoría: ").strip()



    # Inserción en la base de datos

    conexion = conectar_db()

    cursor = conexion.cursor()

    cursor.execute('''

        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)

        VALUES (?, ?, ?, ?, ?)

    ''', (nombre, descripcion, cantidad, precio, categoria))

    

    conexion.commit()

    print(Fore.GREEN + f"\n[✔] Producto '{nombre}' registrado exitosamente con el ID: {cursor.lastrowid}")

    conexion.close()





def visualizar_productos(productos=None):

    """Muestra una lista de productos en formato de tabla. 

    Si no recibe una lista, consulta todos los productos."""

    conexion = conectar_db()

    cursor = conexion.cursor()

    

    if productos is None:

        cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()

    

    conexion.close()



    if not productos:

        print(Fore.YELLOW + "\n[!] No se encontraron productos registrados.")

        return



    # Encabezado de la tabla formateado

    print(Fore.BLUE + "\n" + "="*85)

    print(f"{'ID':<5} | {'Nombre':<20} | {'Categoría':<15} | {'Cant.':<6} | {'Precio':<10} | {'Descripción':<20}")

    print(Fore.BLUE + "="*85)

    

    # Filas de la tabla

    for prod in productos:

        print(f"{prod[0]:<5} | {prod[1]:<20} | {prod[5] or 'N/A':<15} | {prod[3]:<6} | ${prod[4]:<9.2f} | {prod[2] or '':<20}")

    print(Fore.BLUE + "="*85 + "\n")





def actualizar_producto():

    """Actualiza los datos de un producto existente mediante su ID."""

    print(Fore.CYAN + "\n--- Actualizar Producto ---")

    try:

        id_prod = int(input("Ingrese el ID del producto a modificar: "))

    except ValueError:

        print(Fore.RED + "ID inválido.")

        return



    conexion = conectar_db()

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))

    producto = cursor.fetchone()



    if not producto:

        print(Fore.RED + f"No se encontró ningún producto con el ID {id_prod}.")

        conexion.close()

        return



    print(Fore.YELLOW + f"\nProducto encontrado: {producto[1]} (Categoría: {producto[5]})")

    print("Deje en blanco el campo si no desea modificarlo.")



    # Solicitar nuevos valores (si se deja en blanco, se mantiene el actual)

    nombre = input(f"Nuevo Nombre [{producto[1]}]: ").strip() or producto[1]

    descripcion = input(f"Nueva Descripción [{producto[2]}]: ").strip() or producto[2]

    

    cantidad_inp = input(f"Nueva Cantidad [{producto[3]}]: ").strip()

    cantidad = int(cantidad_inp) if cantidad_inp else producto[3]

    

    precio_inp = input(f"Nuevo Precio [{producto[4]}]: ").strip()

    precio = float(precio_inp) if precio_inp else producto[4]

    

    categoria = input(f"Nueva Categoría [{producto[5]}]: ").strip() or producto[5]



    # Ejecutar la actualización

    cursor.execute('''

        UPDATE productos 

        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?

        WHERE id = ?

    ''', (nombre, descripcion, cantidad, precio, categoria, id_prod))

    

    conexion.commit()

    print(Fore.GREEN + f"\n[✔] Producto con ID {id_prod} actualizado correctamente.")

    conexion.close()





def eliminar_producto():

    """Elimina un producto de la base de datos por su ID."""

    print(Fore.CYAN + "\n--- Eliminar Producto ---")

    try:

        id_prod = int(input("Ingrese el ID del producto que desea eliminar: "))

    except ValueError:

        print(Fore.RED + "ID inválido.")

        return



    conexion = conectar_db()

    cursor = conexion.cursor()

    

    # Verificar existencia

    cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_prod,))

    producto = cursor.fetchone()



    if not producto:

        print(Fore.RED + f"No existe un producto con el ID {id_prod}.")

        conexion.close()

        return



    # Confirmación de seguridad

    confirmar = input(Fore.YELLOW + f"¿Seguro que desea eliminar '{producto[0]}' del inventario? (s/n): ").lower()

    if confirmar == 's':

        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,)) # Para el reporte visual

        cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))

        conexion.commit()

        print(Fore.GREEN + f"\n[✔] Producto eliminado exitosamente.")

    else:

        print(Fore.YELLOW + "\nOperación cancelada.")

        

    conexion.close()





def buscar_producto():

    """Busca productos por ID, Nombre o Categoría."""

    print(Fore.CYAN + "\n--- Buscar Producto ---")

    print("1. Buscar por ID")

    print("2. Buscar por Nombre")

    print("3. Buscar por Categoría")

    opcion = input("Seleccione criterio de búsqueda (1-3): ").strip()



    conexion = conectar_db()

    cursor = conexion.cursor()

    resultados = []



    if opcion == '1':

        try:

            id_prod = int(input("Ingrese el ID del producto: "))

            cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))

            res = cursor.fetchone()

            if res: resultados.append(res)

        except ValueError:

            print(Fore.RED + "ID inválido.")

            conexion.close()

            return

    elif opcion == '2':

        nombre = input("Ingrese el nombre (o parte de él): ").strip()

        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))

        resultados = cursor.fetchall()

    elif opcion == '3':

        categoria = input("Ingrese la categoría (o parte de ella): ").strip()

        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{categoria}%",))

        resultados = cursor.fetchall()

    else:

        print(Fore.RED + "Opción inválida.")

        conexion.close()

        return



    conexion.close()

    visualizar_productos(resultados)





def reporte_stock_bajo():

    """Muestra los productos que tengan un stock igual o inferior al límite dado."""

    print(Fore.CYAN + "\n--- Reporte de Stock Bajo ---")

    try:

        limite = int(input("Defina el límite de alerta de cantidad: "))

    except ValueError:

        print(Fore.RED + "Error: Debe ingresar un número entero.")

        return



    conexion = conectar_db()

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))

    resultados = cursor.fetchall()

    conexion.close()



    print(Fore.YELLOW + f"\nResultados con stock menor o igual a: {limite}")

    visualizar_productos(resultados)





# ==========================================

# INTERFAZ DE USUARIO (MENÚ PRINCIPAL)

# ==========================================



def menu_principal():

    """Inicia la interfaz de línea de comandos en bucle."""

    inicializar_db()

    

    while True:

        print(Fore.MAGENTA + "\n=========================================")

        print(Fore.MAGENTA + "       SISTEMA DE GESTIÓN DE INVENTARIO   ")

        print(Fore.MAGENTA + "=========================================")

        print("1. Registrar Producto")

        print("2. Visualizar Productos")

        print("3. Actualizar Producto")

        print("4. Eliminar Producto")

        print("5. Buscar Producto")

        print("6. Reporte de Alerta de Stock Bajo")

        print(Fore.RED + "7. Salir")

        print(Fore.MAGENTA + "-----------------------------------------")

        

        opcion = input("Seleccione una opción (1-7): ").strip()



        if opcion == '1':

            registrar_producto()

        elif opcion == '2':

            visualizar_productos()

        elif opcion == '3':

            actualizar_producto()

        elif opcion == '4':

            eliminar_producto()

        elif opcion == '5':

            buscar_producto()

        elif opcion == '6':

            reporte_stock_bajo()

        elif opcion == '7':

            print(Fore.GREEN + "\n¡Gracias por utilizar el sistema de inventario! Saliendo...")

            break

        else:

            print(Fore.RED + "\n[!] Opción no válida. Por favor, intente de nuevo.")





if __name__ == '__main__':

    menu_principal()