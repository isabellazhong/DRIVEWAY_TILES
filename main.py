import requests
import base64

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
api_key = "AIzaSyAhRRw8UdvOxp4p_o2Pwf-xXRiV1pvh5Q8"

# Read the image file and encode it as Base64
with open("image.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Prepare the JSON payload
data = {
    "contents": [
        {
            "parts": [
                {"text": "would you say that the car is in dangerous conditions to drive in? give yes or no answer"},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": encoded_image
                    }
                }
            ]
        }
    ]
}

# Send the POST request
response = requests.post(url, json=data, params={"key": api_key})

if response.status_code == 200:
    # Extract the useful part of the response
    response_data = response.json()
    try:
        # Access the generated text
        generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
        print(generated_text)
    except KeyError:
        print("Error: Unable to parse the response.")
else:
    print(f"Error: {response.status_code} - {response.text}")