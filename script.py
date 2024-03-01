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

def get_starships():
    starships_data = get_swapi_data("starships")
    if starships_data:
        return starships_data.get("results", [])
    else:
        return []

def create_dataframe_from_swapi(resource):
    data = get_swapi_data(resource)
    if data:
        return pd.DataFrame(data.get("results", []))
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    starships_df = create_dataframe_from_swapi("starships")
    print(starships_df.head())

