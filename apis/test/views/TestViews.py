import pytest
from rest_framework import status
from rest_framework.test import APIClient

@pytest.fixture
def client():
    """Inicializa un cliente de prueba para enviar solicitudes."""
    return APIClient()

@pytest.mark.asyncio
async def test_get_endpoint_post(client):
    """Prueba la vista de 'get-endpoint' en POST."""
    response = await client.post('/apis/get-endpoint/', {})
    
    print("Response:", response)
    # Verifica que la respuesta sea exitosa (código 200 OK)
    assert response.status_code == status.HTTP_200_OK
    # Puedes agregar más aserciones aquí según lo que desees verificar.
