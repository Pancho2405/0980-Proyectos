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

def insert_expense(connection, fecha, categoria, descripcion, monto):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO gastos (fecha, categoria, descripcion, monto)
                          VALUES (%s, %s, %s, %s);'''
        data = (fecha, categoria, descripcion, monto)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Gasto agregado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar gasto:", error)

def generate_report(connection):
    try:
        cursor = connection.cursor()
        report_query = '''SELECT fecha, categoria, descripcion, monto
                         FROM gastos
                         ORDER BY fecha DESC;'''
        cursor.execute(report_query)
        results = cursor.fetchall()
        cursor.close()
        print("Reporte de gastos:")
        for row in results:
            print(f"Fecha: {row[0]}, Categoría: {row[1]}, Descripción: {row[2]}, Monto: {row[3]}")
    except (Exception, psycopg2.Error) as error:
        print("Error al generar reporte:", error)

def adjust_budget(connection, categoria, nuevo_monto):
    try:
        cursor = connection.cursor()
        update_query = f'''UPDATE presupuestos
                           SET monto = %s
                           WHERE categoria = %s;'''
        data = (nuevo_monto, categoria)
        cursor.execute(update_query, data)
        connection.commit()
        cursor.close()
        print("Presupuesto ajustado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al ajustar presupuesto:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar gasto")
            print("2. Ver informe de gastos")
            print("3. Ajustar presupuesto")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                fecha = input("Fecha del gasto (YYYY-MM-DD): ")
                categoria = input("Categoría del gasto: ")
                descripcion = input("Descripción del gasto: ")
                monto = float(input("Monto del gasto: "))
                insert_expense(connection, fecha, categoria, descripcion, monto)
            elif opcion == "2":
                generate_report(connection)
            elif opcion == "3":
                categoria = input("Categoría del presupuesto a ajustar: ")
                nuevo_monto = float(input("Nuevo monto del presupuesto: "))
                adjust_budget(connection, categoria, nuevo_monto)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        connection.close()

if __name__ == "__main__":
    main()
