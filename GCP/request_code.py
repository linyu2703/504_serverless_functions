import requests

url = ''

body = {
    "cholesterol": 180
}

response = requests.post(url, json=body)

print(response.text)
