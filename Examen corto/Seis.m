% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese el primer número
primer_numero = input("Ingrese el primer número: ");

% Solicitar al usuario que ingrese el segundo número
segundo_numero = input("Ingrese el segundo número: ");

% Determinar cuál es el número mayor
numero_mayor = max(primer_numero, segundo_numero);

% Mostrar la lista de números desde el mayor hasta el menor
fprintf("Lista de números desde el mayor hasta el menor:\n");
for i = numero_mayor:-1:min(primer_numero, segundo_numero)
    fprintf("%d\n", i);
end

% Insertar los números ingresados y el número mayor en la tabla "Seis" de la base de datos
try
    Ins1 = 'INSERT INTO Seis (Primer_Numero, Segundo_Numero, Numero_Mayor) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(primer_numero), ', ', num2str(segundo_numero), ', ', num2str(numero_mayor), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

