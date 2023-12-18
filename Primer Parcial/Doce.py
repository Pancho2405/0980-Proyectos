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

def show_all_questions(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT pregunta, respuesta FROM futbol"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        print("Listado de preguntas:")
        for row in results:
            print(f"Pregunta: {row[0]}, Respuesta: {row[1]}")
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener preguntas:", error)

def generate_random_question(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT pregunta, respuesta FROM futbol ORDER BY random() LIMIT 1"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        if results:
            return results[0]
        else:
            return None
    except (Exception, psycopg2.Error) as error:
        print("Error al generar pregunta aleatoria:", error)
        return None

def play_game(connection):
    lives = 3
    points = 0

    while lives > 0:
        question = generate_random_question(connection)
        print(question[0])
        answer = input("Tu respuesta: ")

        if answer == question[1]:
            points += 1
            print("¡Correcto! Ganaste 1 punto.")
        else:
            lives -= 1
            print("¡Incorrecto! Perdiste una vida.")

        if lives == 0:
            print("Has perdido el juego.")
            break

        print("Tu puntuación actual es:", points)

    print("Has ganado", points, "puntos.")

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Jugar")
            print("2. Ver preguntas")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                play_game(connection)
            elif opcion == "2":
                show_all_questions(connection)
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
