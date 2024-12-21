'''
El patrón singleton es un patron de diseño creacional
que garantiza que tan solo exista un objeto de su tipo 
y proporciona un único punto de acceso a él para cualquier 
otro código.
'''
class basededatos:
    _instancia = None

    def __new__(cls: type, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
            # Simulación de inicialización de la conexión a la base de datos
            cls._instancia.connect()
        return cls._instancia

    def connect(self: object):
        print("Conexión a la base de datos establecida")

    def add_user(self: object, user_info: dict):
        # Simulación de inserción de datos en la base de datos
        print("Añadiendo usuario:", user_info)

# Uso del Singleton
_connection1 = basededatos()
_connection2 = basededatos()

print(_connection1 is _connection2)  # nos devolverá el true

# Añadir un usuario utilizando la conexión a la base de datos
user_info = {"nombre": "Alice", "correo": "alice@example.com"}
_connection1.add_user(user_info)

