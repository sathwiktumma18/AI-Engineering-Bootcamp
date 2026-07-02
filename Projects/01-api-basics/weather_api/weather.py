import requests
from config import API_KEY, BASE_URL


def welcome():
    print("=" * 40)
    print("      Weather API Explorer")
    print("=" * 40)


def get_city():
    while True:
        city = input("Enter city name: ").strip()

        if city == "":
            print("❌ City name cannot be empty.\n")
        elif not city.replace(" ", "").isalpha():
            print("❌ Invalid city name.\n")
        else:
            return city


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print(f"❌ Error: {data['message']}")
        return None

    return data    