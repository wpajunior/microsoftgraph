import adal
from microsoftgraph.resources.groups import Groups
import requests
import uuid


BASE_LOGIN_URI = 'https://login.microsoftonline.com/'
RESOURCE_URI = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'

class Client:
    """ Microsoft Graph client class """

    def __init__(self, token):
        """ Constructs a client with a access token

        :param token: Access token
        :type token: str
        """
        self.token = token
        self.__http_headers = self.__create_http_headers()

        self.groups = Groups(self)

    @classmethod
    def create_client_with_username_password(cls, tenant, client_id, username, password):
        """Construct a Microsoft Graph class with username and passowrd

        :param tenant: Azure tenant. Ex.: contoso.onmicrosoft.com
        :type tenant: str
        :param client_id: Application id
        :param username: Username used on authentication
        :type username: str
        :param password: Password used on authentication
        :type password: str
        :returns: Client class: authenticated client instance
        :rtype: Client class instance
        :raises: adal.adal_error.AdalError
        """
        authority = BASE_LOGIN_URI + tenant
        auth_context = adal.AuthenticationContext(authority)
        token = auth_context.acquire_token_with_username_password(RESOURCE_URI, username, password, client_id=client_id)

        return cls(token)
    
    def get(self, path):
        response = requests.get(RESOURCE_URI + API_VERSION + path, headers=self.__http_headers, stream=False).json()
        return response
    
    def get_collection(self, path):
        return self.get(path)['value']
    
    def post(self, path, body):
        response = requests.post(RESOURCE_URI + API_VERSION + path, headers=self.__http_headers, json=body, stream=False)
        
        if response.status_code != 201:
            raise Exception(response.text)
        
        return response.json()

    
    def __create_http_headers(self):
        return {'Authorization': 'Bearer ' + self.token['accessToken'],
                'User-Agent': 'python',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'client-request-id': str(uuid.uuid4())}


