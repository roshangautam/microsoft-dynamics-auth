"""
Microsoft Dynamics 356 authentication plugin for HTTPie.

"""

import os
import json

import requests.auth
from httpie.plugins import AuthPlugin
from adal import AuthenticationContext
from requests_oauthlib import oauth2_auth

__version__ = '0.0.1'
__author__ = 'Roshan Gautam'
__licence__ = 'MIT'


class MsftDynamicsAuth(oauth2_auth.OAuth2):
    authority = os.environ.get('AUTHORITY_URL')
    resource_url = os.environ.get('RESOURCE_URL')
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def __call__(self, request):
        context = AuthenticationContext(self.authority)
        response = context.acquire_token_with_client_credentials(self.resource_url, self.client_id, self.client_secret)
        request.headers['Authorization'] = 'Bearer %s' % response.get('accessToken').encode("ascii","ignore")
        return request

class MsftDynamicsAuthPlugin(AuthPlugin):
    name = 'Microsoft Dynamics 356 authentication plugin'
    auth_type = 'msft-dynamics'

    def get_auth(self, username, password):
        return MsftDynamicsAuth(username, password)

