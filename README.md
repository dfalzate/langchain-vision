# LangGraph AI Examples

Este repositorio contiene ejemplos de implementación de agentes inteligentes utilizando [LangGraph](https://langchain-ai.github.io/langgraph/), [LangChain](https://python.langchain.com/) y [Ollama](https://ollama.com/).

## Contenido del Proyecto

El proyecto incluye tres ejemplos principales de flujos de trabajo con agentes:

### 1. AI Butler "Alfred" (`main.py`)
Un asistente personal multimodal capaz de ver y analizar imágenes, así como realizar cálculos matemáticos.
- **Modelos**: Utiliza `ministral-3:8b` para visión (OCR) y `qwen3:8b` para razonamiento.
- **Funcionalidades**:
  - Extracción de texto de imágenes (OCR) para leer notas manuscritas o documentos.
  - Herramienta de cálculo (división).
  - Mantiene el historial de conversación.
- **Uso de multimodalidad**: Puede interpretar imágenes como `training_and_meals.png` para responder preguntas sobre su contenido (ej. listas de compra).

### 2. Email Intelligent Agent (`main2.py`)
Un sistema completo de procesamiento de correos electrónicos que automatiza la clasificación y respuesta.
- **Modelo**: Utiliza `kimi-k2.5:cloud` a través de Ollama.
- **Flujo de trabajo**:
  1. **Lectura**: Lee el correo entrante.
  2. **Clasificación**: Determina si es Spam o Legítimo usando un LLM.
  3. **Enrutamiento**:
     - Si es **Spam**: Lo descarta y registra la razón.
     - Si es **Legítimo**: Categoriza el correo (consulta, queja, etc.) y redacta un borrador de respuesta.
  4. **Notificación**: Presenta el borrador final al usuario (Mr. Hugg).
- **Observabilidad**: Integrado con [LangFuse](https://langfuse.com/) para trazas y monitoreo.

### 3. Simple Mood Graph (`main1.py`)
Un ejemplo básico introductorio a LangGraph.
- Demuestra cómo crear un grafo de estados simple con nodos y aristas condicionales.
- Decide aleatoriamente entre dos caminos ("happy" o "sad") para ilustrar la lógica de ramificación.

## Requisitos Previos

- **Python 3.10+**
- **Ollama**: Debe estar instalado y ejecutándose localmente (`ollama serve`).
- **Modelos de Ollama**: Debes tener descargados los modelos utilizados o ajustar el código para usar los que tengas:
  ```bash
  ollama pull ministral-3:8b
  ollama pull qwen3:8b
  ollama pull kimi-k2.5:cloud
  ```

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto para las variables de entorno, especialmente si usas LangFuse para `main2.py`:

```env
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

## Uso

Para ejecutar cualquiera de los agentes, simplemente corre el script de Python correspondiente:

```bash
# Ejecutar el mayordomo Alfred
python main.py

# Ejecutar el agente de emails
python main2.py

# Ejecutar el ejemplo básico de grafo
python main1.py
```

## Estructura de Archivos

- `main.py`: Lógica del asistente Alfred (Multimodal).
- `main2.py`: Lógica del agente de correos (Email Automation).
- `main1.py`: Ejemplo básico de grafo de estados.
- `requirements.txt`: Lista de dependencias del proyecto.
- `training_and_meals.png`: Imagen de ejemplo para probar las capacidades de visión de Alfred.
