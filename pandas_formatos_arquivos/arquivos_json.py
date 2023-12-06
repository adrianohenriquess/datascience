import pandas as pd

dados_pacientes = pd.read_json('pacientes.json')
print(dados_pacientes)

dados_pacientes_2 = pd.read_json('pacientes_2.json')
print(dados_pacientes_2)

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])
print(df_normalizado)

df_normalizado.to_json('historico_pacientes_normalizado.json')
print(pd.read_json('historico_pacientes_normalizado.json'))