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

def add_product(connection, producto, cantidad, precio):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO inventario (producto, cantidad, precio)
                          VALUES (%s, %s, %s);'''
        data = (producto, cantidad, precio)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Producto agregado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar producto:", error)

def update_product_quantity(connection, producto, cantidad):
    try:
        cursor = connection.cursor()
        update_query = '''UPDATE inventario
                          SET cantidad = %s
                          WHERE producto = %s;'''
        data = (cantidad, producto)
        cursor.execute(update_query, data)
        connection.commit()
        cursor.close()
        print("Cantidad de producto actualizada con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar cantidad de producto:", error)

def delete_product(connection, producto):
    try:
        cursor = connection.cursor()
        delete_query = '''DELETE FROM inventario
                          WHERE producto = %s;'''
        data = (producto,)
        cursor.execute(delete_query, data)
        connection.commit()
        cursor.close()
        print("Producto eliminado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar producto:", error)

def generate_sales_report(connection):
    try:
        cursor = connection.cursor()
        report_query = '''SELECT  producto, cantidad, precio
                          FROM inventario
                          ORDER BY fecha DESC;'''
        cursor.execute(report_query)
        results = cursor.fetchall()
        cursor.close()

        print("Reporte de ventas:")
        for row in results:
            print(f" Producto: {row[1]}, Cantidad: {row[2]}, Precio: {row[3]}")
    except (Exception, psycopg2.Error) as error:
        print("Error al generar reporte:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar producto")
            print("2. Actualizar cantidad de producto")
            print("3. Eliminar producto")
            print("4. Generar informe de ventas")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                producto = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                add_product(connection, producto, cantidad, precio)
            elif opcion == "2":
                producto = input("Nombre del producto: ")
                cantidad = int(input("Cantidad nueva: "))
                update_product_quantity(connection, producto, cantidad)
            elif opcion == "3":
                producto = input("Nombre del producto: ")
                delete_product(connection, producto)
            elif opcion == "4":
                generate_sales_report(connection)
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
