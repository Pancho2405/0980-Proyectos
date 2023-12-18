def main():
    connection = connect_to_database(peliculas)
    if connection:
        while True:
            print("\nOpciones:")
            print("1. Ingresar género")
            print("2. Ingresar calificación")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                genre = input("Ingresa el género que deseas ver: ")
            elif opcion == "2":
                global rating
                rating = input("Ingresa la calificación que deseas (de 1 a 5): ")
            elif opcion == "3":
                print("Saliendo del programa.")
                close_connection(connection)
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

            recommended_movies = view_recommended_movie(connection, genre, rating)
            if recommended_movies:
                print("Las películas recomendadas son:")
                for movie in recommended_movies:
                    if movie:
                        print(movie)
                    else:
                        print("No se encontraron resultados que coincidan con los criterios.")
            else:
                print("No se encontraron resultados que coincidan con los criterios.")
    else:
        print("Error al conectar a la base de datos.")

if __name__ == "__main__":
    main()
