import sqlite3
 
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
 
cursor.execute("SELECT id, username, email, nombre, apellidos, fecha_nacimiento FROM appFerre_usuario")
 
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(f"ID: {usuario[0]}")
    print(f"Nombre de usuario: {usuario[1]}")
    print(f"Email: {usuario[2]}")
    print(f"Nombre: {usuario[3]}")
    print(f"Apellidos: {usuario[4]}")
    print(f"Fecha de nacimiento: {usuario[5]}")
    print('-' * 40)
 
conn.close()
