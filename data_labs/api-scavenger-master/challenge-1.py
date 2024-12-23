# enter your code below pls
# happy coding!

import os
from dotenv import load_dotenv
import requests
load_dotenv()

print("Hola")
url= "https://api.github.com/repos/ironhack-datalabs/datamad1020-rev/forks"

print(os.getenv("token"))
api_key = os.getenv("token")
parameters = {"Auhorization" : f"token {api_key}"}

#print(parameters)

response = requests.get( url = url, params = parameters).json()
#print(response)

"""
def requestGithub(url):
    token = os.getenv("token")
    if not token:
        raise ValueError ("Necesitas un token")
    print(f"Haciendo request a {url}")
    
    params = {"Auhorization" : f"token {api_key}"}
    response = requests.get( url = url , params = params).json()
    
    return response
"""

print(response[0]["full_name"])
