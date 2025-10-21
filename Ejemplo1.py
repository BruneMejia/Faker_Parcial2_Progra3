# ------------------------------------------------------------
# Ejercicio 1: Generador de datos falsos con interfaz gráfica
# Este programa usa la librería Faker para crear nombres, correos y direcciones
# y los muestra en una ventana usando PyQt5.
# ------------------------------------------------------------

# Importamos las librerías necesarias para la generación de datos y la interfaz gráfica
#Las librerías necesarias son Faker para los datos falsos y PyQt5 para la interfaz gráfica.
from faker import Faker
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
import sys

# Creamos una instancia de Faker con datos 
# configuración por defecto
# Inicializamos Faker sin un local específico para datos genéricos.
fake = Faker()

# Creamos la clase principal de la ventana
# Aquí creamos una ventana con PyQt5 que permita generar y mostrar los datos falsos de usuarios.
# Esta ventana tendrá un botón para generar los datos y un área de texto para mostrarlos.
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos falsos")  # Título de la ventana
        self.resize(500, 400)  # Tamaño de la ventana
        
        layout = QVBoxLayout()  # Diseño vertical (de arriba a abajo)

        # Cuadro de texto donde se mostrarán los datos
        # Área de texto para mostrar los datos generados
        self.texto = QTextEdit()
        
        # Botón que generará los datos al hacer clic
        boton = QPushButton("Generar datos")
        boton.clicked.connect(self.generar_datos)  # Conectamos el botón con la función

        # Agregamos los elementos al diseño
        layout.addWidget(self.texto)
        layout.addWidget(boton)
        self.setLayout(layout)

    # Función que genera y muestra los datos falsos
    def generar_datos(self):
        self.texto.clear()  # Limpia el cuadro antes de mostrar nuevos datos
        for i in range(5):  # Genera 5 registros
            nombre = fake.name()
            correo = fake.email()
            direccion = fake.address().replace("\n", ", ")  # Quita saltos de línea
            # Muestra los datos en el cuadro de texto
            self.texto.append(f" {nombre}\n {correo}\n {direccion}\n{'-'*40}")

# Inicia la aplicación
app = QApplication(sys.argv)
ventana = Ventana()  # Crea una instancia de la ventana
ventana.show()       # Muestra la ventana
sys.exit(app.exec_())  # Mantiene la aplicación en ejecución
