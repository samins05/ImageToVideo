import urllib.parse
import requests

# List of image URLs
image_urls = [
    "https://placehold.co/600x400/png",
    "https://placehold.co/600x400/png",
    "https://placehold.co/600x400/png"
]

# Encode the URLs
encoded_urls = [urllib.parse.quote(url, safe='') for url in image_urls]
encoded_url_string = ",".join(encoded_urls)

# Construct the API endpoint
api_endpoint = f"http://127.0.0.1:5000/ImageToVideo/{encoded_url_string}"

# Make the API request
response = requests.get(api_endpoint)

# Check the response
print(response.status_code)
print(response.text)