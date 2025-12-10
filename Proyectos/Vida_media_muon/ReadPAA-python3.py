#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:12:49 2019

@author: hepf
"""
import sys
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd
from paa01 import paaFile
import numpy as np

sys.argv.append("LA-mml-data_1h-180320-182704.paa")

if( len(sys.argv) < 2 ):
    print("No filename given")
    sys.exit()
    
DataFile = paaFile( sys.argv[1] )

print( DataFile.paaGetTextHeader(0) )
print( DataFile.paaGetTextHeader(1) )
print( DataFile.paaGetTextHeader(2) )
print( DataFile.paaGetTextHeader(3) )
print( DataFile.paaGetTextHeader(4) )

ps = DataFile.paaGetPulseSize()
pc = DataFile.paaGetPulseCount()
tl = DataFile.paaGetThresholdLevel()

print("Points per pulse: ", ps)
print("Pulses in this file: ", pc)
print("threshold level: ", tl)
print()

pulse_data_t = list(range( ps ))

#Ahora vamos a hallar los eventos con dos pulsos
threshold = -150
min_separation = 5   # muestras mínimas para considerar que dos pulsos son distintos
tiempos_picos = []

for i in range(pc):
    data = DataFile.paaGetPulseRP(i)
    j = 0
    pulsos = []  # aquí guardaremos los índices de inicio de cada pulso
    # estado = 0: buscando inicio, estado = 1: dentro de pulso hasta salir del umbral
    estado = 0

    while j < len(data):
        if estado == 0:
            # busco cruce descendente de umbral
            if data[j] < threshold:
                pulsos.append(j)
                estado = 1
            j += 1
        else:
            # estoy dentro de un pulso, espero a que termine (se recupere arriba del umbral)
            if data[j] >= threshold:
                estado = 0
                # para evitar que vuelvas a detectar el mismo pulso por pequeñas oscilaciones,
                # saltamos algunas muestras
                j += min_separation
            else:
                j += 1

    # si encontré al menos dos pulsos completos, mido la distancia entre los dos primeros
    if len(pulsos) >= 2:
        dt_muestras = pulsos[1] - pulsos[0]
        dt_ns = dt_muestras * 8       # 8 ns por muestra
        # filtrar tiempos razonables, por ejemplo entre 1000 ns (1 μs) y 20000 ns (20 μs)
        if 0 < dt_ns < 8000:
            tiempos_picos.append(dt_ns / 1000.0)  # lo guardo en μs


print("Los tiempos entre pulsos son", tiempos_picos)
print("La vida media del muon fue de", np.mean(tiempos_picos) )
#Guardamos los tiempos entre pulsos en un doc excel
df = pd.DataFrame(tiempos_picos, columns=['Tiempos entre pulsos'])
df.to_excel('tiempos_picos5.xlsx', index = False)

while(1):
    try:
        pulse_number = int(input('Pulse number to plot: '))
    except ValueError:
        print("Not a number")
        sys.exit(0)
    except KeyboardInterrupt:
        print()
        sys.exit()
    if( ( pulse_number < 0 ) or (pulse_number > (pc-1) )):
        print("Error: Bad pulse number")
        sys.exit(0)
    pulse_data_v = DataFile.paaGetPulseRP(pulse_number)
    # For paa files generated from other sources than
    # pacq on a RedPitaya, use paaGetPulseRaw() instead.
    #
    #pulse_data_v = DataFile.paaGetPulseRaw(pulse_number)
    #
    
    plt.plot(pulse_data_t, pulse_data_v)
        
    ax = plt.gca()
    ax.add_line( mlines.Line2D([0,ps-1], [tl,tl] ) )
    plt.show()
