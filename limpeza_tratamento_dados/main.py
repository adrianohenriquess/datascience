import pandas as pd
import json


#dados_churn = pd.read_json(url)
#print(dados_churn.head())

#print(dados_churn['conta'][0])

#pd.json_normalize(dados_churn['conta']).head()
#pd.json_normalize(dados_churn['telefone']).head()

with open('dataset-telecon.json') as f:
    json_bruto = json.load(f)

print(json_bruto)
dados_normalizados = pd.json_normalize(json_bruto)
print(dados_normalizados.head())