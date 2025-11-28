import requests
import pandas as pd
from sqlalchemy import create_engine

def extract ()-> list[dict]:
# API extracts data(data1) from https://open-meteo.com/
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.9612&longitude=-82.9988&current_weather=true"
    resp = requests.get(url)
    resp.raise_for_status()   # Ensures API returned 200 OK
    return resp.json()

data1 = extract()
print(data1)
# Print the result











