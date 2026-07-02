from weather import welcome, get_city, get_weather

welcome()

city = get_city()

weather = get_weather(city)

print(f"\nCity        : {weather['name']}")
print(f"Temperature : {weather['main']['temp']} °C")
print(f"Humidity    : {weather['main']['humidity']} %")
print(f"Weather     : {weather['weather'][0]['description'].title()}")
print(f"Wind Speed  : {weather['wind']['speed']} m/s")