import json
import os

def guardar_historial(nombre_cliente, historial):

    if not os.path.exists('historiales'):
        os.makedirs('historiales')
    
    archivo = f"historiales/{nombre_cliente.lower()}.json"
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)

def cargar_historial(nombre_cliente):
    archivo = f"historiales/{nombre_cliente.lower()}.json"
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 