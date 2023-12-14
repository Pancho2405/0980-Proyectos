% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Solicitar al usuario que ingrese un número
    numero_ingresado = input("Ingrese un número: ");

    % Verificar si el número es divisible por 7
    if mod(numero_ingresado, 7) == 0
        % Calcular el factorial del número
        factorial_resultado = factorial(numero_ingresado);
        fprintf("El factorial de %d es %d.\n", numero_ingresado, factorial_resultado);
        resultado_mensaje = num2str(factorial_resultado);
    else
        % Mostrar mensaje de número incorrecto
        disp("Número incorrecto.");
        resultado_mensaje = "Número incorrecto";
    end

    % Insertar los resultados en la tabla "Diez" de la base de datos
    Ins1 = 'INSERT INTO Diez (Numero_Ingresado, Resultado) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(numero_ingresado), ', ''', resultado_mensaje, '''', Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

