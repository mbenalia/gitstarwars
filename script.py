import requests

import pandas as pd

def get_swapi_data(resource):
    url = f"https://swapi.dev/api/{resource}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from {url}")
        return None

def get_vehicles():
    vehicles_data = get_swapi_data("vehicles")
    if vehicles_data:
        return vehicles_data.get("vehicles", [])
    else:
        return []

def create_dataframe_from_swapi(resource):
    data = get_swapi_data(resource)
    if data:
        return pd.DataFrame(data.get("results", []))
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    vehicles_df = create_dataframe_from_swapi("vehicles")
    print(vehicles_df.head())

