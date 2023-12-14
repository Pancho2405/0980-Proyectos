% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Solicitar al usuario ingresar 3 notas
    nota1 = input("Ingrese la primera nota: ");
    nota2 = input("Ingrese la segunda nota: ");
    nota3 = input("Ingrese la tercera nota: ");

    % Calcular el promedio
    promedio = (nota1 + nota2 + nota3) / 3;

    % Mostrar el promedio
    fprintf("El promedio es: %.2f\n", promedio);

    % Determinar si está aprobado o desaprobado
    mensaje = '';
    if promedio > 60
        mensaje = 'Aprobado';
    else
        mensaje = 'Desaprobado';
    end

    % Mostrar el mensaje
    fprintf("Mensaje: %s\n", mensaje);

    % Insertar los resultados en la tabla "Doce" de la base de datos
    Ins1 = 'INSERT INTO Doce (Primer_Nota, Segunda_Nota, Tercera_Nota, Promedio, Mensaje) VALUES (';
    Ins2 = strcat(num2str(nota1), ', ', num2str(nota2), ', ', num2str(nota3), ', ', num2str(promedio), ', ''', mensaje, ''');');
    Instruccion = strcat(Ins1, Ins2);
    Registro = pq_exec_params(conn, Instruccion);

catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

