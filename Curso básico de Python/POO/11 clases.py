#Realizar un programa que conste de una clase llamada Estudiante, 
#que tenga como atributos el nombres, apellidos, edad y la nota del alumno. Definir 
#los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de 
#la nota y si ha aprobado o no. Si tiene nota arriba de 70 tiene el curso aprobado, si lo tiene debajo 
#de 70 esta reprobado.

class estudiante:
    def __init__(self,nombre,apellido,edad:int,nota,curso):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nota=nota
        self.curso=list()
    
    def atr(self):
        print("Su nombre es: ", self.nombre + " "+ self.apellido)
        print("su edad es: ", self.edad)
        print("Su nota es: ", self.nota)
        if self.nota>61:
            print("Has aprobado el curso")
        elif self.nota>100:
            print("La nota es incorrecta")
        else:
            print("Has reprobado el curso")


primer_estudiante= estudiante("Naydelin", "Ortiz", 21, 89)
primer_estudiante.atr()

#Al programa anterior, agregarle una estructura de datos que, a la hora de llamarla a traves 
#de un metodo, se agregue un curso nuevo sin borrar el anterior, así, cada vez que llame a ese método, 
#se agregará un curso nuevo en la cola con su respectiva nota.

