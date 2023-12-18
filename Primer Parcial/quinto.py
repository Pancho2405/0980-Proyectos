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
        insert_query = '''INSERT INTO ventas (fecha, producto, cantidad, precio)
                          VALUES (%s, %s, %s, %s);'''
        data = (fecha, producto, cantidad, precio)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Venta agregada con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar venta:", error)

def generate_report(connection):
    try:
        cursor = connection.cursor()
        report_query = '''SELECT fecha, producto, cantidad, precio
                          FROM ventas
                          ORDER BY fecha DESC;'''
        cursor.execute(report_query)
        results = cursor.fetchall()
        cursor.close()

        print("Reporte de ventas:")
        for row in results:
            print(f"Fecha: {row[0]}, Producto: {row[1]}, Cantidad: {row[2]}, Precio: {row[3]}")
    except (Exception, psycopg2.Error) as error:
        print("Error al generar reporte:", error)

def analyze_data(connection):
    try:
        cursor = connection.cursor()
        analysis_query = '''SELECT producto, SUM(cantidad) AS cantidad, SUM(precio) AS precio
                          FROM ventas
                          GROUP BY producto;'''
        cursor.execute(analysis_query)
        results = cursor.fetchall()
        cursor.close()

        for row in results:
            print(f"Producto: {row[0]}, Cantidad: {row[1]}, Precio: {row[2]}")

        print("Patrones y tendencias:")
        # Aquí puedes agregar tu código para analizar los datos y encontrar patrones y tendencias.
        # Por ejemplo, puedes calcular el crecimiento de las ventas, el producto más vendido, etc.
    except (Exception, psycopg2.Error) as error:
        print("Error al analizar datos:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar venta")
            print("2. Generar reporte")
            print("3. Analizar datos")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                fecha = input("Fecha de la venta (YYYY-MM-DD): ")
                producto = input("Producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                insert_sale(connection, fecha, producto, cantidad, precio)
            elif opcion == "2":
                generate_report(connection)
            elif opcion == "3":
                analyze_data(connection)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
