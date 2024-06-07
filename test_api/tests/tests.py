import allure
import pytest
import requests
from test_api.src.enums.common import HttpErrorCodes

# url = "https://petstore.swagger.io/v2/pet"
#
#
# def test_delete_user_name():
#     new_pet = {
#         "id": 1,
#         "category": {
#             "id": 0,
#             "name": "string"
#         },
#         "name": "er",
#         "photoUrls": [
#             "string"
#         ],
#         "tags": [
#             {
#                 "id": 0,
#                 "name": "string"
#             }
#         ],
#         "status": "available"
#     }
#
#
#     response = requests.post(url, json=new_pet)
#     assert response.status_code == HttpErrorCodes.Ok
#
import pytest
import requests
import allure

base_url = "https://petstore.swagger.io/v2"


@pytest.mark.api
@allure.feature("Petstore API Tests")
class TestPetstoreAPI:
    @allure.title("Get Pet by ID Test")
    def test_get_pet_by_id(self):
        pet_id = 1
        response = requests.get(f"{base_url}/pet/{pet_id}")
        assert response.status_code == HttpErrorCodes.Ok
        pet_data = response.json()
        assert pet_data["id"] == pet_id

    @allure.title("Add a new Pet Test")
    def test_add_new_pet(self):
        new_pet_data = {
            "id": 1001,
            "name": "Max",
            "photoUrls": [],
            "status": "available"
        }
        response = requests.post(f"{base_url}/pet", json=new_pet_data)
        assert response.status_code == HttpErrorCodes.Ok

    @allure.title("Update Pet Status Test")
    def test_update_pet_status(self):
        pet_id = 1
        updated_status = "sold"
        response = requests.post(f"{base_url}/pet/{pet_id}", json={"status": updated_status})
        assert response.status_code == HttpErrorCodes.Ok
