import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def crecimientoPob(p0, r):
    pt = p0
    pob_anio = [p0]
    for t in range(1,1000):
        pt = pt*(1+r)
        pob_anio.append(pt)
        if pt >= 2*p0:
            print(f'la poblacion se duplica en {t} años')
            break
    return pob_anio

p0 = 1000
r = 0.005

poblacion_1 = crecimientoPob(p0, r)
for t, pt in enumerate(poblacion_1):
    print(f'La población en el año {t} es {pt}')


plt.figure(figsize=(14,9))
plt.plot(range(len(poblacion_1)), poblacion_1, marker='o')
plt.xlabel('tiempo')
plt.ylabel('población')
plt.title(f'Crecimiento poblacional\nPoblación inicial: {p0}\nTasa de cremimiento de: {r*100}%\nLa población se duplica cada {(len(poblacion_1))-1} años ', fontsize=13, fontweight='bold' )
duplicacion = poblacion_1.index(next(x for x in poblacion_1 if x>=2 *p0))
plt.axvline(x=duplicacion, color='r', linestyle='--')
#plt.text(duplicacion-2.5, 2*p0-700,'Duplicación de la\n población inicial', rotation=0, va='bottom')
plt.legend()
plt.grid(True)
plt.savefig('crecimiento_poblacional_a.png')
plt.show()