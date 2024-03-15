import re
import streamlit as st
from utils import calculate_security_score, show_diagnosis

def main():
    st.title("SE-Ciberseguridad")

    questions = [
        {
            "question": "¿Utiliza contraseñas seguras y las cambia regularmente?",
            "type": "radio",
            "options": ["Sí", "No"]
        },
        {
            "question": "¿Mantiene su software actualizado?",
            "type": "radio",
            "options": ["Sí", "No"]
        },
        {
            "question": "¿Utiliza un software antivirus actualizado?",
            "type": "radio",
            "options": ["Sí", "No"]
        },
        {
            "question": "¿Qué tipo de dispositivos de almacenamiento utiliza con frecuencia?",
            "type": "multiselect",
            "options": ["USB", "Discos externos", "Nube", "Correo electrónico", "Disco duro del dispositivo"]
        },
        {
            "question": "¿Qué sistemas operativos utiliza?",
            "type": "multiselect",
            "options": ["Windows", "MacOS", "Linux", "iOS", "Android"]
        },
        {
            "question": "¿Ha recibido capacitación en seguridad cibernética en el último año?",
            "type": "radio",
            "options": ["Sí", "No"]
        },
        {
            "question": "¿Cómo evalúa su conocimiento en seguridad cibernética?",
            "type": "selectbox",
            "options": ["Bajo", "Medio", "Alto"]
        },
        {
            "question": "¿Cuál de las siguientes prácticas de seguridad cibernética realiza regularmente?",
            "type": "multiselect",
            "options": ["Realizar copias de seguridad", "Utilizar VPN", "Actualizar software regularmente", "Utilizar autenticación de dos factores", "Revisar permisos de aplicaciones", "Utilizar administrador de contraseñas"]
        },
        {
            "question": "Por favor, ingrese el correo electrónico:",
            "type": "text"
        }
    ]

    answers = {}

    for i, question_data in enumerate(questions):
        question = question_data["question"]
        question_type = question_data["type"]

        if question_type == "radio":
            answer = st.radio(question, options=question_data["options"])
            answers[question] = answer
        elif question_type == "multiselect":
            answer = st.multiselect(question, options=question_data["options"])
            answers[question] = answer
        elif question_type == "selectbox":
            answer = st.selectbox(question, options=question_data["options"])
            answers[question] = answer
        elif question_type == "text":
            answer = st.text_input(question)
            answers[question] = answer

    if st.button("Enviar"):
        if validate_institutional_email(answers.get("Por favor, ingrese el correo electrónico:", "")):
            show_diagnosis(answers)
            st.success("Correo institucional verificado.")
        else:
            show_diagnosis(answers)
            st.error("¡ALERTA DE PISHING! Este correo no pertenece a la empresa.")

def validate_institutional_email(email):
    # Expresión regular para verificar el formato del correo electrónico
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verifica si el correo electrónico sigue el formato correcto
    if re.match(email_regex, email):
        # Verifica si el dominio del correo electrónico es institucional
        institutional_domains = ["unica.edu.pe", "sistemasunica.edu.pe"]
        domain = email.split('@')[-1]
        if domain in institutional_domains:
            return True
    return False

if __name__ == "__main__":
    main()