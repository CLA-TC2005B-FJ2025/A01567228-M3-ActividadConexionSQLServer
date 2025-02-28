import pymssql

# Configuración de la conexión
SERVER = "localhost"  # Cambia si te conectas desde fuera del Codespace
PORT = 1433
DATABASE = "master"
USERNAME = "sa"
PASSWORD = "YourPassword123!"

def get_connection():
    try:
        conn = pymssql.connect(server=SERVER, port=PORT, user=USERNAME, password=PASSWORD, database=DATABASE)
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def create(id, name, email):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Test (id, name, email) VALUES (%s, %s, %s)", (id, name, email))
            conn.commit()
            print(f" Registro insertado: ({id}, {name}, {email})")
        except Exception as e:
            print("Error al insertar:", e)
        finally:
            conn.close()

def read():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Test")
            records = cursor.fetchall()
            print(" Registros en la tabla Test:")
            for row in records:
                print(row)
        except Exception as e:
            print("Error al leer los registros:", e)
        finally:
            conn.close()

def update(id, new_name):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE Test SET name = %s WHERE id = %s", (new_name, id))
            conn.commit()
            print(f"Registro actualizado: ID {id} -> {new_name}")
        except Exception as e:
            print("Error al actualizar:", e)
        finally:
            conn.close()

def delete(id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Test WHERE id = %s", (id,))
            conn.commit()
            print(f"Registro eliminado: ID {id}")
        except Exception as e:
            print("Error al eliminar:", e)
        finally:
            conn.close()

def read_where_name(name):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Test WHERE name = %s", (name))
            records = cursor.fetchall()
            print(f"Resgistros de {name} en la tabla Test:")
            for row in records:
                print(row)
        except Exception as e:
            print(f"Error al buscar {name} nombre")
        finally:
            conn.close()

# Ejemplo de uso:
if __name__ == "__main__":
    create(3, "Mando", "pedroPascal@gmail.com")         # Crea un nuevo registro
    read()                     # Lee todos los registros
    update(3, "Mandalorian")   # Actualiza el registro con ID 3
    read()                     # Verifica la actualización
    delete(3)                  # Elimina el registro con ID 3
    read()                     # Verifica la eliminación
    create(3, "Mando", "pedroPascal@gmail.com")
    read_where_name("Mando")
