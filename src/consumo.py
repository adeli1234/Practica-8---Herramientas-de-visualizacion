import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
    "latitude": 19.70, 
    "longitude": -101.19,     
    "start_date": "2024-01-01", "end_date": "2024-01-05",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Mexico_City",
}

respuesta = requests.get(url, params=parametros, timeout=30)
print(respuesta.status_code)          # 200 = salió bien
datos = respuesta.json()              # de texto JSON a diccionario
df = pd.DataFrame(datos["daily"])     # de diccionario a tabla

print(df.shape)
print(df.head())
print(df.dtypes)