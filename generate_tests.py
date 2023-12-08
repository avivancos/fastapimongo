# generate_tests.py

import os
import argparse

def generator(module_name):
    # Generar el código de las pruebas
    tests_code = f"""
import pytest
import httpx

@pytest.fixture
def client():
    with httpx.Client(base_url='http://localhost:8000') as c:
        yield c

def test_create(client):
    # Aquí iría el código de la prueba para la operación de creación
    response = client.post('/{module_name}', json={{...}})
    assert response.status_code == 200
    assert 'id' in response.json()

def test_read(client):
    # Aquí iría el código de la prueba para la operación de lectura
    response = client.get(f'/{module_name}/{{id}}')
    assert response.status_code == 200

def test_read_all(client):
    # Aquí iría el código de la prueba para la operación de lectura de todos los elementos
    response = client.get(f'/{module_name}')
    assert response.status_code == 200

def test_update(client):
    # Aquí iría el código de la prueba para la operación de actualización
    response = client.put(f'/{module_name}/{{id}}', json={{...}})
    assert response.status_code == 200

def test_delete(client):
    # Aquí iría el código de la prueba para la operación de eliminación
    response = client.delete(f'/{module_name}/{{id}}')
    assert response.status_code == 200
    """

    # Crear y guardar los archivos de prueba en el directorio de pruebas
    with open(f'tests/test_{module_name}_router.py', 'w') as file:
        file.write(tests_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CRUD tests for a module.")
    parser.add_argument("module_name", type=str, help="Name of the module for which to generate tests")
    args = parser.parse_args()
    generator(args.module_name)