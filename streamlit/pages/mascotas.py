import streamlit as st
from datetime import date
from src.main import crear_sistema

sistema = crear_sistema()
gClientes = sistema["clientes"]
gMascotas = sistema["mascotas"]

st.title("🐶 Gestión de Mascotas")

propietarios = gClientes.listar_clientes()
if not propietarios:
    st.warning("Primero debes añadir clientes.")
else:
    st.header("Agregar Mascota")
    nombre = st.text_input("Nombre")
    especie = st.text_input("Especie")
    raza = st.text_input("Raza")
    fecha_nac = st.date_input("Fecha de nacimiento", date.today())
    propietario = st.selectbox("Propietario", propietarios, format_func=lambda x: x.nombre)

    if st.button("Guardar"):
        nueva = gMascotas.agregar_mascota(nombre, especie, raza, fecha_nac, propietario.id)
        st.success(f"Mascota añadida con ID: {nueva.id}")

st.header("Listado de Mascotas")
for m in gMascotas.listar_mascotas():
    st.write(f"🐾 {m.id} — {m.nombre} ({m.especie}) — Propietario: {m.propietario_id}")
