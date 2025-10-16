import requests

url = 'https://yulin-serverless-hqehfjhdbdevghf9.eastus-01.azurewebsites.net/api/http_trigger1?code=HX9t08TylJXkwNVO4-fSLPlGIax01RS0mz7blEbCqVPwAzFu7Moddw=='

body = {
    "cholesterol": 270
}

response = requests.post(url, json=body)

print(response.text)
