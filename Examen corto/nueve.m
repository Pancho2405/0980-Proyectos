% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Solicitar al usuario que ingrese tres números enteros positivos
    lado1 = input("Ingrese el primer lado del triángulo: ");
    lado2 = input("Ingrese el segundo lado del triángulo: ");
    lado3 = input("Ingrese el tercer lado del triángulo: ");

    % Verificar el tipo de triángulo
    if lado1 == lado2 && lado2 == lado3
        tipo_triangulo = 'Equilátero';
    elseif lado1 == lado2 || lado2 == lado3 || lado1 == lado3
        tipo_triangulo = 'Isósceles';
    else
        tipo_triangulo = 'Escaleno';
    end

    % Mostrar el tipo de triángulo en la consola
    fprintf("El triángulo con lados %d, %d y %d es %s.\n", lado1, lado2, lado3, tipo_triangulo);

    % Insertar los resultados en la tabla "Nueve" de la base de datos
    Ins1 = 'INSERT INTO Nueve (Primer_Lado, Segundo_Lado, Tercer_Lado, Tipo_De_Triangulo) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(lado1), ', ', num2str(lado2), ', ', num2str(lado3), ', ''', tipo_triangulo, '''', Ins2);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

