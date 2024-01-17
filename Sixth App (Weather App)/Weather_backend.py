import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5" #Go to My API keys and copi the one shown


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}" # These are json data
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days # The data are collected in intervals of 3h, so we have 8 observations per day
    filtered_data = filtered_data[:nr_values]
    return filtered_data



if __name__ == "__main__":
    print(get_data("Tokyo", 3))