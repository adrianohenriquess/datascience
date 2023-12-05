import pandas as pd

#url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

#dados_co2 = pd.read_excel(url)
#print(dados_co2.head())

#print(pd.ExcelFile(url).sheet_names)
#percapita = pd.read_excel(url, sheet_name='emissoes_percapita')
#fontes = pd.read_excel(url, sheet_name='fontes')
#print(fontes.head())

#intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D')
#print(intervalo)

#intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D', nrows=10)
#print(intervalo_2)

#percapita.to_excel('co2_percapita.xlsx', index=False)

#pd.read_excel('co2_percapita.xlsx')

#'https://docs.google.com/spreadsheets/d/1PSa3CajR7jy-TeEbcU4yrFiflOC30g8CeXITCpNlUUw/edit?usp=sharing'
sheet_id = '1PSa3CajR7jy-TeEbcU4yrFiflOC30g8CeXITCpNlUUw'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
dados_co2_sheets = pd.read_csv(url)
print(dados_co2_sheets.head())
sheet_name = 'emissoes_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

percapita_sheets = pd.read_csv(url_percapita)
print(percapita_sheets.head())