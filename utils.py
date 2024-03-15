import streamlit as st

def calculate_security_score(answers):
    security_score = 0
    for answer in answers.values():
        if isinstance(answer, list):
            security_score += len(answer)
        elif answer == "Sí":
            security_score += 1
    return security_score

def show_diagnosis(answers):
    total_questions = 8 
    security_score = calculate_security_score(answers)
    max_score = total_questions

    if security_score >= max_score * 0.9:
        st.success("¡Enhorabuena! Su seguridad cibernética parece estar bien protegida.")
    elif security_score >= max_score * 0.7:
        st.info("Tiene una seguridad cibernética razonable, pero hay margen de mejora.")
    elif security_score >= max_score * 0.5:
        st.warning("Puede haber algunas áreas de preocupación en su seguridad cibernética. Se recomienda tomar medidas adicionales.")
    else:
        st.error("Es posible que tenga vulnerabilidades significativas en su seguridad cibernética. Se recomienda tomar medidas urgentes.")


    if answers.get("¿Utiliza contraseñas seguras y las cambia regularmente?", "") == "No":
        st.subheader("Recomendaciones:")
        st.markdown("- **Utiliza contraseñas seguras y las cambia regularmente:** Es importante utilizar contraseñas complejas y cambiarlas periódicamente para evitar accesos no autorizados.")
    if answers.get("¿Mantiene su software actualizado?", "") == "No":
        st.subheader("Recomendaciones:")
        st.markdown("- **Mantiene su software actualizado:** Mantener el software actualizado es esencial para parchear vulnerabilidades conocidas y protegerse contra ataques.")
    if answers.get("¿Utiliza un software antivirus actualizado?", "") == "No":
        st.subheader("Recomendaciones:")
        st.markdown("- **Utiliza un software antivirus actualizado:** Un software antivirus actualizado puede ayudar a proteger su sistema contra malware y otras amenazas en línea.")
    if answers.get("¿Ha recibido capacitación en seguridad cibernética en el último año?", "") == "No":
        st.subheader("Recomendaciones:")
        st.markdown("- **Recibir capacitación en seguridad cibernética:** Mantenerse actualizado sobre las últimas amenazas y mejores prácticas de seguridad es crucial para protegerse en línea.")
