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

def insert_student(connection, nombre, edad, genero, direccion):
    try:
        cursor = connection.cursor()
        insert_query = '''INSERT INTO estudiantes (nombre, edad, genero, direccion)
                          VALUES (%s, %s, %s, %s);'''
        data = (nombre, edad, genero, direccion)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        print("Estudiante agregado con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al agregar estudiante:", error)

def update_student(connection, estudiante_id, campo, nuevo_valor):
    try:
        cursor = connection.cursor()
        update_query = f'''UPDATE estudiantes
                           SET {campo} = %s
                           WHERE id = %s;'''
        data = (nuevo_valor, estudiante_id)
        cursor.execute(update_query, data)
        connection.commit()
        cursor.close()
        print("Información del estudiante actualizada con éxito.")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar información del estudiante:", error)

def delete_student(connection, estudiante_id):
    try:
        cursor = connection.cursor()
        delete_query = '''DELETE FROM estudiantes WHERE id = %s;'''
        cursor.execute(delete_query, (estudiante_id,))
        connection.commit()
        cursor.close()
        print("Estudiante eliminado de la base de datos.")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar estudiante:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Agregar estudiante")
            print("2. Editar información de estudiante")
            print("3. Eliminar estudiante")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del estudiante: ")
                edad = int(input("Edad: "))
                genero = input("Género: ")
                direccion = input("Dirección: ")
                insert_student(connection, nombre, edad, genero, direccion)
            elif opcion == "2":
                estudiante_id = int(input("ID del estudiante a editar: "))
                campo = input("Campo a editar (nombre/edad/genero/direccion): ")
                nuevo_valor = input(f"Nuevo valor para {campo}: ")
                update_student(connection, estudiante_id, campo, nuevo_valor)
            elif opcion == "3":
                estudiante_id = int(input("ID del estudiante a eliminar: "))
                delete_student(connection, estudiante_id)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        connection.close()

if __name__ == "__main__":
    main()
