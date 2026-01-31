# 🤖 AGENTE IA - Agente Auditor de Gestion de Cobranza

# INTEGRANTES
* EDWIN MORA BARCO @masterprime28.
* ISRAEL ONOFRE MONTERO.
* YANDRY FIGUEROA YOSA.
* RUTH CAMPOZANO ROMERO.
* STEVEN ESPAÑA TORRES. 
* CARLOS PAREDES COLOBON.

# 👥 Agente Auditor de Gestión de Cobranzas

Este proyecto consiste en un **Agente Inteligente** diseñado para optimizar los procesos de cobranza mediante el uso de **Machine Learning** y **Procesamiento de Lenguaje Natural (NLP)**. El objetivo principal es auditar el perfil socioeconómico del cliente para ofrecer negociaciones personalizadas con un lenguaje empático.

# 🚀 Funcionalidades Clave

* **🧠 Perfilamiento con IA:** Clasifica a los clientes en tres perfiles (Estable, Moderado y Crítico) utilizando algoritmos de clustering (**K-Means**).
* **💬 Conversación Empática:** Genera respuestas dinámicas utilizando modelos de lenguaje avanzados (**Llama-3**) a través de la API de **Hugging Face**.
* **💾 Memoria de Sesión:** Persistencia de datos mediante archivos **JSON** que permiten al agente recordar conversaciones previas y dar seguimiento a acuerdos.
* **📊 Base de Datos Dinámica:** Manejo de carteras de clientes mediante archivos **CSV** con Pandas.

# 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 
* **Análisis de Datos:** Pandas
* **Machine Learning:** Scikit-learn
* **IA Generativa:** Hugging Face Inference API (Modelo Llama-3-8B-Instruct)
* **Gestión de Entorno:** Python-dotenv

# 📁 Estructura del Proyecto

* `main.py`: Orquestador principal y gestión del bucle de chat.
* `auditor.py`: Motor de auditoría y lógica de Machine Learning.
* `agente_hf.py`: Conexión con la API de Hugging Face y configuración de prompts.
* `generar_datos.py`: Script para crear la base de datos inicial de clientes (`clientes.csv`).
* `historiales/`: Carpeta que almacena las memorias de conversación en formato JSON.

## 📁 Instalación y Uso

1. **Clonar/Abrir la carpeta** en Visual Studio Code.
2. **Crear un entorno virtual:**
   ```bash

   python -m venv venv




