"""
Example presents usage of the successful compilers() API method
"""
from sphere_engine import CompilersClientV4
from sphere_engine.exceptions import SphereEngineException

# define access parameters
accessToken = '<access_token>'
endpoint = '<endpoint>'

# initialization
client = CompilersClientV4(accessToken, endpoint)

# API usage
try:
    response = client.compilers()
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')
