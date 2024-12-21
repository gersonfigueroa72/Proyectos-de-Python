import calendar

def imprimir_calendario_semanal(anio):
    cal = calendar.Calendar()
    meses = list(calendar.month_name)

    for mes in range(1, 13):
        print(f"\n{meses[mes]} {anio}\n")
        semanas = cal.monthdayscalendar(anio, mes)
        print("Lun Mar Mié Jue Vie Sáb Dom")
        for semana in semanas:
            for dia in semana:
                if dia == 0:
                    print("   ", end=" ")  # Día vacío
                else:
                    print(f"{dia:2}", end=" ")  # Día del mes
            print()

# Ejemplo de uso
anio = int(input("Introduce un año: "))
imprimir_calendario_semanal(anio)
