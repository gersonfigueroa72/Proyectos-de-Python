#empezamos definiendo las constantes
a_1=15.56
a_2=17.23
a_3=0.697
a_4=93.14
a_5=12
mp=938.271
me=0.511
mn=939.565
k=931.494 #valor de conversion (/) de Mev/c^2 a u
def f(Z,A):
    f_0=Z*(mp+me)+(A-Z)*mn
    f_1=-a_1*A
    f_2=a_2*A**(2/3)
    f_3=a_3*Z**2/A**(1/3)
    f_4=a_4*(Z-A/2)**2/A
    if Z%2==0 and (A-Z)%2==0:
        f_5=-a_5*A**(-1/2)
    elif Z%2!=0 and (A-Z)%2!=0:
        f_5=a_5*A**(-1/2)
    else:
        f_5=0
    
    return f_0+f_1+f_2+f_3+f_4+f_5

isotopo=f(int(input("Agregue Z ")),int(input("Agregue A ")))
print("la masa de su isotopo en Mev/c^2 es "+ str(isotopo))
print("la masa de su isotopo en u es ", float(isotopo)/k)

#la diferencia experimental es:
exp=None
dif=abs(isotopo/k-exp)
print("La diferencia experimental es: ", dif)

#La energia que se reparten las particulas finales será:
#(isotopopadre-isotoposhijos-menosparticulaslibres)k