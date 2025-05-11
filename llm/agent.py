import os
import json
import time
import requests
import logging

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,  # or DEBUG, WARNING, ERROR
    format='%(asctime)s %(levelname)s: %(message)s',
)

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    if tool_call.function.name == "get_current_time":
        time = get_current_time()
        response = {
            "role": "tool",
            "content": json.dumps({"Time": time}),
            "tool_call_id": tool_call.id
        }
        return response
    elif tool_call.function.name == "get_weather":
        arguments = json.loads(tool_call.function.arguments)
        city = arguments.get('city')
        weather = get_weather(city)
        response = {
            "role": "tool",
            "content": json.dumps({"Weather": weather}),
            "tool_call_id": tool_call.id
        }
        return response


def getTools():
	time_function = {
	    "name": "get_current_time",
	    "description": "Get the current time. Call this whenever you need to know the current time or date, for example when a user asked 'What is time right now? or 'What is today's date?'.",
	    "parameters": {
	        "type": "object",
	        "properties": {},
	        "required": [],
	        "additionalProperties": False
	    }
	}

	weather_function = {
	    "name": "get_weather",
	    "description": "Get the weather details. Call this whenever you need to know the weather for a city, for example when a user asked 'How is weather now?'",
	    "parameters": {
	        "type": "object",
	        "properties": {
	            "city": {
	                "type": "string",
	                "description": "The name of the city (e.g., 'Paris', 'New York'). Do not repeat it."
	            }
	        },
	        "required": ["city"],
	        "additionalProperties": False
	    }
	}

	tools = [
		{"type": "function", "function": time_function},
		{"type": "function", "function": weather_function},
	]
	return tools

def get_current_time():
	logging.info("Tool get_current_time called.")
	os.environ['TZ'] = 'Asia/Dubai'
	time.tzset()
	return time.strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city):
    logging.info(f"Tool get_weather called for location {city}.")
    base_url = "https://wttr.in/"+city
    params = {
        'format': 'j1',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        return str(data)

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
