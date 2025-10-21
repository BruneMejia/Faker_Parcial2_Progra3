# -------------------------------
#Ejercicio 3: Este programa genera información falsa de usuarios, incluyendo nombre, correo electrónico y dirección completa en El Salvador.
#Utiliza la librería Faker y una clase personalizada para crear direcciones realistas.
#También limpia los nombres de tildes para formar correos válidos.
# -------------------------------

# Importación de librerías
from faker import Faker
from faker.providers import BaseProvider
import random
import unicodedata
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

# Clase personalizada para generar direcciones de El Salvador
class ElSalvadorProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.data = {
            "Ahuachapán": {
                "Ahuachapán": ["Colonia El Carmen", "Colonia Las Flores", "Colonia El Progreso"],
                "Atiquizaya": ["Colonia Las Flores", "Barrio San Pedro", "Colonia El Rosario"],
                "Apaneca": ["Barrio San Pedro", "Colonia San Juan", "Barrio El Calvario"]
            },
            "Cabañas": {
                "Sensuntepeque": ["Barrio El Calvario", "Colonia El Centro", "Colonia Los Ángeles"],
                "Ilobasco": ["Colonia San José", "Colonia Los Pinos", "Colonia San Martín"],
                "Victoria": ["Colonia Los Ángeles", "Barrio San Rafael", "Colonia Santa Lucía"]
            },
            "Chalatenango": {
                "Chalatenango": ["Colonia Santa Lucía", "Colonia El Paraíso", "Colonia La Esperanza"],
                "Nueva Concepción": ["Colonia Los Pinos", "Colonia Jardines del Río", "Barrio La Cruz"],
                "La Palma": ["Barrio El Rosario", "Barrio El Carmen", "Colonia Los Robles"]
            },
            "Cuscatlán": {
                "Cojutepeque": ["Colonia Santa Eduviges", "Colonia San Rafael", "Colonia Las Flores"],
                "Suchitoto": ["Barrio El Centro", "Colonia San Antonio", "Barrio Santa Lucía"],
                "San Rafael Cedros": ["Colonia Los Olivos", "Colonia El Progreso", "Barrio San José"]
            },
            "La Libertad": {
                "Santa Tecla": ["Colonia Quezaltepeque", "Colonia San Benito", "Colonia Primavera"],
                "Antiguo Cuscatlán": ["Colonia Escalón", "Colonia Jardines del Volcán", "Colonia Miramonte"],
                "Zaragoza": ["Colonia Altos del Cerro", "Colonia San Jorge", "Colonia Las Brisas"]
            },
            "La Paz": {
                "Zacatecoluca": ["Colonia San Rafael", "Colonia San José", "Colonia Santa Ana"],
                "Olocuilta": ["Colonia San Luis", "Barrio El Calvario", "Colonia Las Margaritas"],
                "Santiago Nonualco": ["Barrio Concepción", "Colonia San Pablo", "Barrio El Carmen"]
            },
            "La Unión": {
                "La Unión": ["Colonia El Molino", "Colonia San Carlos", "Colonia Jardines del Puerto"],
                "Santa Rosa de Lima": ["Barrio El Centro", "Colonia Los Pinos", "Colonia San José"],
                "Conchagua": ["Colonia Las Brisas", "Colonia El Sol", "Barrio El Calvario"]
            },
            "Morazán": {
                "San Francisco Gotera": ["Colonia Jardines del Río", "Colonia El Milagro", "Colonia El Bosque"],
                "Jocoro": ["Colonia La Esperanza", "Barrio El Rosario", "Colonia Santa Cruz"],
                "Corinto": ["Barrio San Antonio", "Barrio La Paz", "Colonia El Carmen"]
            },
            "San Miguel": {
                "San Miguel": ["Colonia Ciudad Jardín", "Colonia Las Brisas", "Colonia Santa Julia"],
                "Chinameca": ["Colonia Las Rosas", "Colonia El Bosque", "Barrio San José"],
                "Moncagua": ["Colonia El Mirador", "Barrio El Calvario", "Colonia San Carlos"]
            },
            "San Salvador": {
                "Mejicanos": ["Colonia Zacamil", "Colonia San Roque", "Colonia Miramonte"],
                "San Salvador": ["Colonia Escalón", "Colonia Médica", "Colonia Flor Blanca"],
                "Soyapango": ["Colonia Guadalupe", "Colonia Las Margaritas", "Colonia San Ernesto"]
            },
            "San Vicente": {
                "San Vicente": ["Colonia Santa Teresa", "Colonia San Antonio", "Barrio El Calvario"],
                "Tecoluca": ["Colonia San José", "Colonia El Rosario", "Colonia El Bosque"],
                "Apastepeque": ["Barrio El Centro", "Colonia La Paz", "Colonia Los Pinos"]
            },
            "Santa Ana": {
                "Santa Ana": ["Colonia Altamira", "Colonia San Luis", "Colonia El Palmar"],
                "Metapán": ["Barrio El Carmen", "Colonia San Pedro", "Colonia La Vega"],
                "Chalchuapa": ["Colonia San Sebastián", "Barrio Santa Cruz", "Colonia El Paraíso"]
            },
            "Sonsonate": {
                "Izalco": ["Colonia Las Palmeras", "Colonia Santa Fe", "Colonia Los Ángeles"],
                "Sonzacate": ["Colonia Miramar", "Colonia San Francisco", "Colonia Jardines del Sol"],
                "Nahuizalco": ["Barrio San Juan", "Colonia Los Pinos", "Barrio La Merced"]
            },
            "Usulután": {
                "Usulután": ["Colonia San Antonio", "Colonia San Rafael", "Colonia Los Almendros"],
                "Jiquilisco": ["Colonia Las Margaritas", "Colonia San José", "Colonia El Progreso"],
                "Santiago de María": ["Barrio El Calvario", "Colonia El Carmen", "Colonia Santa Julia"]
            }
        }
    
    def departamento(self):
        return self.random_element(list(self.data.keys()))

    def ciudad(self, departamento):
        return self.random_element(list(self.data[departamento].keys()))

    def colonia(self, departamento, ciudad):
        return self.random_element(self.data[departamento][ciudad])

    def direccion_completa(self):
        departamento = self.departamento()
        ciudad = self.ciudad(departamento)
        colonia = self.colonia(departamento, ciudad)
        calle = f"Calle {self.generator.last_name()} #{random.randint(1, 200)}"
        return f"{calle}, {colonia}, {ciudad}, {departamento}, El Salvador"

# Inicializar Faker y añadir nuestro proveedor
fake = Faker('es_MX')
fake.add_provider(ElSalvadorProvider)

# Dominios de correo válidos
dominios = ['gmail.com', 'hotmail.com']

# Función para quitar tildes
def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )


# Interfaz gráfica

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Usuarios Falsos de El Salvador")
        self.setGeometry(300, 200, 600, 400)

        # Layout principal
        self.layout = QVBoxLayout()

        # Botón para generar usuarios
        self.boton_generar = QPushButton("Generar Usuarios")
        self.boton_generar.clicked.connect(self.generar_usuarios)
        self.layout.addWidget(self.boton_generar)

        # Área de texto para mostrar los usuarios
        self.area_texto = QTextEdit()
        self.area_texto.setReadOnly(True)
        self.layout.addWidget(self.area_texto)

        self.setLayout(self.layout)

    def generar_usuarios(self):
        self.area_texto.clear()
        for i in range(4):
            nombre_completo = fake.name()
            partes = nombre_completo.lower().split()
            nombre = quitar_tildes(partes[0])
            apellido = quitar_tildes(partes[-1])
            numero = random.randint(10, 999)
            dominio = random.choice(dominios)
            correo = f"{nombre}.{apellido}{numero}@{dominio}"
            direccion = fake.direccion_completa()

            self.area_texto.append(f"USUARIO {i+1}")
            self.area_texto.append(f"Nombre: {nombre_completo}")
            self.area_texto.append(f"Correo: {correo}")
            self.area_texto.append(f"Dirección: {direccion}")
            self.area_texto.append("---------------------------------------")


# Ejecución principal

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()
