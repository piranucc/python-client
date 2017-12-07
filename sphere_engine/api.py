# coding: utf-8

"""
Sphere Engine API

@copyright  Copyright (c) 2015 Sphere Research Labs (http://sphere-research.com)
"""

from .apis.compilers import CompilersApi
from .apis.compilersV4 import CompilersApiV4
from .apis.problems import ProblemsApi
from .apis.problemsV4 import ProblemsApiV4
from .api_client import ApiClient

class CompilersClientV3(CompilersApi):
    """
    Client for Sphere Engine Compilers - version 3
    """

    _version = 'v3'
    _access_token = None
    _endpoint = None

    def __init__(self, access_token, endpoint):
        """
        :param access_token: string
        :param endpoint: string
        """

        self._access_token = access_token
        self._endpoint = endpoint
        api_client = ApiClient(self._access_token, self._endpoint, self._version, 'compilers')

        CompilersApi.__init__(self, api_client)

class ProblemsClientV3(ProblemsApi):
    """
    Client for Sphere Engine Problems - version 3
    """

    _version = 'v3'
    _access_token = None
    _endpoint = None

    def __init__(self, access_token, endpoint):
        """
        :param access_token: string
        :param endpoint: string
        """

        self._access_token = access_token
        self._endpoint = endpoint
        api_client = ApiClient(self._access_token, self._endpoint, self._version, 'problems')

        ProblemsApi.__init__(self, api_client)
        
class CompilersClientV4(CompilersApiV4):
    """
    Client for Sphere Engine Compilers - version 4
    """
    
    _version = 'v4'
    _access_token = None
    _endpoint = None

    def __init__(self, access_token, endpoint):
        """
        :param access_token: string
        :param endpoint: string
        """
        
        self._access_token = access_token
        self._endpoint = endpoint
        api_client = ApiClient(self._access_token, self._endpoint, self._version, 'compilers')

        CompilersApiV4.__init__(self, api_client)
        
class ProblemsClientV4(ProblemsApiV4):
    """
    Client for Sphere Engine Problems - version 4
    """
    
    _version = 'v4'
    _access_token = None
    _endpoint = None

    def __init__(self, access_token, endpoint):
        """
        :param access_token: string
        :param endpoint: string
        """
        
        self._access_token = access_token
        self._endpoint = endpoint
        api_client = ApiClient(self._access_token, self._endpoint, self._version, 'problems')

        ProblemsApiV4.__init__(self, api_client)
