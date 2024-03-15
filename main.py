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

    if st.button("Enviar"):
        show_diagnosis(answers)

if __name__ == "__main__":
    main()
