import requests

url = ''

body = {
    "cholesterol": 270
}

response = requests.post(url, json=body)

print(response.text)
