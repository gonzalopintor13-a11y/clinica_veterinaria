"""
Página Streamlit para gestionar las Historias Clínicas de cada mascota.
Permite añadir nuevas entradas y consultar el historial completo.
"""

import streamlit as st
from datetime import datetime
from src.main import crear_sistema

sistema = crear_sistema()
gMascotas = sistema["mascotas"]
gHistorias = sistema["historias"]
gVets = sistema["veterinarios"]

st.title("📘 Historias Clínicas")

# --- Verificación de datos mínimos ---
if not gMascotas.listar_mascotas():
    st.warning("No hay mascotas registradas. Debes añadir mascotas primero.")
else:
    st.header("➕ Añadir Entrada a la Historia Clínica")

    mascota = st.selectbox(
        "Selecciona la mascota",
        gMascotas.listar_mascotas(),
        format_func=lambda m: m.nombre
    )

    vet = st.selectbox(
        "Veterinario responsable",
        gVets.listar_veterinarios(),
        format_func=lambda v: v.nombre,
        index=0 if gVets.listar_veterinarios() else None
    )

    motivo = st.text_input("Motivo de la consulta")
    diagnostico = st.text_area("Diagnóstico")
    tratamiento = st.text_area("Tratamiento recomendado")
    fecha = datetime.now()

    if st.button("Guardar entrada"):
        entrada = gHistorias.crear_entrada(
            mascota_id=mascota.id,
            vet_id=vet.id if vet else None,
            motivo=motivo,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            fecha=fecha
        )
        st.success(f"Entrada añadida a la historia de {mascota.nombre} (ID: {entrada.id})")

# --- Listado de historias ---
st.header("📄 Historial Clínico")

for m in gMascotas.listar_mascotas():
    st.subheader(f"🐾 {m.nombre} — ID {m.id}")

    entradas = gHistorias.obtener_historia(m.id)

    if not entradas:
        st.write("No hay entradas todavía.")
        continue

    for e in entradas:
        st.write(f"🗓 **Fecha:** {e.fecha}")
        st.write(f"👨‍⚕️ **Veterinario:** {e.vet_id}")
        st.write(f"💬 **Motivo:** {e.motivo}")
        st.write(f"🩺 **Diagnóstico:** {e.diagnostico}")
        st.write(f"💊 **Tratamiento:** {e.tratamiento}")
        st.markdown("---")

