% Cargar el paquete de base de datos
pkg load database

% Establecer la conexión con la base de datos PostgreSQL
conn = pq_connect(setdbopts('dbname', '0980 Proyectos', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', '2405'));

% Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra: ", 's');

% Inicializar contadores para cada vocal
contador_a = 0;
contador_e = 0;
contador_i = 0;
contador_o = 0;
contador_u = 0;

% Contar el número de veces que aparece cada vocal en la palabra
for letra = palabra_ingresada
    letra = lower(letra);
    switch letra
        case 'a'
            contador_a = contador_a + 1;
        case 'e'
            contador_e = contador_e + 1;
        case 'i'
            contador_i = contador_i + 1;
        case 'o'
            contador_o = contador_o + 1;
        case 'u'
            contador_u = contador_u + 1;
    end
end

% Mostrar el resultado en la consola
fprintf("A=%d, E=%d, I=%d, O=%d, U=%d.\n", contador_a, contador_e, contador_i, contador_o, contador_u);

% Insertar los resultados en la tabla "Siete" de la base de datos
try
    Ins1 = 'INSERT INTO Siete (Palabra, Letra_A, Letra_E, Letra_I, Letra_O, Letra_U) VALUES (''';
    Ins2 = ''', ';
    Ins3 = ');';
    Instruccion = strcat(Ins1, palabra_ingresada, Ins2, num2str(contador_a), ', ', num2str(contador_e), ', ', num2str(contador_i), ', ', num2str(contador_o), ', ', num2str(contador_u), Ins3);
    Registro = pq_exec_params(conn, Instruccion);
catch e
    disp(['Error durante la conexión a la DB, Consulte el error: ' e.message]);
end

% Cerrar la conexión con la base de datos
close(conn);

