import streamlit as st
from src.main import crear_sistema

sistema = crear_sistema()
gestion = sistema["veterinarios"]

st.title("🩺 Gestión de Veterinarios")

st.header("Agregar Veterinario")
nombre = st.text_input("Nombre")
esp = st.text_input("Especialidad")

if st.button("Guardar"):
    nuevo = gestion.agregar_veterinario(nombre, esp)
    st.success(f"Veterinario añadido con ID: {nuevo.id}")

st.header("Listado de Veterinarios")
for v in gestion.listar_veterinarios():
    st.write(f"👨‍⚕️ {v.id} — {v.nombre} — {v.especialidad}")
