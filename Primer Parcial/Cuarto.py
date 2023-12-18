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

def insert_sale(connection, fecha, producto, cantidad, precio):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO pedidos (fecha, producto, cantidad, precio)
                          VALUES (%s, %s, %s, %s);'''
        data = (fecha, producto, cantidad, precio)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Pedido agregado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar pedido:", error)

def edit_sale(connection, id, fecha, producto, cantidad, precio):
    try:
        cursor = connection.cursor()
        update_query = '''UPDATE pedidos
                          SET fecha = %s,
                              producto = %s,
                              cantidad = %s,
                              precio = %s
                          WHERE id = %s;'''
        data = (fecha, producto, cantidad, precio, id)
        cursor.execute(update_query, data)
        connection.commit()
        cursor.close()
        print("Pedido editado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al editar pedido:", error)

def delete_sale(connection, id):
    try:
        cursor = connection.cursor()
        delete_query = '''DELETE FROM pedidos
                          WHERE id = %s;'''
        data = (id,)
        cursor.execute(delete_query, data)
        connection.commit()
        cursor.close()
        print("Pedido eliminado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar pedido:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar pedido")
            print("2. Editar pedido")
            print("3. Eliminar pedido")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                fecha = input("Fecha del pedido (YYYY-MM-DD): ")
                producto = input("Producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                insert_sale(connection, fecha, producto, cantidad, precio)
            elif opcion == "2":
                id = input("ID del pedido a editar: ")
                fecha = input("Fecha nueva del pedido (YYYY-MM-DD): ")
                producto = input("Producto nuevo: ")
                cantidad = int(input("Cantidad nueva: "))
                precio = float(input("Precio nuevo: "))
                edit_sale(connection, id, fecha, producto, cantidad, precio)
            elif opcion == "3":
                id = input("ID del pedido a eliminar: ")
                delete_sale(connection, id)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
