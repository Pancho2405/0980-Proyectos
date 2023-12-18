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

def add_company(connection, nombre, direccion, telefono, ingresos_anuales, egresos_anuales):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO empresas (nombre, direccion, telefono, ingresos_anuales, egresos_anuales)
                          VALUES (%s, %s, %s, %s, %s);'''
        data = (nombre, direccion, telefono, ingresos_anuales, egresos_anuales)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Empresa agregada con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar empresa:", error)

def select_company(connection, nombre):
    try:
        cursor = connection.cursor()
        select_query = '''SELECT nombre, direccion, telefono, ingresos_anuales, egresos_anuales
                          FROM empresas
                          WHERE nombre = %s;'''
        data = (nombre,)
        cursor.execute(select_query, data)
        results = cursor.fetchall()
        cursor.close()

        if results:
            print("Empresa seleccionada:")
            for row in results:
                print(f"Nombre: {row[0]}, Dirección: {row[1]}, Teléfono: {row[2]}, Ingresos anuales: {row[3]}, Egresos anuales: {row[4]}")
        else:
            print("La empresa no existe.")
    except (Exception, psycopg2.Error) as error:
        print("Error al seleccionar empresa:", error)

def view_results(connection, nombre):
    try:
        cursor = connection.cursor()
        select_query = '''SELECT nombre, ingresos_anuales - egresos_anuales AS utilidad
                          FROM empresas
                          WHERE nombre = %s;'''
        data = (nombre,)
        cursor.execute(select_query, data)
        results = cursor.fetchall()
        cursor.close()

        if results:
            print("Resultados:")
            for row in results:
                print(f"Empresa: {row[0]}, Utilidad: {row[1]}")
        else:
            print("La empresa no existe.")
        return results
    except (Exception, psycopg2.Error) as error:
        print("Error al ver resultados:", error)

def close_connection(connection):
    try:
        connection.close()
        return None
    except (Exception, psycopg2.Error) as error:
        print("Error al cerrar la conexión:", error)
        return None
def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar empresa")
            print("2. Seleccionar empresa")
            print("2.1. Ver resultados")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre de la empresa: ")
                direccion = input("Dirección de la empresa: ")
                telefono = input("Teléfono de la empresa: ")
                ingresos_anuales = float(input("Ingresos anuales: "))
                egresos_anuales = float(input("Egresos anuales: "))
                add_company(connection, nombre, direccion, telefono, ingresos_anuales, egresos_anuales)
            elif opcion == "2":
                nombre = input("Nombre de la empresa: ")
                select_company(connection, nombre)
            elif opcion == "2.1":
                nombre = input("Nombre de la empresa: ")
                results = view_results(connection, nombre)
                for row in results:
                    print(f"Empresa: {row[0]}, Utilidad: {row[1]}")
            elif opcion == "3":
                print("Saliendo del programa.")
                connection.close()
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
    else:
        print("Error al conectar a la base de datos.")

if __name__ == "__main__":
    main()
