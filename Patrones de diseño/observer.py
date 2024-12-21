#PATRON OBSERVER
class Observado:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

class Observador:
    def actualizar(self, mensaje):
        print("Mensaje recibido:", mensaje)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un objeto observado
    sujeto = Observado()

    # Creamos dos observadores
    observador1 = Observador()
    observador2 = Observador()

    # Los agregamos como observadores del sujeto
    sujeto.agregar_observador(observador1)
    sujeto.agregar_observador(observador2)

    # Notificamos a los observadores
    sujeto.notificar_observadores("¡Hola a todos!")
