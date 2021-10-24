import pandas as pd

# Variables definition
ORIGINAL_DATA = "dados_13mai2021.csv"
STATES_DATA = "states.csv"
COUNTRY_DATA = "brasil.csv"


try:
  df = pd.read_csv(ORIGINAL_DATA, sep=";")
except FileNotFoundError:
  raise SystemExit(">>> Data file not found ==> " + ORIGINAL_DATA)

# States data only
df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
# Country data only
df_brasil = df[df["regiao"] == "Brasil"]

df_states.to_csv(STATES_DATA)
df_brasil.to_csv(COUNTRY_DATA)