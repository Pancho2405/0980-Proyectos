% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Definir las opciones del menú
opciones = ["Agregar estudiante", "Editar estudiante", "Eliminar estudiante", "Salir"];

% Bucle principal
while true

  % Mostrar el menú
  fprintf("Seleccione una opción:\n");
  for i = 1:length(opciones)
    fprintf("%d. %s\n", i, opciones(i));
  end

  % Solicitar al usuario que ingrese una opción
  opcion = input("Opción: ");

  % Procesar la opción seleccionada
  switch opcion

    case 1
      % Agregar estudiante
      agregar_estudiante(conn);

    case 2
      % Editar estudiante
      editar_estudiante(conn);

    case 3
      % Eliminar estudiante
      eliminar_estudiante(conn);

    case 4
      % Salir
      break;

    default
      fprintf("Opción no válida.\n");

  end

end

% Cerrar la conexión con la base de datos
close(conn);

