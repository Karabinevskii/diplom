from io import BytesIO
import allure
import pytest
import requests
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from test_api.src.enums.common import HttpErrorCodes

base_url = "https://petstore.swagger.io/v2"


@pytest.mark.api
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
                json=updated_pet
            )

        with allure.step("Check status code"):
            assert put_response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {put_response.status_code}"

        with allure.step("Check the pets name"):
            get_response = requests.get(f"{base_url}/pet/1")
            assert get_response.json()["name"] == expected_name, f"The pet's name does not match the expected one: {get_response.json()["name"]}"


    def test_find_pets_by_status(self):
        """
        Тест API для получения списка питомцев по статусу.
        """
        url = "https://petstore.swagger.io/v2/pet/findByStatus"
        status = "available"  # Укажите желаемый статус питомца

        headers = {
            "accept": "application/json",
        }

        params = {
            "status": status,
        }

        response = requests.get(url, headers=headers, params=params)

        # Проверьте статус-код ответа
        assert response.status_code == HttpErrorCodes.Ok, f"Неверный статус-код: {response.status_code}"

        # Проверьте, что ответ содержит список питомцев
        data = response.json()
        assert isinstance(data, list), "Ответ не является списком"

        # Проверьте, что все питомцы в списке имеют заданный статус
        for pet in data:
            assert pet[
                       "status"] == status, f"Питомец со статусом {pet['status']} не соответствует ожидаемому статусу {status}"

        print("Тест пройден успешно!")

    @allure.title("Get Pet by ID Test")
    def test_get_pet_by_id(self):
        """
        API test for adding a new pet
        :return:
        """
        pet_id = 1
        response = requests.get(f"{base_url}/pet/{pet_id}")
        assert response.status_code == HttpErrorCodes.Ok
        pet_data = response.json()
        assert pet_data["id"] == pet_id
