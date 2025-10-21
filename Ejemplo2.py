# ------------------------------------------------------------
# 🇲🇽 Ejercicio 2: Generador de datos falsos de México
# Este programa crea nombres, correos, direcciones y datos falsos mexicanos.
# Usa Faker para generar los datos y PyQt5 para mostrarlos en una ventana.
# ------------------------------------------------------------

# Importamos las librerías necesarias
from faker import Faker
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
import random
import unicodedata
import sys

# Faker con datos basados en México
fake = Faker('es_MX')

# Lista de dominios válidos para los correos
dominios = ['gmail.com', 'hotmail.com']

# Función que quita tildes a letras (para evitar errores en el correo)
def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )

# Clase principal de la ventana
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos falsos de México")  # Título de la ventana
        self.resize(600, 500)  # Tamaño de la ventana
        
        layout = QVBoxLayout()  # Diseño vertical

        # Cuadro donde se mostrarán los datos
        self.texto = QTextEdit()
        # Botón para generar los datos
        boton = QPushButton("Generar datos")
        boton.clicked.connect(self.generar_datos)  # Cuando se presiona, llama a la función

        # Agregamos los elementos al diseño
        layout.addWidget(self.texto)
        layout.addWidget(boton)
        self.setLayout(layout)

    # Función para generar los datos falsos
    def generar_datos(self):
        self.texto.clear()  # Limpia el cuadro antes de mostrar nuevos datos
        for i in range(4):  # Genera 4 usuarios
            nombre_completo = fake.name()
            partes = nombre_completo.lower().split()

            # Tomamos nombre y apellido sin tildes para el correo
            nombre = quitar_tildes(partes[0])
            apellido = quitar_tildes(partes[-1])
            numero = random.randint(10, 999)
            dominio = random.choice(dominios)
            correo = f"{nombre}.{apellido}{numero}@{dominio}"

            # Generamos más datos del usuario
            empresa = fake.company()
            puesto = fake.job()
            direccion = fake.address().replace("\n", ", ")
            telefono = fake.phone_number()
            descripcion = fake.text(max_nb_chars=100)

            # Mostramos toda la información en la ventana
            self.texto.append(f"USUARIO {i+1}")
            self.texto.append(f"Nombre: {nombre_completo}")
            self.texto.append(f"Correo: {correo}")
            self.texto.append(f"Empresa: {empresa}")
            self.texto.append(f"Puesto: {puesto}")
            self.texto.append(f"Dirección: {direccion}")
            self.texto.append(f"Teléfono: {telefono}")
            self.texto.append(f"Descripción: {descripcion}")
            self.texto.append("—" * 80 + "\n")

# Inicia la aplicación gráfica
app = QApplication(sys.argv)
ventana = Ventana()   # Creamos la ventana
ventana.show()        # La mostramos
sys.exit(app.exec_()) # Mantenemos la app activa