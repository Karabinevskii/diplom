from io import BytesIO
import allure
import pytest
import requests
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from test_api.src.enums.common import HttpErrorCodes
from test_api.tests.tests import base_url


@pytest.mark.api
@allure.feature("Petstore API Tests")
class TestPetstoreAPI:

    @pytest.mark.parametrize("pet_id, file_name, expected_status_code", [
        (1, "test_image.png", 200),
        (1000, "test_image.png", 200),
    ])
    def test_upload_file(self, api_client, pet_id, file_name, expected_status_code):
        """
        Checking upload file
        """
        image = Image.new("RGB", (100, 100))
        image_io = BytesIO()
        image.save(image_io, "JPEG")
        image_io.seek(0)

        file = SimpleUploadedFile(
            name=file_name,
            content=image_io.read(),
            content_type="image/jpeg"
        )
        payload = {
            'file': file,
            'additionalMetadata': 'null'
        }

        with allure.step(f"Download file {file_name} for pet with ID {pet_id}"):
            response = requests.post(url=f"{base_url}/pet/{pet_id}/uploadImage", files=payload)

        with allure.step(f"Check status code: {response.status_code}"):
            assert response.status_code == expected_status_code

        if expected_status_code == HttpErrorCodes.Ok:
            with allure.step("Checking the contents of the response"):
                assert response.json()["code"] == HttpErrorCodes.Ok
                assert response.json()[
                           "message"] == 'additionalMetadata: null\nFile uploaded to ./test_image.png, 823 bytes'

    @pytest.mark.parametrize("name", ["Altai", "Baltai", "Shaltai"])
    @pytest.mark.parametrize("pet_id", [1002, 345, 1598])
    def test_add_new_pet(self, name, pet_id, api_client):
        """
        This function allows you to add a new pet to the storage
        :param api_client:
        :param name:
        :param pet_id:
        :return:
        """
        with allure.step("Add new pet"):
            new_pet = {
                "pet_id": pet_id,
                "name": name,
                "photoUrls": [],
                "status": "available"
            }
        with allure.step("Request to add a new pet"):
            add_response = requests.post(f"{base_url}/pet",
                                         headers={"accept": "application/json",
                                                  "Content-Type": "application/json"},
                                         json=new_pet)

        with allure.step("Check answer"):
            assert add_response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {add_response.status_code}"

        with allure.step("Check pet name"):
            assert add_response.json()["name"] == name

        with allure.step("Check status"):
            assert add_response.json()["status"] == "available"

        get_response = api_client.pet.get_pet_by_id(pet_id)
        assert get_response.status_code == HttpErrorCodes.NotFound, f"Wrong code: {get_response.status_code}"


    @pytest.mark.parametrize("pet_id, name, status, expected_status_code",
                             [
                                 (1, "Altai", "available", HttpErrorCodes.Ok),
                                 (2, "Baltai", "pending", HttpErrorCodes.Ok),
                                 (3, "Shaltai", "sold", HttpErrorCodes.NotFound),
                             ]
                             )
    @allure.title("Update Pet with Form Test")
    def test_update_pet_with_form(self, api_client, pet_id, name, status, expected_status_code):
        """
        This function tests the Update Pet with Form API
        :param pet_id: ID of the pet to update
        :param name: New name for the pet
        :param status: New status for the pet
        :param expected_status_code: Expected status code of the response
        :return:
        """

        with allure.step(f"Update pet with ID '{pet_id}'"):
            post_response = api_client.pet.update_pet_with_form(pet_id)
            assert post_response.status_code == expected_status_code

    @allure.title("Find Pets by Status Test")
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_find_by_status(self, api_client, status):
        get_response = api_client.pet.find_pets_by_status(status)
        with allure.step("Check status code"):
            assert get_response.status_code == HttpErrorCodes.Ok, f"Wrong status code: {get_response.status_code}"

    @allure.title("Get Pet by ID")
    @pytest.mark.parametrize("pet_id, expected_status_code", [
        (1, HttpErrorCodes.Ok),
        (1000, HttpErrorCodes.NotFound),
    ])
    def test_get_pet_by_id(self, pet_id, expected_status_code, api_client):
        """
        API test for getting information about a pet by ID.
        :param pet_id:
        :param expected_status_code:
        :param api_client:
        :return:
        """
        with allure.step(f"Request to receive a pet with an ID {pet_id}"):
            get_response = api_client.pet.get_pet_by_id(pet_id)

        if expected_status_code == HttpErrorCodes.Ok:
            response = get_response.json()
            with allure.step("Checking the contents of the response"):
                assert response['id'] == pet_id
            with allure.step("Check name is not empty"):
                assert response['name'] is not None
            with allure.step("Check status is not empty"):
                assert response['status'] is not None

    @pytest.mark.parametrize("pet_id, name, status, expected_status_code",
                             [
                                 (1, "Altai", "available", HttpErrorCodes.Ok),
                                 (2, "Baltai", "pending", HttpErrorCodes.Ok),
                                 (3, "Shaltai", "sold", HttpErrorCodes.NotFound),
                             ]
                             )
    @allure.title("Update Pet with Form Test")
    def test_update_pet_with_form(self, api_client, pet_id, name, status, expected_status_code):
        """
        This function tests the Update Pet with Form API
        :param pet_id: ID of the pet to update
        :param name: New name for the pet
        :param status: New status for the pet
        :param expected_status_code: Expected status code of the response
        :return:
        """

        with allure.step(f"Update pet with ID '{pet_id}'"):
            post_response = api_client.pet.update_pet_with_form(pet_id)
            assert post_response.status_code == expected_status_code

    @pytest.mark.parametrize("pet_id, api_key, expected_status_code",
                             [
                                 (1, "api_key", HttpErrorCodes.Ok),
                                 (2, "api_key", HttpErrorCodes.Ok),
                                 (3, "api_key", HttpErrorCodes.NotFound),
                             ]
                             )
    @allure.title("Delete Pet Test")
    def test_delete_pet(self, api_client, pet_id, api_key, expected_status_code):
        """
        This function tests the Delete Pet API
        :param pet_id: to delete
        :param api_key: API
        :param expected_status_code:
        :return:
        """
        with allure.step(f"Delete pet with ID '{pet_id}'"):
            del_response = api_client.pet.delete_pet(pet_id)

        with allure.step("Check status code"):
            assert del_response.status_code == expected_status_code, \
                f"Expected status code {expected_status_code}, received {del_response.status_code}"
