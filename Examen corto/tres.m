% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra: ", 's');

% Contar el número de vocales en la palabra
numero_vocales = sum(ismember(lower(palabra_ingresada), ['a', 'e', 'i', 'o', 'u']));

% Mostrar el resultado en la consola
fprintf("La palabra '%s' tiene %d vocales.\n", palabra_ingresada, numero_vocales);

% Insertar los resultados en la tabla "Tres" de la base de datos
try
    Ins1 = 'INSERT INTO Tres (Palabra_Ingresada, numero_vocales) VALUES (''';
    Ins2 = ''', ';
    Ins3 = ');';
    Instruccion = strcat(Ins1, palabra_ingresada, Ins2, num2str(numero_vocales), Ins3);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

