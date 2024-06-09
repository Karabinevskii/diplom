from test_api.src.api.base_api import BaseApi


class PetApi(BaseApi):
    PATH = "/v2/pet"

    def post_pet_image(self, pet_id: int):
        return self._post(path=f"/{pet_id}/uploadFile")

    def add_new_pet(self, pet_id: int):
        return self._post(path=f"/{pet_id}")

    def update_pet(self, pet_id):
        return self._put(path=f"/{pet_id}")

    def find_pets_by_status(self, status):
        return self._get(path="/findByStatus", params={"status": status})

    def get_pet_by_id(self, pet_id: int):
        return self._get(path=f"/{pet_id}")

    def update_pet_with_form(self, pet_id: int):
        return self._post(path=f"/{pet_id}")

    def delete_pet(self, pet_id: int):
        return self._delete(path=f"/{pet_id}")
