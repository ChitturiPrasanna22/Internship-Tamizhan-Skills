import tkinter as tk
import requests

# Replace with your OpenWeatherMap API key
API_KEY = "2a9fdaf1d7510aada72339e98d6c5301"

def get_weather():
    city = city_entry.get().strip()
    if city == "":
        result_label.config(text="Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            # Show real error message from API
            message = data.get("message", "City not found")
            result_label.config(text=f"Error: {message.title()}")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()

        result_label.config(
            text=f"City: {city}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description}"
        )

    except requests.exceptions.RequestException:
        result_label.config(text="Error fetching data. Check your internet connection.")

# ---------------- GUI Window ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

# Title
tk.Label(root, text="Weather App", font=("Arial", 16)).pack(pady=10)

# City entry
city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

# Get Weather button
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
