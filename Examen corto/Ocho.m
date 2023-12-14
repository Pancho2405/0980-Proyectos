% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Mostrar todos los números impares del 1 al 100
    fprintf("Números impares del 1 al 100:\n");
    total_impares = 0;
    for num = 1:2:100
        fprintf("%d ", num);
        total_impares = total_impares + 1;
    end

    % Mostrar el total de números impares
    fprintf("\nEl total de números impares es: %d\n", total_impares);

    % Insertar el total de números impares en la tabla "Ocho" de la base de datos
    Ins1 = 'INSERT INTO Ocho (Total_numeros_impares) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(total_impares), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);
