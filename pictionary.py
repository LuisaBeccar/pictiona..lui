

import random
import streamlit as st

# Lista de cartas: cada una en inglés y español
cartas = ["Dog - Perro", "Cat - Gato", "Car - Auto", "House - Casa", "Tree - Árbol", 
 "Pizza - Pizza", "Movie - Película", "Superhero - Superhéroe", "Phone - Teléfono",
  "Airport - Aeropuerto", "School - Escuela", "Doctor - Doctor",
  "Soccer - Fútbol", "Beach - Playa", "Rainbow - Arco iris",
  "Doctor - Médico", "Mountain - Montaña", "Elephant - Elefante",
  "Basketball - Baloncesto", "Television - Televisión", "Clown - Payaso",
  "Santa Claus - Santa Claus", "Fish - Pez", "Bird - Pájaro",
  "Train - Tren", "Robot - Robot", "Guitar - Guitarra",
  "Cake - Pastel", "Sun - Sol", "Moon - Luna",
  "Ice Cream - Helado", "Shark - Tiburón", "Computer - Computadora",
  "Beach Ball - Pelota de playa", "Tennis - Tenis", "Firefighter - Bombero",
  "Lion - León", "Cow - Vaca", "Pirate - Pirata",
  "Bicycle - Bicicleta", "Vampire - Vampiro", "Wizard - Mago",
  "Giraffe - Jirafa", "Hurricane - Huracán", "Snowman - Muñeco de nieve",
  "Spider - Araña", "Vase - Florero", "Jungle - Jungla",
  "Circus - Circo", "Library - Biblioteca", "Lighthouse - Faro",
  "Helicopter - Helicóptero", "Chandelier - Araña (de luz)", "Waterfall - Cascada",
  "Puzzle - Rompecabezas", "Magician - Mago", "Submarine - Submarino",
  "Harmonica - Armónica", "Microscope - Microscopio", "Telescope - Telescopio",
  "Owl - Búho", "Octopus - Pulpo", "Witch - Bruja",
  "Spaghetti - Espagueti", "Chameleon - Camaleón", "Cactus - Cactus",
  "Eclipse - Eclipse", "Dragonfly - Libélula", "Treasure - Tesoro",
  "Castle - Castillo", "Turtle - Tortuga", "Carousel - Carrusel",
  "Accordion - Acordeón", "Chopsticks - Palillos", "Jukebox - Jukebox",
  "Cliff - Acantilado", "Scarecrow - Espantapájaros", "Lobster - Langosta",
  "Trampoline - Trampolín", "Caterpillar - Oruga", "Dinosaur - Dinosaurio",
  "Knight - Caballero", "Seahorse - Caballito de mar", "Pyramid - Pirámide",
  "Postcard - Postal", "Sandcastle - Castillo de arena", "Stethoscope - Estetoscopio",
  "Kite - Cometa", "Lightning - Relámpago", "Ballet - Ballet",
  "Popcorn - Palomitas de maíz", "Bumblebee - Abejorro", "Broomstick - Escoba",
  "Compass - Brújula", "Zebra - Cebra", "Eclipse solar - Solar eclipse",
  "Reloj de arena - Hourglass", "Sismo - Earthquake", "Fantasía - Fantasy", "Alquimia - Alchemy",
  "Cerebro - Brain", "Aguijón - Stinger", "Supernova - Supernova",
  "Cilindro - Cylinder", "Cromosoma - Chromosome", "Imán - Magnet",
  "Arquitecto - Architect", "Tsunami - Tsunami", "Meteorito - Meteorite",
  "Antártida - Antarctica", "Dodecaedro - Dodecahedron", "Biblioteca - Library",
  "Química - Chemistry", "Cromatografía - Chromatography", "Filósofo - Philosopher",
  "Aeropuerto - Airport", "Hidrosfera - Hydrosphere", "Sinfonía - Symphony",
  "Torbellino - Whirlwind", "Anarquía - Anarchy", "Bumerán - Boomerang", "Fahrenheit - Fahrenheit", 
  "Fórmula matemática - Mathematical formula",
  "Arquitectura gótica - Gothic architecture", "Ojo de huracán - Eye of the hurricane", "Antídoto - Antidote",
  "Científico - Scientist", "Neurona - Neuron", "Translúcido - Translucent",
  "Estalactita - Stalactite", "Magnetismo - Magnetism", "Genoma - Genome",
  "Holograma - Hologram", "Cianuro - Cyanide", "Radiación - Radiation", "Virus - Virus", 
"Antivirus - Antivirus", "Revolución industrial - Industrial revolution"]


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
    st.success(f"Tu carta al azar es:      **{carta}**")
#

# Mensaje de despedida opcional
st.write("¡Buena suerte!")
