import requests



class BaseApi:
    url = "https://petstore.swagger.io"

    def _post(self, id: int = None, params: dict = None):


        if headers is not None:
            default_headers.update(headers)

