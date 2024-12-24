

import random
import streamlit as st

# Lista de cartas: cada una en inglés y español
cartas = [
    "Dog - Perro", "Cat - Gato", "Car - Auto", "House - Casa", "Tree - Árbol",
    "Pizza - Pizza", "Movie - Película", "Superhero - Superhéroe", 
    "Phone - Teléfono", "Airport - Aeropuerto", "School - Escuela",
    "Doctor - Doctor", "Soccer - Fútbol", "Beach - Playa", 
    "Rainbow - Arco iris", "Doctor - Médico", "Mountain - Montaña", 
    "Elephant - Elefante", "Basketball - Baloncesto", "Television - Televisión",
    # ... You can include all the other cards here
    "Virus - Virus", "Antivirus - Antivirus", "Revolución industrial - Industrial revolution"
]

# Función para elegir una carta aleatoria
def elegir_carta_aleatoria(cartas):
    return random.choice(cartas)

# Título de la aplicación
st.title("Bienvenido a Pictiona..Lui")

# Instrucciones
st.write("Presiona el botón para sacar una carta al azar")

# Botón para generar una nueva carta
if st.button("Nueva Carta"):
    carta = elegir_carta_aleatoria(cartas)
    st.success(f"Tu carta al azar es: **{carta}**")
else:
    st.info("Haz clic en el botón para comenzar.")

# Mensaje de despedida opcional
st.write("¡Buena suerte!")
