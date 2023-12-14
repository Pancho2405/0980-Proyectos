% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese un número entero
numero_ingresado = input("Ingrese un número entero: ");

% Calcular los divisores del número ingresado
divisores = find(mod(numero_ingresado, 1:numero_ingresado) == 0);

% Mostrar los divisores en la consola
fprintf("Los divisores de %d son: %s\n", numero_ingresado, num2str(divisores));

% Contar los divisores en total
total_divisores = numel(divisores);

% Mostrar el número total de divisores
fprintf("El número total de divisores de %d es: %d\n", numero_ingresado, total_divisores);

% Insertar el número ingresado y el total de divisores en la tabla "Dos" de la base de datos
try
    Ins1 = 'INSERT INTO Dos (numero_ingresado, Total_de_Divisores) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(numero_ingresado), ', ', num2str(total_divisores), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

