% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Solicitar al usuario que ingrese el modelo del auto y el kilometraje
    modelo_auto = input("Ingrese el modelo del auto (año): ");
    kilometraje_auto = input("Ingrese el kilometraje del auto en km: ");

    % Calcular el diagnóstico según las condiciones especificadas
    if modelo_auto < 2007 && kilometraje_auto > 20000.0
        diagnostico = "Renovarse";
    elseif modelo_auto >= 2007 && modelo_auto <= 2013 && kilometraje_auto > 20000
        diagnostico = "Debe recibir mantenimiento";
    elseif modelo_auto > 2013 && kilometraje_auto < 10000
        diagnostico = "En óptimas condiciones";
    else
        diagnostico = "Mecánico";
    end

    % Mostrar el diagnóstico en la consola
    fprintf("El diagnóstico del carro es: %s\n", diagnostico);

    % Insertar los resultados en la tabla "Catorce" de la base de datos
    Instruccion = sprintf("INSERT INTO Catorce (modelo, kilometraje_recorrido, diagnostico) VALUES (%d, %f, '%s');", modelo_auto, kilometraje_auto, diagnostico);
    Registro = pq_exec_params(conn, Instruccion);

catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

