import requests


class Weather:
    """
    Contains functions to obtain weather data via OpenWeather API.
    """

    @staticmethod
    def get_current_weather(city: str, api_key: str) -> dict:
        """
        Gets weather for a given city name.
        :param city: str, city name.
        :param api_key: the API key from OpenWeather. See https://openweathermap.org/appid.
        :return: JSON dict with weather data.
        """
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api_key
        return requests.get(url).json()

    @staticmethod
    def get_weather_main(weather_data: dict) -> str:
        """
        Accepts weather data in JSON dict format received by get_current_weather call and returns general weather description.
        :param weather_data: JSON dict with weather data.
        :return: str, weather description.
        """
        return weather_data['weather'][0]['description'].capitalize()

    @staticmethod
    def get_temperature(weather_data: dict) -> str:
        """
        Accepts weather data in JSON dict format received by get_current_weather call and returns temperature.
        :param weather_data:
        :return: str, temperature data.
        """
        tm = str(weather_data['main']['temp'])
        fl = str(weather_data['main']['feels_like'])
        return f"Temperature: {tm} °C, feels_like: {fl} °C"
