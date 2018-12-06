from microsoftgraph import auth
from unittest.mock import call, patch
import unittest


class TestClient(unittest.TestCase):
    @patch('adal.AuthenticationContext')
    def test_create_client_with_username_password(self, adal_AuthenticationContext):
        tenant = 'contoso.onmicrosoft.com'
        username = 'test@example.com'
        password = 'test'
        client_id = 'testclientid'
        
        auth.Client.create_client_with_username_password(tenant, client_id, username, password)

        self.assertEqual(adal_AuthenticationContext.mock_calls, [call(auth.BASE_LOGIN_URI + tenant),
            call().acquire_token_with_username_password(auth.RESOURCE_URI, username, password, client_id=client_id)])

if __name__ == '__main__':
    unittest.main()


