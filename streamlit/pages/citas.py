import streamlit as st
from datetime import datetime
from src.main import crear_sistema

sistema = crear_sistema()
gCitas = sistema["citas"]
gMascotas = sistema["mascotas"]
gVets = sistema["veterinarios"]

st.title("📅 Gestión de Citas")

if not gMascotas.listar_mascotas() or not gVets.listar_veterinarios():
    st.warning("Necesitas mascotas y veterinarios para crear citas.")
else:
    st.header("Programar Cita")

    mascota = st.selectbox("Mascota", gMascotas.listar_mascotas(), format_func=lambda x: x.nombre)
    vet = st.selectbox("Veterinario", gVets.listar_veterinarios(), format_func=lambda x: x.nombre)
    fecha = st.date_input("Fecha")
    hora = st.time_input("Hora")
    motivo = st.text_input("Motivo")

    if st.button("Guardar"):
        dt = datetime.combine(fecha, hora)
        nueva = gCitas.programar_cita(mascota.id, vet.id, dt, motivo)
        st.success(f"Cita creada con ID: {nueva.id}")

st.header("Listado de Citas")
for c in gCitas.listar_citas():
    st.write(f"📌 {c.id} — Mascota: {c.mascota_id} — Vet: {c.veterinario_id} — {c.fecha_hora} — {c.estado}")
