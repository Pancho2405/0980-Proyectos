% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Solicitar al usuario que ingrese tres números
    primer_numero = input("Ingrese el primer número: ");
    segundo_numero = input("Ingrese el segundo número: ");
    tercer_numero = input("Ingrese el tercer número: ");

    % Verificar y realizar las operaciones según las condiciones especificadas
    if primer_numero > segundo_numero && primer_numero > tercer_numero
        resultado = primer_numero + segundo_numero + tercer_numero;
        fprintf("El resultado es la suma de los tres números: %d\n", resultado);
    elseif segundo_numero > primer_numero && segundo_numero > tercer_numero
        resultado = primer_numero * segundo_numero * tercer_numero;
        fprintf("El resultado es la multiplicación de los tres números: %d\n", resultado);
    elseif tercer_numero > primer_numero && tercer_numero > segundo_numero
        resultado = strcat(num2str(primer_numero), num2str(segundo_numero), num2str(tercer_numero));
        fprintf("El resultado es la concatenación de los tres números: %s\n", resultado);
    elseif primer_numero == segundo_numero
        fprintf("El número diferente es: %d\n", tercer_numero);
    elseif primer_numero == tercer_numero
        fprintf("El número diferente es: %d\n", segundo_numero);
    elseif segundo_numero == tercer_numero
        fprintf("El número diferente es: %d\n", primer_numero);
    else
        fprintf("Todos los números son iguales: %d\n", primer_numero);
    end

    % Insertar los resultados en la tabla "Uno" de la base de datos
    Ins1 = 'INSERT INTO Uno (Primer_Numero, Segundo_Numero, Tercer_Numero) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(primer_numero), ', ', num2str(segundo_numero), ', ', num2str(tercer_numero), Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

