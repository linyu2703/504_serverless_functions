import requests

url = 'https://blood-pressure-370972544757.us-central1.run.app'

body = {
    "cholesterol": 180
}

response = requests.post(url, json=body)

print(response.text)
