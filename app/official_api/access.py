import os
import requests
import dotenv
from auth import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET

AUTH_CODE = "AQQqPMJQPkfO0_he1ema0_fQnfwGK76IIL-tn6NH9QblQ6zi7i8oNOo6qn2hKPzvHGQcuseL0-dYwgLZ72sGZA2n9yD2ndXc2jBRO1LFf62DR1lbz9g8z-vpCuYplRFk60LRoVvNUP6Sqai46u-iV1o3siNFNPkguCbG8uqH6xjAS7nEouAl65v1AY3iZA"

ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

qd = {'grant_type': 'authorization_code',
      'code': AUTH_CODE,
      'redirect_uri': REDIRECT_URI,
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET}

response = requests.post(ACCESS_TOKEN_URL, data=qd, timeout=60)

response = response.json()
import ipdb; ipdb.set_trace()

access_token = response['access_token']

print ("Access Token:", access_token)
print ("Expires in (seconds):", response['expires_in'])