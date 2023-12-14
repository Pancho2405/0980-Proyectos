% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese un número
numero_ingresado = input("Ingrese un número: ");

% Calcular la suma de los números desde 0 hasta el número ingresado
resultado_suma = sum(0:numero_ingresado);

% Mostrar el resultado de la suma en la consola
fprintf("La suma de los números desde 0 hasta %d es: %d\n", numero_ingresado, resultado_suma);

% Insertar el número ingresado y el resultado de la suma en la tabla "Cuatro" de la base de datos
try
    Ins1 = 'INSERT INTO Cuatro (Numero_Ingresado, Resultado_Suma) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(numero_ingresado), ', ', num2str(resultado_suma), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

