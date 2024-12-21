#En esta sección seguiremos viendo if pero ahora aprenderemos
#sobre el codigo else y elif
#else sabemos que se usa para decirle al codigo que hacer 
#si el if no se cumple

#Haremos el siguiente programa:
print("verificacion de acceso")

edad_usuario=int(input("Introduce tu edad"))

if edad_usuario<18:
    print("NO puedes pasar")
else:
    print("Puedes pasar")

#Notemos que si ponemos 300 años se ejecutaría el else, pero debería decir algo
#como dato incorrecto
#Eso lo resolvemos usando elif
edad_usuario=int(input("Coloca tu edad 2.0"))
if edad_usuario<18:
    print("NO puedes pasar")
elif edad_usuario>100: #elif sirve para agregar una condición más al if incial
    print("Edad incorrecta")
else:
    print("Puedes pasar")

