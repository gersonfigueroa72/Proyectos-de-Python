'''En esta seccion empezaremos nuestro estudio
de clases, que es un tema de progra 
orientada a objetos (POO).
Una clase es como una plantilla que nos
permitirá crear varios objetos con ciertos 
atributos.
Ahora definiremos una clase la cual serán personajes
y nuestros objetos, serán nuevos personajes.

el __init__ es el constructor  (que es un método) que se ejecuta automáticamente 
cuando creas un nuevo objeto. Piénsalo como las instrucciones de ensamblaje:
'''
class peleador:
    def __init__(self, nombre, division, pais):
        self.nombre=nombre #atributos de la clase
        self.division=division
        self.pais=pais
#en esta parte definimos en el constructor los parametros
#que tendrá nuestra clase.
#Ahora dentro de la clase, haremos una nueva función (metodo llamado atributos),
#que nos permita saber el valor que le dimos a los diferentes
#atributos (parametros como nombre, pais...)
#como se encargará de mostrar los atributos, solo
#necesita el self para tener acceso a ellos.
    def atributos(self):
        print("El nombre del peleador es "+self.nombre)
        print("El pais del peleador es ", self.pais)
        print("La division del peleador es ", self.division)
#Quitando la identacion salimos de la clase

primer_peleador=peleador("Alexander Volkanovski", "145lb","Australia")
primer_peleador.atributos()
        
#Ahora haremos una clase que nos permita crear personajes
#estos tendran niveles de vida, fuerza, etc...

class personaje:
    def __init__(self,nickname,fuerza,inteligencia,defensa,vida):
        self.nickname=nickname
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
#con lo anterior definimos los atributos del objeto
#ahora definiremos los metodos:
    def datos(self):
        print("el nombre del personaje es ", self.nickname)
        print("fuerza",self.fuerza)
        print("inteligencia", self.inteligencia)
        print("defensa", self.defensa)
        print("vida", self.vida)

#Ahora vamos a crear un metodo para subirle el nivel 
#al personaje
    def subir_nivel(self,fuerza,inteligencia,defensa,vida):
        self.fuerza=self.fuerza+fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa
        self.vida=self.vida+vida
#ahora definiremos un personaje (objeto), con sus respectivos parametros
primer_personaje=personaje("Kevinator",100,100,100,100)
primer_personaje.datos()
#ahora le subiremos puntos de nivel
primer_personaje.subir_nivel(1,1,1,1)
#ahora que ya le subimos el nivel volvemos a llamar a los
#datos porque ya deberian estar actualizados
primer_personaje.datos()
