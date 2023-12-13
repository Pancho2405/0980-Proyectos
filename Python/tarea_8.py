import psycopg2 
conn = psycopg2.connect(
    dbname= '0980 Proyectos',
    user = 'postgres',
    password = '2405',
    host = 'localhost',
    port = '5433'
)
cur = conn.cursor()
precio = float(input("Ingrese el precio del producto: Q"))
Iva = precio*0.12
precio_sin_iva = precio - Iva
print(f"el precion sin iva es {precio_sin_iva: .0f}, el iva es de Q{Iva: .0f}")
try:
    Ins1 = 'insert into codigo (precio) VALUES (%s);'
    instruccion = cur.mogrify(Ins1, (precio,))
    cur.execute(instruccion)
    conn.commit ()
except psycopg2.Error as e:
    print(f"Error durante la conexion a la base de datos. consulte el error {e}")
finally:
    cur.close()
    conn.close()
