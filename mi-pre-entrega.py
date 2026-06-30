def sistema_gestion():
    # Lista principal para almacenar los productos (sublistas)
    productos = []

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar producto")
        print("2. Visualizar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        # 1. AGREGAR PRODUCTOS
        if opcion == "1":
            while True:
                nombre = input("Nombre del producto: ").strip()
                if nombre: break
                print("Error: El nombre no puede estar vacío.")

            while True:
                categoria = input("Categoría: ").strip()
                if categoria: break
                print("Error: La categoría no puede estar vacía.")

            while True:
                precio_input = input("Precio (solo números enteros): ")
                if precio_input.isdigit():
                    precio = int(precio_input)
                    break
                print("Error: Ingrese un precio válido sin centavos.")

            # Almacenamos como sublista
            productos.append([nombre, categoria, precio])
            print(f"Producto '{nombre}' agregado con éxito.")

        # 2. VISUALIZAR PRODUCTOS
        elif opcion == "2":
            if not productos:
                print("\nNo hay productos registrados.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for i, prod in enumerate(productos, 1):
                    print(f"{i}. Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")

        # 3. BUSCAR PRODUCTOS
        elif opcion == "3":
            if not productos:
                print("\nNo hay productos para buscar.")
                continue
            
            busqueda = input("Ingrese el nombre del producto a buscar: ").lower()
            encontrados = []

            for prod in productos:
                if busqueda in prod[0].lower():
                    encontrados.append(prod)

            if encontrados:
                print("\n--- RESULTADOS ENCONTRADOS ---")
                for prod in encontrados:
                    print(f"Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
            else:
                print(f"No se encontraron coincidencias para '{busqueda}'.")

        # 4. ELIMINAR PRODUCTOS
        elif opcion == "4":
            if not productos:
                print("\nNo hay productos para eliminar.")
                continue
            
            # Reutilizamos la visualización para que el usuario sepa qué número elegir
            print("\n--- SELECCIONE EL NÚMERO A ELIMINAR ---")
            for i, prod in enumerate(productos, 1):
                print(f"{i}. {prod[0]}")
            
            try:
                indice = int(input("Ingrese el número de posición: ")) - 1
                if 0 <= indice < len(productos):
                    eliminado = productos.pop(indice)
                    print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                else:
                    print("Error: Posición fuera de rango.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        # 5. SALIR
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    sistema_gestion()