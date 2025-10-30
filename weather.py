import requests
import os
import sys

def weather(city,country):
	api_key = os.environ.get('OPENWEATHER_API_KEY')
	
	if not api_key :
		print("\n ERROR: OPENWEATHER_API_KEY environment variable not set.")
		print("Please set this variable and try again.")
		sys.exit(1)

	base_url = "http://api.openweathermap.org/data/2.5/weather"
	params = {"q": f"{city},{country}", "appid": api_key}
	

	try:
		response = requests.get(base_url,params = params)
		response.raise_for_status()
		data = response.json()

		lat = data['coord']['lat']
		lon = data['coord']['lon']
		temperature = data['main']['temp']
		feels_like = data['main']['feels_like']
		max_temp = data['main']['temp_max']
		min_temp = data['main']['temp_min']
		pressure = data['main']['pressure']
		humidity = data['main']['humidity']
		description = data['weather'][0]['description']

		print(f"\nCity: {city}")
		print(f"Latitude: {lat}")
		print(f"Longitude: {lon}")
		print(f"Temperature: {temperature}°C")
		print(f"Feels Like: {feels_like}°C")
		print(f"Max temp: {max_temp}°C")
		print(f"Min temp: {min_temp}°C")
		print(f"Pressure: {pressure} hPa")
		print(f"Humidity: {humidity}%")
		print(f"Description: {description.title()}")
	
	except requests.exceptions.HTTPError as http_err:
		if response.status_code == 404:
			print(f"\nError: City not found. Please check the city and country code.")
		elif response.status_code == 401:
			print(f"\nError: Invalid API key. Please check your OPENWEATHER_API_KEY.")
		else:
			print(f"\nHTTP error occurred: {http_err}")
	except request.exception.RequestException as req_err:
		print(f"\nError: A request error occurred: {req_err}")
	except KerError:
		print(f"\nError: Could not parse weather data. The response may be malformed.")
	except Exception as err:
		print(f"\nAn unexpected error occured: {err}")


def main():
	city = input("\nEnter the name of the city: ")
	country = input("Enter the country code: ")
	weather(city, country)


if __name__ == "__main__":
	main()