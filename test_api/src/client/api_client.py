from test_api.src.api.pet_api import PetApi



class ApiClient:

    def __init__(self):
        self.pet: PetApi = PetApi()