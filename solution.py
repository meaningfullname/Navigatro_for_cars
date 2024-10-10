
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="something")

t = input("Enter your address: ")

locat1 = geolocator.geocode(t)

if locat1:

    location_data = locat1.raw





    display_name = location_data.get('display_name', '')
    country = display_name.split(",")[-1].strip()

    print(f"Country: {country}")
else:
    print("Location not found. Please check your input.")
