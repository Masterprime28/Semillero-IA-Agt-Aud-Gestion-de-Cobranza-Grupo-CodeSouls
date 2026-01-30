import pandas as pd
import os
import json
from auditor import auditar_con_IA
from agente_hf import respuesta_ia

def cargar_historial(nombre_cliente):
    """Carga mensajes previos de un archivo JSON."""
    ruta = f"historiales/{nombre_cliente.lower()}.json"
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_historial(nombre_cliente, historial):
    """Guarda la conversación actual en un archivo JSON."""
    if not os.path.exists('historiales'):
        os.makedirs('historiales')
    ruta = f"historiales/{nombre_cliente.lower()}.json"
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)


def ejecutar_agente_auditor():
    print("\n" + "="*60)
    print("   AGENTE AUDITOR INTELIGENTE: GESTIÓN DE COBRANZAS v1.0")
    print("="*60)
    
    try:
        df = pd.read_csv('clientes.csv')
        print(f"✅ Conectado a base de datos de clientes.")
    except FileNotFoundError:
        print("❌ Error: No se encontró 'clientes.csv'.")
        return

    # 2. Identificación y Perfilamiento con ML
    while True:
        nombre_input = input("\n👤 Ingrese el nombre del cliente (o escribe 'salir' para cerrar): ").strip().lower()
        
        # Opción para cerrar el programa si se equivocaron de App
        if nombre_input == 'salir':
            print("Cerrando sistema...")
            return

        # Intentamos obtener el perfil
        perfil, deuda = auditar_con_IA(nombre_input)
        
        if perfil:
            # Si el perfil existe, rompemos el bucle y seguimos con el chat
            break
        else:
            # Si no existe, lanzamos el mensaje de error y el bucle vuelve a empezar
            print(f"❌ El cliente '{nombre_input}' no existe en la base de datos.")
            print("👉 Intenta con: " + ", ".join(df['nombre'].tolist())) # Tip extra: muestra los nombres disponibles

    historial = cargar_historial(nombre_input)
    nombre_cap = nombre_input.capitalize()
    
    print(f"\n[SISTEMA]: Perfil Socioeconómico: {perfil}")
    print(f"[SISTEMA]: Deuda a auditar: ${deuda}")
    
    if historial:
        print(f"✨ Bienvenido de nuevo, {nombre_cap}. Retomando conversación previa...")
    else:
        print(f"👋 Iniciando nueva sesión de auditoría para {nombre_cap}.")

    print("\n" + "-"*60)
    print(f"Agente: Hola {nombre_cap}, ¿cómo podemos avanzar con tu saldo pendiente?")
    
    while True:
        usuario_txt = input(f"\n[{nombre_cap}] (escribe 'salir' para guardar): ").strip()
        
        if usuario_txt.lower() in ['salir', 'adios', 'finalizar']:
            guardar_historial(nombre_input, historial)
            print("\n✅ Conversación guardada exitosamente en /historiales/.")
            print("👋 ¡Hasta la próxima sesión!")
            break

        if not usuario_txt:
            continue

        historial.append({"role": "user", "content": usuario_txt})
        
        print("\n[IA procesando contexto y memoria...] ⏳")
        
        try:
            respuesta = respuesta_ia(historial, perfil, deuda)
            
            historial.append({"role": "assistant", "content": respuesta})
            
            print(f"\n[Agente Auditor]: {respuesta}")
            
        except Exception as e:
            print(f"❌ Error al conectar con la IA: {e}")
            break

if __name__ == "__main__":
    ejecutar_agente_auditor()