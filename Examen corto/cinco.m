% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese un número de inicio
inicio = input("Ingrese un número de inicio: ");

% Solicitar al usuario que ingrese un número de fin
fin = input("Ingrese un número de fin: ");

% Mostrar los números de dos en dos desde inicio hasta fin
fprintf("Números de dos en dos desde %d hasta %d:\n", inicio, fin);
for i = inicio:2:fin
    fprintf("%d\n", i);
end

% Insertar el número de inicio y el de fin en la tabla "Cinco" de la base de datos
try
    Ins1 = 'INSERT INTO Cinco (Inicio, Fin) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(inicio), ', ', num2str(fin), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

