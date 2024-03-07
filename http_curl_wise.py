import requests
import os, dotenv

# # Replace these with the actual values
# endpoint = "YOUR_ENDPOINT_HERE"
# indexName = "YOUR_INDEX_NAME_HERE"
# api_version = "2023-11-01"
# api_key = "YOUR_API_KEY_HERE"  # Assuming API key is required for authorization

api_version = "2023-11-01"
search_service_name = os.getenv("SEARCH_SERVICE_NAME")
indexName = os.getenv("INDEX_NAME")
api_key = os.getenv("API_KEY")
endpoint = f"https://{search_service_name}.search.windows.net/"

# Construct the URL
url = f"{endpoint}/indexes('{indexName}')/docs/search.post.search?api-version={api_version}"

# Headers - Add or modify them according to your API's requirements
headers = {
    "Content-Type": "application/json",
    "Api-Key": api_key  # Assuming the API uses an API key for authentication
}

# Request body - Modify it according to your API's requirements
data = {
  "search": "gagal login brimo",
  "top": 3
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
    # Process the response as needed
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
