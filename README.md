# Cloud Serverless Functions

## Zoom Recording
Recording: https://drive.google.com/file/d/1heHOG47wYt6OUWIXjxORj25nLsCtPu7A/view?usp=sharing

## Cloud environments
Cloud environment used and their regions: 
- Google Cloud Platform: US-central-1
- Azure: East US

## Steps to deployment
GCP: 
1. Search Cloud Run function 
2. Create new function
3. Name the function, select region and finish configuration
4. Edit main source code
5. Test and deploy.

Azure: 
1. Search Function 
2. Create new function app
3. Name the function app, select region and finish configuration
4. Create new function with HTTP trigger and set authorization level to "Function" or "Anonymous"
5. Edit main source code.
6. Test and deploy.

## Functionality showcase
GCP:
![GCP function](/GCP/gcp_request.png)
![GCP function](/GCP/gcp_test.png)

Azure:
![azure functionality](/AZURE/azure_request.png)
![azure functionality](/AZURE/azure_test.png)


## Public Endpoint URLs
GCP: https://blood-pressure-370972544757.us-central1.run.app

Azure: https://yulin-serverless-hqehfjhdbdevghf9.eastus-01.azurewebsites.net/api/http_trigger1?code=HX9t08TylJXkwNVO4-fSLPlGIax01RS0mz7blEbCqVPwAzFu7Moddw==

## Cholesterol Source Link:
https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean

## Example Requests
### Testing Optimal Total Cholesterol level (GCP) 
```python
import requests

url = 'https://blood-pressure-370972544757.us-central1.run.app'

body = {
    "cholesterol": 180
}

response = requests.post(url, json=body)

print(response.text)
```
Output:

```json
{"cholesterol": 180.0, "status": "optimal", "category": "Optimal (<200 mg/dL)"}
```

### Testing High Total Cholesterol level (Azure)
```python
import requests

url = 'https://yulin-serverless-hqehfjhdbdevghf9.eastus-01.azurewebsites.net/api/http_trigger1?code=HX9t08TylJXkwNVO4-fSLPlGIax01RS0mz7blEbCqVPwAzFu7Moddw=='

body = {
    "cholesterol": 270
}

response = requests.post(url, json=body)

print(response.text)
```
Output:
```json
{"cholesterol": 270.0, "status": "high", "category": "High (>=240 mg/dL)"}
```

### Testing Borderline High Total Cholesterol level (Azure)
```python
import requests

url = 'https://yulin-serverless-hqehfjhdbdevghf9.eastus-01.azurewebsites.net/api/http_trigger1?code=HX9t08TylJXkwNVO4-fSLPlGIax01RS0mz7blEbCqVPwAzFu7Moddw=='

body = {
    "cholesterol": 225
}

response = requests.post(url, json=body)

print(response.text)
```
Output:
```json
{"cholesterol": 225.0, "status": "borderline high", "category": "Borderline High (200-240 mg/dL)"}
```

## Comparison between GCP and Azure for serverless functions
Azure:
- Offers a wider variety of trigger types (HTTP, timer, blob, queue, etc.).
- Provides control over authentication with options like function keys, anonymous access, or Azure Active Directory integration.
- Has a more feature-rich local testing and debugging environment through VS Code and the Azure Functions Core Tools.

GCP:
- Features a simple, user-friendly interface for creating and configuring Cloud Functions.
- Allows for quick function editing and redeployment directly from the console with minimal setup.
- Provides detailed monitoring and logging through Cloud Logging and Cloud Trace, making it easier to track performance and errors.


### Overall assessment
Both Azure and GCP deliver strong performance for running lightweight serverless applications. Azure stands out for its flexibility, rich configuration options, and strong integration with enterprise tools. GCP, on the other hand, excels in simplicity, ease of use, and fast deployment, making it ideal for rapid development and testing. Overall, both platforms effectively handle cloud-based functions, but the choice often depends on whether a user prioritizes flexibility and integration (Azure) or usability and speed (GCP).
