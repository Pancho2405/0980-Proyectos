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

def show_all_songs(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM canciones"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        print("Listado de canciones:")
        for row in results:
            print(f"Artista: {row[0]}, Canción: {row[1]}")
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener canciones:", error)

def search_by_artist(connection, artist):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM canciones WHERE artista = '{artist}'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        if results:
            print(f"Canciones de {artist}:")
            for row in results:
                print(f"Canción: {row[1]}")
        else:
            print(f"No se encontraron canciones de {artist}")
    except (Exception, psycopg2.Error) as error:
        print("Error al buscar canciones por artista:", error)

def search_by_song(connection, song):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM canciones WHERE cancion = '{song}'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        if results:
            print(f"Canción {song}:")
            for row in results:
                print(f"Artista: {row[0]}")
        else:
            print(f"No se encontró la canción {song}")
    except (Exception, psycopg2.Error) as error:
        print("Error al buscar canciones por canción:", error)

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Desplegar el listado de canciones")
            print("2. Buscar por artista")
            print("3. Buscar por canción")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                show_all_songs(connection)
            elif opcion == "2":
                artista = input("Introduce el nombre del artista: ")
                search_by_artist(connection, artista)
            elif opcion == "3":
                cancion = input("Introduce el título de la canción: ")
                search_by_song(connection, cancion)
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

        connection.close()

if __name__ == "__main__":
    main()
