"""
Microsoft Dynamics 356 authentication plugin for HTTPie.

"""

import sys, os
import json
import re
import argparse
import ConfigParser
from os.path import expanduser
import requests.auth
from httpie.plugins import AuthPlugin
from adal import AuthenticationContext
from requests_oauthlib import oauth2_auth

__author__ = 'Roshan Gautam'
__licence__ = 'MIT'


class MsftDynamicsAuth(oauth2_auth.OAuth2):
    def __init__(self, section, password):
        config = ConfigParser.ConfigParser()
        config.read("/Users/rogautam/.parc")
        self.client_id = config.get(section, 'key')
        self.client_secret = config.get(section, 'secret')
        self.resource_url = config.get(section, 'resource')
        self.authority = os.environ.get('AUTHORITY_URL')

    def __call__(self, request):
        context = AuthenticationContext(self.authority)
        response = context.acquire_token_with_client_credentials(self.resource_url, self.client_id, self.client_secret)
        request.headers['Authorization'] = 'Bearer %s' % response.get('accessToken')
        return request

class MsftDynamicsAuthPlugin(AuthPlugin):
    name = 'Microsoft Power Platform Authentication Plugin'
    auth_type = 'msft-power-platform'
    description = "Httpie2 auth plugin for Microsoft Power Platform"

    def get_auth(self, username, password):
        return MsftDynamicsAuth(username, "")

