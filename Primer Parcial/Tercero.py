import psycopg2

def connect_to_database():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="2405",
            host="localhost",
            port="5433",
            database="0980 Proyectos"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

def insert_product(connection, nombre, precio, cantidad):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO productos (nombre, precio, cantidad)
                          VALUES (%s, %s, %s);'''
        data = (nombre, precio, cantidad)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Producto agregado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar producto:", error)

def update_product(connection, producto_id, campo, nuevo_valor):
    try:
        cursor = connection.cursor()
        update_query = f'''UPDATE productos
                          SET {campo} = %s
                          WHERE id = %s;'''
        data = (nuevo_valor, producto_id)
        cursor.execute(update_query, data)
        connection.commit()
        cursor.close()
        print("Información del producto actualizada con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar información del producto:", error)

def delete_product(connection, producto_id):
    try:
        cursor = connection.cursor()
        delete_query = '''DELETE FROM productos WHERE id = %s;'''
        cursor.execute(delete_query, (producto_id,))
        connection.commit()
        cursor.close()
        print("Producto eliminado de la base de datos.")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar producto:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar producto")
            print("2. Actualizar información de producto")
            print("3. Eliminar producto")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                insert_product(connection, nombre, precio, cantidad)
            elif opcion == "2":
                producto_id = int(input("ID del producto a editar: "))
                campo = input("Campo a editar (nombre/precio/cantidad): ")
                nuevo_valor = input(f"Nuevo valor para {campo}: ")
                update_product(connection, producto_id, campo, nuevo_valor)
            elif opcion == "3":
                producto_id = int(input("ID del producto a eliminar: "))
                delete_product(connection, producto_id)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
