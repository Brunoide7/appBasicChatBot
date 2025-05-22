# 🧠 appBasicChatBot

Esta es una aplicación básica de chatbot desarrollada con LangChain y Streamlit, que permite interactuar con un modelo de lenguaje de OpenAI en tiempo real. El asistente mantiene una memoria limitada de los últimos mensajes, lo que simula una conversación coherente sin almacenar un historial completo.

## ✨ Características principales
- Interfaz web desarrollada con Streamlit.
- Conexión a modelos de lenguaje de OpenAI.
- Uso de LangChain para estructurar el flujo conversacional.
- Historial de conversación limitado a los últimos N mensajes.
- Compatible con despliegue en Streamlit Cloud.

## 📸 Captura / Demo

![imagen](https://github.com/user-attachments/assets/60926aae-b67c-4f92-9d1e-24ff010726f3)

👉 [Ver en Streamlit](https://appbasicchatbot.streamlit.app/)

## 📦 Requisitos / Instalación / Uso

```bash
git clone https://github.com/Brunoide7/appBasicChatBot.git
cd appBasicChatBot
pip install -r requirements.txt
streamlit run app.py

