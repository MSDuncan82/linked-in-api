import dotenv
import os
import string
import random
import requests

dotenv.load_dotenv()

REDIRECT_URI = "http://localhost:8000"
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

letters = string.ascii_lowercase
CSRF_TOKEN = "".join(random.choice(letters) for i in range(24))

auth_params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "state": CSRF_TOKEN,
    "scope": "r_liteprofile,r_emailaddress",
}

html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
                    params = auth_params)

# Print the link to the approval page
print(html.url)



# Click the link below to be taken to your redirect page.
