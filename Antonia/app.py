import streamlit as st
import datetime
import os
import random

# Configuración para el iPhone
st.set_page_config(
    page_title="Nuestra Historia ❤️",
    page_icon="🌷",
    layout="centered"
)

# Personalización de colores, botones y centrado del contador
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #FFFFFF;
    }
    /* Color de títulos principales */
    h1, h2, h3 {
        color: #d81b60 !important;
        text-align: center;
        font-weight: bold;
    }
    /* Color de párrafos y textos generales */
    p, span, div, label {
        color: #2b2b2b !important;
    }
    /* Centrar textos y etiquetas del contador de métricas */
    [data-testid="stMetric"] {
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    [data-testid="stMetricValue"] {
        color: #d81b60 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #4a4a4a !important;
    }
    /* Estilo personalizado para los Botones (Fondo fucsia, texto blanco) */
    .stButton > button {
        background-color: #d81b60 !important;
        color: #ffffff !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
    }
    .stButton > button:hover {
        background-color: #c2185b !important;
        color: #ffffff !important;
    }
    .stButton > button p {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💕 Para Antonia Mi Persona Favorita 💕")
st.write("### Hice esta página solo para ti...")

st.divider()

# --- 1. CONTADOR DE TIEMPO ---
st.subheader("⏳ Tiempo que llevamos juntos")

# Fecha en la que empezamos a ser novios (7 de Agosto de 2026, 8:30 PM)
fecha_inicio = datetime.datetime(2026, 8, 7, 20, 30, 0)
ahora = datetime.datetime.now()

diferencia = ahora - fecha_inicio
dias = diferencia.days
horas = diferencia.seconds // 3600
minutos = (diferencia.seconds % 3600) // 60

# Mostrar en 3 columnas estilizadas
col1, col2, col3 = st.columns(3)
col1.metric("Días", f"{dias}")
col2.metric("Horas", f"{horas}")
col3.metric("Minutos", f"{minutos}")

# Mensaje centrado
st.markdown("<p style='text-align: center; font-size: 18px; font-weight: 500;'>Quiero seguir cada segundo contigo 😍</p>", unsafe_allow_html=True)

st.divider()

# --- 2. SECCIÓN INTERACTIVA DE RAZONES ---
st.subheader("💗 Una razón especial por la que te amo 💗")

razones = [
    "Porque a pesar de todo siempre tengo ganas de verte",
    "Cuando me miras se que todo esta bien",
    "Me llenas de paz",
    "Porque no necesito a nadie mas",
    "Porque me pierdo en tus ojos",
    "Cuando me abrazas me tranquilizas",
    "Porque contigo cada minuto vale",
    "Eres la mujer de mis sueños",
    "Me tienes loco por verte cada dia",
    "Te amo Antonia Ceron Arroyo",
    "Porque te necesito",
    "Confio en ti como en nadie mas",
    "Me encantaria estar todo el dia contigo",
    "Me encantan tus abrazos"
]

if st.button("❤️❤️❤️", use_container_width=True):
    razon_elegida = random.choice(razones)
    st.success(razon_elegida)
    st.balloons()

st.divider()

# --- 3. GALERÍA DE FOTOS EN 2 COLUMNAS ---
st.subheader("📸 Nuestros mejores momentos 💫")

# Rutas posibles donde puede estar la carpeta de imágenes
rutas_posibles = ["fotos", "Antonia/fotos", "./fotos"]
carpeta_fotos = None

for ruta in rutas_posibles:
    if os.path.exists(ruta) and os.path.isdir(ruta):
        carpeta_fotos = ruta
        break

if carpeta_fotos:
    archivos_fotos = [
        os.path.join(carpeta_fotos, f) 
        for f in os.listdir(carpeta_fotos) 
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))
    ]
    
    if archivos_fotos:
        col_izq, col_der = st.columns(2)
        for i, foto in enumerate(archivos_fotos):
            if i % 2 == 0:
                col_izq.image(foto, use_container_width=True)
            else:
                col_der.image(foto, use_container_width=True)
    else:
        st.info("La carpeta 'fotos' existe pero no contiene imágenes soportadas.")
else:
    st.info("No se encontró la carpeta con las imágenes.")
# --- 4. MENSAJE FINAL ---
if st.button("Haz clic aquí ❤️", use_container_width=True):
    st.balloons()
    st.success("Gracias por estar en mi vida, tu eres mi mas grande regalo")