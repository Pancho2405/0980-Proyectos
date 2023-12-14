% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

try
    % Despliega el menú
    fprintf("Seleccione la figura para calcular el área:\n");
    fprintf("1. Circulo\n");
    fprintf("2. Triangulo\n");
    fprintf("3. Cuadrado\n");
    fprintf("4. Rectangulo\n");

    % Solicita la opción al usuario
    opcion = input("Ingrese el número de la figura: ");

    % Realiza el cálculo del área según la opción
    switch opcion
        case 1 % Circulo
            radio = input("Ingrese el radio del circulo: ");
            area = pi * radio^2;
            figura = 'Circulo';
        case 2 % Triangulo
            base = input("Ingrese la base del triangulo: ");
            altura = input("Ingrese la altura del triangulo: ");
            area = 0.5 * base * altura;
            figura = 'Triangulo';
        case 3 % Cuadrado
            lado = input("Ingrese el lado del cuadrado: ");
            area = lado^2;
            figura = 'Cuadrado';
        case 4 % Rectangulo
            base = input("Ingrese la base del rectangulo: ");
            altura = input("Ingrese la altura del rectangulo: ");
            area = base * altura;
            figura = 'Rectangulo';
        otherwise
            error("Opción no válida");
    end

    % Muestra el resultado del cálculo del área
    fprintf("El área del %s es: %.2f\n", figura, area);

    % Inserta los resultados en la tabla "Once" de la base de datos
    Ins1 = 'INSERT INTO Once (Opcion_Elegida, Figura, Area) VALUES (';
    Ins2 = ');';
    Instruccion = strcat(Ins1, num2str(opcion), ', ''', figura, ''', ', num2str(area), Ins2);
    Registro = pq_exec_params(conn, Instruccion);

catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

