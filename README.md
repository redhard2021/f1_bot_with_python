# 🏎️ Telegram F1 Bot

Este es un bot de Telegram simple que permite consultar información actualizada sobre la Fórmula 1, como:

- Cuándo es la próxima carrera.
- Tabla de posiciones de los pilotos.
- Interacción con lenguaje natural (preguntas como "¿cuándo es la próxima carrera?" en lugar de comandos `/next_race`).

## 🚀 Funcionalidades

- Consulta de información a través de una API gratuita de F1.
- Uso de IA local (modelo de embeddings) para interpretar frases del usuario y mapearlas a intenciones.
- Interfaz sencilla con comandos y/o lenguaje natural.

## 🛠️ Tecnologías y Librerías Utilizadas

- **Python 3.10+**
- **python-telegram-bot** – para manejar la interacción con Telegram.
- **requests** – para hacer peticiones HTTP a la API de F1.
- **sentence-transformers** – para interpretación semántica de frases (IA ligera, local).
- **python-dotenv** – para gestión de variables sensibles en un archivo `.env`.

## 📁 Estructura del proyecto
telegram-bot-f1/ 
│ ├── bot/ # Lógica principal del bot 
│ ├── handlers/ # Manejadores de comandos y respuestas 
| ├── settings/ # Carga del .env
│ ├── services/ # Conexión con la API de F1 
│ ├── ai/ # Clasificación de intenciones con IA local 
│ ├── .env # Variables de entorno (no subido al repo) 
├── main.py # Punto de entrada de la aplicación 
├── requirements.txt # Lista de dependencias 
├── README.md


## ⚙️ Instalación y uso

# Clona el repositorio
git clone https://github.com/tu_usuario/telegram-f1-bot.git
cd telegram-f1-bot

# Crea un entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Crea tu archivo .env y agrega tu token de Telegram
echo "TELEGRAM_TOKEN=tu_token_aqui" > .env

# Ejecuta el bot
python main.py
