import requests

def weather(city,country):
	base_url = "http://api.openweathermap.org/data/2.5/weather"
	api_key = '41261d6f6cbd2eb9e9aa96c6c1dd7e98'
	
	params = {"q": f"{city},{country}", "appid": api_key}
	response = requests.get(base_url,params = params)
	data = response.json()
	
	if response.status_code == 200 :
		lat = data['coord']['lat']
		lon = data['coord']['lon']
		temperature = data['main']['temp'] - 273.15
		feels_like = data['main']['feels_like'] - 273.15
		max_temp = data['main']['temp_max'] - 273.15
		min_temp = data['main']['temp_min']- 273.15
		pressure = data['main']['pressure']
		description = data['weather'][0]['description']
		
		print("\nCity :"+city)
		print("\nLatitude :"+str(lat))
		print("\nLongitude :"+str(lon))
		print("\nTemperature :"+str(temperature)+"°C")
		print("\nFeels Like :"+str(feels_like)+"°C")
		print("\nMax temp :"+str(max_temp)+"°C")
		print("\nMin temp :"+str(min_temp)+"°C")
		print("\nPressure :"+str(pressure))
		print("\nDescription :"+description)
	
	


city = input("\nEnter the name of the city :")
country = input("\nEnter the country code :")
weather(city,country)
