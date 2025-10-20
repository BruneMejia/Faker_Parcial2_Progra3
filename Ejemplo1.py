#Codigo base

#Importacion de la libreria
from faker import Faker

fake = Faker('ja_JP')

for i in range(4):
    print("Nombre:", fake.name())
    print("Correo:", fake.email())
    print("Dirrección:",fake.address())
    print("----------------------------------")