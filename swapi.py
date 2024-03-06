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

def get_planets(n):
    planets_data = get_swapi_data("planets")
    if planets_data:
        planets_list = planets_data.get("results", [])
        return planets_list[:n]  # Renvoie les n premières planètes de la liste
    else:
        return []

def create_dataframe_from_swapi_planets(n):
    data = get_planets(n)
    if data:
        return pd.DataFrame(data)  # Passer directement la liste de dictionnaires
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    planets_df = create_dataframe_from_swapi_planets(10)
    print(planets_df)
