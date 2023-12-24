import pandas as pd
import numpy  as np

url_dados_imoveis_disponiveis = 'https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/moveis_disponiveis.json'

dt_data = pd.read_json(url_dados_imoveis_disponiveis)
print(dt_data.head())
print(dt_data.info())

dt_data['data'] = pd.to_datetime(dt_data['data'])
print(dt_data.info())
print(dt_data.head())

#Formatar as datas com apenas o mes e o ano e contar
#quais são os imoveis disponives em cada mes do ano
subset_agrupado_por_mes = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
print(subset_agrupado_por_mes)