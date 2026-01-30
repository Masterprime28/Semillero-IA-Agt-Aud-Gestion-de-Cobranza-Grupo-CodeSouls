from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def respuesta_ia(historial, perfil, deuda):
    prompt_sistema = {
        "role": "system", 
        "content": f"""Actúa como un asesor humano y amable. 
        El cliente es {perfil} y debe ${deuda}.
        REGLAS CRÍTICAS:
        1. Responde máximo en 3 frases.
        2. NO te presentes como auditor ni como IA.
        3. NO traduzcas al inglés.
        4. Sé muy empático y directo."""
    }
    
    historial_limpio = [msg for msg in historial if msg.get("content") and msg["content"].strip()]
    mensajes_completos = [prompt_sistema] + historial_limpio

    response = client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct", 
        messages=mensajes_completos,
        max_tokens=150,
        temperature=0.5 
    )
    
    return response.choices[0].message.content