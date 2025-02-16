import requests
from datetime import datetime
import base64
import pyfirmata
import time

weather_url = "http://api.weatherstack.com/current"
weather_api_key = "722f61064d45c659430c0b9d043cbbfa"
temperature = 10
ai_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
ai_api_key = "AIzaSyAhRRw8UdvOxp4p_o2Pwf-xXRiV1pvh5Q8"
# board = pyfirmata.Arduino("")

def find_weather(city: str):
    params = {
        'access_key': weather_api_key,
        'query': city, 
        'hourly': 1
    }

    response = requests.get(weather_url, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'current' in data:
                current_weather = data['current']
                sliced_data = {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'temperature': current_weather['temperature'],
                    'description': current_weather['weather_descriptions'][0]
                }
                return sliced_data
            else:
                print("Failed to fetch current weather data")
                print(data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
    else:
        print(f"Failed to fetch weather data: {response.status_code}")
        print(response.text)


#print(find_weather('Toronto'))


def watts_to_heat(dh: int, dl: int, dw:int):
        # Calculate volume of snow
        volume = dh * dl * dw

        # Prepare the JSON payload
        data = {
            "contents": [
                        { "parts": [ {"text": f"How many estimated watts does it take to melt {volume} cubic meters of snow at {temperature} degree celcius? Only provide the number"}]}
                        ]
        }
        # Send the POST request
        response = requests.post(ai_url, json=data, params={"key": ai_api_key})

        if response.status_code == 200:
            try:
                # View the entire response to debug the structure
                response_data = response.json()
                
                # Adjust based on actual API structure
                generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
                return generated_text
            except Exception as e:
                return f"Error parsing response: {e}"
        else:
            return f"Error: {response.status_code} - {response.text}"


print(watts_to_heat(0.3,0.2,1))






            



    
    








