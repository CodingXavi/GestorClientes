import helpers
import re

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'nsocio': '1547M'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'nsocio': '9091H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'nsocio': '9092H'})


def show(client):
    print(f"{client['nsocio']}: {client['nombre']} {client['apellido']}")


def show_all():
    for client in clients:
        show(client)

def find():

    socio = input("Introduce el socio del cliente\n> ")

    for i, client in enumerate(clients):
        if client['nsocio'] == socio:
            show(client)
            return i, client

    print("No se ha encontrado ningún cliente con ese socio")
    helpers.clear()
    volver = input("¿ Desea buscar otro cliente ?")
    if volver == "si":
        find()

def is_valid(socio):
    """
    >>> is_valid('48H')  # No válido, en uso
    False
    >>> is_valid('X82')  # No válido, incorrecto
    False
    >>> is_valid('21A')  # Válido
    True
    """
    # Comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{4}[A-Z]', socio):
        return False

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['nsocio'] == socio:
            return False

    return True

def add():

    client = dict()

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce nsocio (4 números y 1 carácter en mayúscula)")
        socio = helpers.input_text(5, 5)
        if is_valid(socio):
            client['nsocio'] = socio
            break
        print("nsocio incorrecto o en uso")

    clients.append(client)
    return client

def edit():

    i, client = find()

    if client:

        print(f"Introduce nuevo nombre ({client['nombre']})")
        clients[i]['nombre'] = helpers.input_text(2, 30)

        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2, 30)
        return True

    return False

def delete():

    i, client = find()

    if client:
        client = clients.pop(i)
        return True

    return False