# Weather App

This is a simple Python weather application that fetches weather data for a given city using the OpenWeatherMap API.

## Features

- Fetches current temperature, humidity, and weather description for a specified city.
- Uses the OpenWeatherMap API to retrieve weather data.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-app
    ```

3. Install the required library:

    ```bash
    pip install requests
    ```

## Usage

1. Replace `"your_api_key_here"` with your OpenWeatherMap API key in the `weather_app.py` file.

    ```python
    api_key = "your_api_key_here"
    ```

2. Run the script:

    ```bash
    python weather_app.py
    ```

3. Enter the city name when prompted:

    ```bash
    Enter city name: London
    ```

4. The script will display the weather details for the specified city.

## Example

```bash
Enter city name: London
City: London
Temperature: 15°C
Humidity: 82%
Description: broken clouds
