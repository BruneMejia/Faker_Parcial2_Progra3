from faker import Faker
import random
fake = Faker()

ejCorreo = ['gmail.com', 'hotmail.com']


for i in range(1):
    nombre = fake.name()
    usuario = fake.user_name()
    ejCorreo = random.choice(ejCorreo)
    correo = f"{usuario}@{ejCorreo}"

    print("Nombre:", nombre)
    print("Correo:", correo)
    print("Dirrección:",fake.address())
    print("----------")