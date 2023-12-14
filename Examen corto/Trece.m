% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese su año de nacimiento
ano_nacimiento = input("Ingrese su año de nacimiento: ");

% Verificar si el año ingresado es bisiesto
if mod(ano_nacimiento, 4) == 0 && (mod(ano_nacimiento, 100) ~= 0 || mod(ano_nacimiento, 400) == 0)
    mensaje = "El año es bisiesto.";
else
    mensaje = "El año no es bisiesto.";
end

% Mostrar el resultado en la consola
fprintf('%s\n', mensaje);

% Insertar los resultados en la tabla "Trece" de la base de datos
try
    Ins1 = 'INSERT INTO Trece (Año_Ingresado, Tipo_De_año) VALUES (';
    Ins2 = ', ''';
    Ins3 = ''');';
    Instruccion = strcat(Ins1, num2str(ano_nacimiento), Ins2, mensaje, Ins3);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

