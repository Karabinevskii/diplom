from io import BytesIO
import allure
import pytest
import requests
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from test_api.src.enums.common import HttpErrorCodes

base_url = "https://petstore.swagger.io/v2"



@allure.feature("Petstore API Tests")
class TestPetstoreAPI:

    @allure.title("Test uploading a file")
    @pytest.mark.parametrize("pet_id", [1, 2, 3])
    def test_upload_file(self, pet_id: int):
        """
        Тест API для загрузки файла с использованием UploadImage.
        """
        url = f"{base_url}/pet/{pet_id}/uploadImage"

        image_data = BytesIO()
        image = Image.new('RGB', (100, 100), 'white')
        image.save(image_data, format='png')
        image_data.seek(0)

        file = SimpleUploadedFile("test_image.png", image_data.read(), content_type='image/png')

        payload = {
            'file': file,
            'additionalMetadata': 'null'
        }

        with allure.step("Sending a file download request"):
            response = requests.post(url, files=payload)

        with allure.step("Check status code"):
            assert response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {response.status_code}"

        data = response.json()
        assert data[
                   'message'] == 'additionalMetadata: null\nFile uploaded to ./test_image.png, 289 bytes', f"Wrong message: {data['message']}"
        assert data['code'] == HttpErrorCodes.Ok, f"Wrong code: {data['code']}"

    @pytest.mark.parametrize("name", ["Altai", "Baltai", "Shaltai"])
    @pytest.mark.parametrize("pet_id", [1002, 5, 1598])
    def test_add_new_pet(self, name, pet_id):
        """
        This feature allows you to add a new pet to the storage
        :param name:
        :param pet_id:
        :return:
        """
        with allure.step("Add new pet"):
            new_pet = {
                "pet_id": 1001,
                "name": "Altai",
                "photoUrls": [],
                "status": "available"
            }
        with allure.step("Request to add a new pet"):
            response = requests.post(f"{base_url}/pet",
                                     headers={"accept": "application/json",
                                              "Content-Type": "application/json"},
                                     json=new_pet)
        with allure.step("Check answer"):
            assert response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {response.status_code}"

        with allure.step("Check pet name"):
            assert response.json()["name"] == "Altai"

        with allure.step("Check status"):
            assert response.json()["status"] == "available"

        get_response = requests.get(f"{base_url}",
                                    headers={"accept": "application/json",
                                             "Content-Type": "application/json"},
                                    )
        assert get_response.status_code == HttpErrorCodes.NotFound, f"Wrong code: {get_response.status_code}"

    @pytest.mark.parametrize("new_name, expected_name",
                             [
                                 ("Altai", "Altai"),
                                 ("Baltai", "Baltai"),
                                 ("Shaltai", "Shaltai")
                             ]
                             )
    @allure.title("Update Pet Status Test")
    def test_update_pet(self, new_name, expected_name):
        """
        This function updates the pet's name
        :param new_name, expected_name:
        :return:
        """
        updated_pet = {
            "id": 1,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": new_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        with allure.step("Update pets name"):
            put_response = requests.put(
                url=f"{base_url}/pet",
                headers={"accept": "application/json",
                         "Content-Type": "application/json"},
                json=updated_pet
            )

        with allure.step("Check status code"):
            assert put_response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {put_response.status_code}"

        with (allure.step("Check the pets name")):
            get_response = requests.get(f"{base_url}/pet/1")
            assert get_response.json()["name"] == expected_name, \
                f"The pet's name doesn't match the expected one: {get_response.json()["name"]}"

    @allure.title("Find Pets by Status Test")
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_find_pets_by_status(self, status):
        """
        This function tests find Pets by Status
        :param status:
        :return:
        """
        with allure.step(f"Get pets with status '{status}'"):
            get_response = requests.get(
                url=f"{base_url}/pet/findByStatus",
                headers={"accept": "application/json",
                         "Content-Type": "application/json"},
                params={"status": status}
            )

        with allure.step("Check status code"):
            assert get_response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {get_response.status_code}"

    @allure.title("Get Pet by ID")
    @pytest.mark.parametrize("pet_id, expected_status_code", [
        (1, HttpErrorCodes.Ok),
        (1000, HttpErrorCodes.NotFound),
    ])
    def test_get_pet_by_id(self, pet_id, expected_status_code):
        """
        API test for getting information about a pet by ID.
        """
        with allure.step(f"Request to receive a pet with an ID {pet_id}"):
            get_response = requests.get(
                url=f"{base_url}/pet/{pet_id}"
            )

        with allure.step("Check status code"):
            assert get_response.status_code == expected_status_code

        if expected_status_code == HttpErrorCodes.Ok:
            with allure.step("Checking the contents of the response"):
                assert get_response.json()['id'] == pet_id
            with allure.step("Check name is not empty"):
                assert get_response.json()['name'] is not None
            with allure.step("Check status is not empty"):
                assert get_response.json()['status'] is not None

    @pytest.mark.parametrize("pet_id, name, status, expected_status_code",
                             [
                                 (1, "Altai", "available", HttpErrorCodes.Ok),
                                 (2, "Baltai", "pending", HttpErrorCodes.Ok),
                                 (3, "Shaltai", "sold", HttpErrorCodes.NotFound),
                             ]
                             )
    @allure.title("Update Pet with Form Test")
    def test_update_pet_with_form(self, pet_id, name, status, expected_status_code):
        """
        This function tests the Update Pet with Form API
        :param pet_id: ID of the pet to update
        :param name: New name for the pet
        :param status: New status for the pet
        :param expected_status_code: Expected status code of the response
        :return:
        """
        with allure.step(f"Update pet with ID '{pet_id}'"):
            response = requests.post(
                url=f"{base_url}/pet/{pet_id}",
                data={"name": name, "status": status}
            )

        with allure.step("Check status code"):
            assert response.status_code == expected_status_code, f"Expected status {expected_status_code}, \
             status code received{response.status_code}"

        if expected_status_code == HttpErrorCodes.Ok:
            with allure.step("Get updated pet by ID"):
                get_response = requests.get(
                    url=f"{base_url}/pet/{pet_id}"
                )

            with allure.step("Check updated name"):
                assert get_response.json()[
                           "name"] == name, f"The pet's name has not been updated, it was expected '{name}',  received '{get_response.json()['name']}'"

            with allure.step("Check updated status"):
                assert get_response.json()[
                           "status"] == status, f"The status of the pet has not been updated, it was expected '{status}', received '{get_response.json()['status']}'"

    @pytest.mark.parametrize("pet_id, api_key, expected_status_code",
                             [
                                 (1, "api_key", HttpErrorCodes.Ok),
                                 (2, "api_key", HttpErrorCodes.Ok),
                                 (3, "api_key", HttpErrorCodes.NotFound),
                             ]
                             )
    @allure.title("Delete Pet Test")
    def test_delete_pet(self, pet_id, api_key, expected_status_code):
        """
        This function tests the Delete Pet API
        :param pet_id: to delete
        :param api_key: API
        :param expected_status_code:
        :return:
        """
        with allure.step(f"Delete pet with ID '{pet_id}'"):
            response = requests.delete(
                url=f"{base_url}/pet/{pet_id}",
                headers={"api_key": api_key}
            )

        with allure.step("Check status code"):
            assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, received {response.status_code}"
