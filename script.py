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

def get_people():
    people_data = get_swapi_data("people")
    if planets_data:
        return planets_data.get("results", [])
    else:
        return []

def create_dataframe_from_swapi(resource):
    data = get_swapi_data(resource)
    if data:
        return pd.DataFrame(data.get("results", []))
    else:
        return pd.DataFrame()
def get_people(n):
    people_data = get_swapi_data("people")
    if people_data:
        results = people_data.get("results", [])
        liste = []
        for i in range(min(n, len(results))):
            liste.append(results[i])
        return liste
    else:
        return []

def create_dataframe_from_swapi(n):
    data = get_people(n)
    if data:
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    people_df = create_dataframe_from_swapi("people")
    print(people_df.head())
