import pandas as pd
import random

data = {
    'nombre': ['Ana', 'Luis', 'Carlos', 'Maria', 'Jose', 'Elena', 'Pedro', 'Laura', 'Diego', 'Sofia'],
    'ingresos': [2500, 1200, 3500, 800, 2100, 1500, 4000, 950, 2800, 1100],
    'meses_atraso': [1, 3, 0, 5, 2, 4, 1, 6, 0, 3],
    'deuda_total': [500, 1200, 200, 1500, 800, 900, 300, 2000, 150, 1100]
}

df = pd.DataFrame(data)
df.to_csv('clientes.csv', index=False)
print("¡Archivo clientes.csv creado con éxito!")