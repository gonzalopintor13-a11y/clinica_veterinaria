<<<<<<< HEAD
# clinica_veterinaria
Proyecto Progamación II. Clínica veterinaria con python.
Autores proyecto: Gonzalo Pintor y Gonzalo Nocea
=======
# 🏥 Clínica Veterinaria

Proyecto académico para la asignatura **Programación II (UFV)**.  
El objetivo es desarrollar un sistema de gestión para una clínica veterinaria aplicando **POO, SOLID, TDD, manejo de excepciones, logging, decoradores y conexión a base de datos** (SQLite o MySQL).

---

## 👨‍💻 Integrantes del equipo
- Gonzalo Pintor  
- Gonzalo Nocea

## 📁 Estructura del proyecto

clinica_veterinaria/
│
├── venv/
├── streamlit/
│   └── pages/
│
├── src/
│   ├── models/
│   │   ├── mascota.py
│   │   ├── cliente.py
│   │   ├── veterinario.py
│   │   └── cita.py
│   │
│   ├── utils/
│   │   ├── excepciones.py
│   │   ├── logger.py
│   │   ├── utilidades.py
│   │   └── db_connector.py
│   │
│   ├── services/
│   │   ├── gestion_mascotas.py
│   │   ├── gestion_clientes.py
│   │   ├── gestion_veterinarios.py
│   │   └── gestion_citas.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_mascota.py
│   └── test_db_connector.py
│
├── logs/
├── requirements.txt
└── README.md


## ⚙️ Tecnologías utilizadas

- **Python 3.12**
- **FastAPI** → para API REST y microservicios  
- **Streamlit** → para interfaz visual  
- **SQLAlchemy** + **MySQL / SQLite** → para persistencia  
- **Logging**, **Excepciones personalizadas**, **Decoradores**, **Generadores (yield)**  
- **Principios SOLID** aplicados en las clases  
- **TDD (Test Driven Development)** con `pytest`



>>>>>>> 2e604af (Estructura inicial del proyecto clinica veterinaria)
