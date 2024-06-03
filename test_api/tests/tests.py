import requests
from test_api.src.enums.common import HttpErrorCodes

url = "https://petstore.swagger.io/v2/pet"


def test_delete_user_name():
    new_pet = {
        "id": 1,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "er",
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


    response = requests.post(url, json=new_pet)
    assert response.status_code == HttpErrorCodes.Ok
