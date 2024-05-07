import pytest
import requests
from lambda_forge.constants import BASE_URL


@pytest.mark.integration(method="GET", endpoint="/pool")
def test_list_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/pool")

    assert response.status_code == 200
