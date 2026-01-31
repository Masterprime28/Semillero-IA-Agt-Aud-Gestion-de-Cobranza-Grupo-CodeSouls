import pandas as pd
from sklearn.cluster import KMeans

def auditar_con_IA(nombre_cliente):
    df = pd.read_csv('clientes.csv')
    
    X = df[['ingresos', 'meses_atraso', 'deuda_total']]
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['perfil_id'] = kmeans.fit_predict(X)
    
    cliente = df[df['nombre'].str.lower() == nombre_cliente.lower()]
    
    if cliente.empty:
        return None, None
    
    perfil_id = cliente['perfil_id'].values[0]
    deuda = cliente['deuda_total'].values[0]

    mapa_perfiles = {
        0: "ESTABLE (Recordatorio amable)",
        1: "MODERADO (Requiere negociación)",
        2: "CRÍTICO (Requiere máxima empatía)"
    }
    
    return mapa_perfiles.get(perfil_id), deuda

print("Modelo de IA entrenado y listo.")