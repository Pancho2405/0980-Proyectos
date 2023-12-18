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

def close_connection(connection):
    try:
        connection.close()
        return None
    except (Exception, psycopg2.Error) as error:
        print("Error al cerrar la conexión:", error)
        return None

def view_sensor_results_graph(connection, sensor):
    import matplotlib.pyplot as plt

    try:
        cursor = connection.cursor()
        select_query = '''SELECT calidad, precio
                          FROM sensores
                          WHERE sensor = %s;'''
        data = (sensor,)
        cursor.execute(select_query, data)
        results = cursor.fetchall()
        cursor.close()

        if results:
            calidad = [row[0] for row in results]
            precio = [row[1] for row in results]
            plt.plot(calidad, precio, linewidth=2)
            plt.xlabel("Calidad")
            plt.ylabel("Precio")
            plt.title("Gráfica de calidad-precio de los sensores")
            plt.show()
        else:
            print("El sensor no existe.")
    except (Exception, psycopg2.Error) as error:
        print("Error al ver resultados del sensor:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar sensor")
            print("2. Editar sensor")
            print("3. Ver resultados del sensor")
            print("4. Ver resultados del sensor en gráfica")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                sensor = input("Nombre del sensor: ")
                calidad = input("Calidad del sensor: ")
                precio = float(input("Precio del sensor: "))
                add_sensor(connection, sensor, calidad, precio)
            elif opcion == "2":
                sensor = input("Nombre del sensor: ")
                calidad = input("Calidad del sensor: ")
                precio = float(input("Precio del sensor: "))
                edit_sensor(connection, sensor, calidad, precio)
            elif opcion == "3":
                sensor = input("Nombre del sensor: ")
                view_sensor_results(connection, sensor)
            elif opcion == "4":
                sensor = input("Nombre del sensor: ")
                view_sensor_results_graph(connection, sensor)
            elif opcion == "5":
                print("Saliendo del programa.")
                close_connection(connection)
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
    else:
        print("Error al conectar a la base de datos.")

if __name__ == "__main__":
    main()
    
