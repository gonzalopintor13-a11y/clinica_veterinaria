import streamlit as st
from src.main import crear_sistema

sistema = crear_sistema()
gestion = sistema["clientes"]

st.title("👤 Gestión de Clientes")

st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
telefono = st.text_input("Teléfono")
email = st.text_input("Email")

if st.button("Guardar"):
    nuevo = gestion.agregar_cliente(nombre, telefono, email)
    st.success(f"Cliente añadido con ID: {nuevo.id}")

st.header("Listado de Clientes")
for c in gestion.listar_clientes():
    st.write(f"📌 {c.id} — {c.nombre} — {c.telefono} — {c.email}")
