#Ejemplo Mexico 

#Importacion de las librerias
from faker import Faker
import random
import unicodedata

#Los datos generados seran basados en Mexico 
fake = Faker('es_MX')

#Delimitacion de dominios validos 
dominios = ['gmail.com', 'hotmail.com']

#Funcion para quitar las tildes de los nombres y apellidos que se
#usaran en el correo
def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )


for i in range(4):
    #Nombre del usuario
    nombre_completo = fake.name()
    #Convierte el nombre a minuscula y lo divide en partes
    partes = nombre_completo.lower().split()
    #Toma el primer nombre para formar el correo y si tiene tilde se la quita   
    nombre = quitar_tildes(partes[0]) 
    #Toma el primer apellido para formar el correo y si tiene tilde se la quita   
    apellido = quitar_tildes(partes[-1])
    numero = random.randint(10, 999)  # Toma un numero entre 10 y 999 para formar el correo

    #Seleccion aleatoria del dominio a utilizar
    dominio = random.choice(dominios)
    #Formacion del correo
    correo = f"{nombre}.{apellido}{numero}@{dominio}"
    #Empresa del usuario
    empresa = fake.company()
    #Puesto de trabajo del usuario
    puesto = fake.job()
    #Direccion del usuario
    direccion = fake.address().replace("\n", ", ")
    #Telefono del usuario
    telefono = fake.phone_number()
    descripcion = fake.text(max_nb_chars=100)

    print(f"USUARIO {i+1}")
    print("Nombre:", nombre_completo)
    print("Correo:", correo)
    print("Empresa:", empresa)
    print("Puesto:", puesto)
    print("Dirección:", direccion)
    print("Teléfono:", telefono)
    print("Descripción:", descripcion)
    print("—" * 80)