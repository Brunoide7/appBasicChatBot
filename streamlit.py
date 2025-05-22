"""
App chatbot básico con memoria limitada.
"""

#modulos:
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

#inicializa historial si no existe:
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

#carga del llm:
def load_llm(openai_api_key):
    return ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

#limita el historial de mensajes:
def limited_memory_of_messages(messages, number_of_messages_to_keep=4):
    return messages[-number_of_messages_to_keep:]

#prompt:
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         Eres un asistente muy útil. Responde a todas las preguntas lo mejor que puedas."""
         ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

#streamlit UI
st.markdown(
    """
    <div style='text-align: center; padding: 20px; background-color: #76448a; border-radius: 10px; color: white;'>
        <div style='display: flex; justify-content: center; align-items: center; gap: 15px;'>
            <img src="https://cdn-icons-png.flaticon.com/128/1698/1698586.png" width="50">
            <h2 style="margin: 0;">Bienvenido al Chatbot Inteligente</h2>
        </div>
        <div style="display: flex; justify-content: center; gap: 40px; margin-top: 20px;">
            <a href="https://github.com/Brunoide7" target="_blank" style="text-decoration:none; color: white; display:flex; align-items:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" style="margin-right:8px;">
                Mas aplicaciones en GitHub
            </a>
            <a href="https://www.linkedin.com/in/bruno-ignacio-tolaba/" target="_blank" style="text-decoration:none; color: white; display:flex; align-items:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" style="margin-right:8px;">
                Contacto personal en LinkedIn
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

#ingreso de API Key:
openai_api_key = st.text_input("OpenAI API Key", type="password", placeholder="Ex: sk-2twmA8tfCb8un4...")

#ingreso de texto:
draft_input = st.text_area("Escribe tu pregunta abajo y el asistente responderá con memoria limitada.",
                            placeholder="Pregunta..")

#mostrar respuesta:
st.markdown("##### Respuesta:")

if draft_input:
    #verificación de la api_key:
    if not openai_api_key:
        st.warning("Por favor inserte una API Key válida.")
        st.stop()

    llm = load_llm(openai_api_key)

    #cadena:
    chain = prompt | llm

    #función dummy que devuelve el historial desde session_state:
    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        return st.session_state.chat_history

    #cadena completa: 
    chatbot_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_message_key="messages",
    )

    #guardar mensaje del usuario:
    st.session_state.chat_history.add_user_message(draft_input)

    #ejecutar modelo con historial limitado:
    response = chatbot_chain.invoke(
        {"messages": limited_memory_of_messages(st.session_state.chat_history.messages)},
        config={"configurable": {"session_id": "001"}},
    )

    #guardar respuesta del llm:
    st.session_state.chat_history.add_ai_message(response.content)

    #visualización de la respuesta:
    st.write(response.content)
