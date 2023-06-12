import requests
import mysql.connector
from geopy.geocoders import Nominatim

url = 'https://countriesnow.space/api/v0.1/countries'

# Set up MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin@00',
    database='travel_itinerary'
)
cursor = conn.cursor()

geolocator = Nominatim(user_agent='my_geocoder')

def create_table():
    # Creates the 'coordinates' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coordinates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(255),
            country VARCHAR(255),
            latitude FLOAT,
            longitude FLOAT
        )
    """)

def save_coordinates(city, country, latitude, longitude):
    # Saves coordinates to the MySQL database
    sql = "INSERT INTO coordinates (city, country, latitude, longitude) VALUES (%s, %s, %s, %s)"
    values = (city, country, latitude, longitude)
    cursor.execute(sql, values)
    conn.commit()

try:
    response = requests.get(url)
    data = response.json()
    citiesAndCountriesData = []

    create_table()

    for country in data['data']:
        if isinstance(country['cities'], list):
            for city in country['cities']:
                try:
                    geo_data = geolocator.geocode(city)
                    if geo_data is not None:
                        latitude = geo_data.latitude
                        longitude = geo_data.longitude
                        save_coordinates(city, country['country'], latitude, longitude)
                        citiesAndCountriesData.append({
                            'label': f"{city}, {country['country']}",
                            'value': city,
                            'country': country['country'],
                            'latitude': latitude,
                            'longitude': longitude
                        })
                except Exception as e:
                    print(f"Error geocoding '{city}': {str(e)}")
                    
    # Now you have the cities, countries, and coordinates data in the 'citiesAndCountriesData' list

except requests.exceptions.RequestException as e:
    print('Error fetching cities:', str(e))

# Close the MySQL connection
cursor.close()
conn.close()
