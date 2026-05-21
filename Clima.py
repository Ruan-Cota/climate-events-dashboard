import pandas as pd
import requests

estados = {
    "RS": {
        "nome": "Rio Grande do Sul",
        "lat": -30.03,
        "lon": -51.23
    },

    "SC": {
        "nome": "Santa Catarina",
        "lat": -27.59,
        "lon": -48.55
    },

    "PR": {
        "nome": "Paraná",
        "lat": -25.42,
        "lon": -49.27
    }
}

lista_dfs = []

for estado, coords in estados.items():

    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={coords['lat']}&longitude={coords['lon']}&start_date=2023-01-01&end_date=2025-12-31&daily=precipitation_sum&timezone=America%2FSao_Paulo"

    resposta = requests.get(url)

    dados = resposta.json()

    df = pd.DataFrame(dados["daily"])

    df["Estado"] = coords["nome"]
    df["Sigla"] = estado
    df["Latitude"] = coords["lat"]
    df["Longitude"] = coords["lon"]


   

    lista_dfs.append(df)

df_final = pd.concat(lista_dfs)

print(df_final)
df_final.to_csv(r"C:\Users\Ruan\Downloads\eventos_climaticos_sul.csv", index=False, sep=";", decimal=",")