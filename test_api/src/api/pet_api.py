
from test_api.src.api.base_api import BaseApi


class PetApi(BaseApi):
    PATH = "/v2/pet"


    def post_pet_image(self, pet_id: int):
        return self._get(path=f"/{pet_id}/uploadFile")

    def get_pet_by_id(self, pet_id: int):
        return self._get(path=f"/{pet_id}")
