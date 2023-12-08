import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

dados = pd.read_csv(url)

dados.to_sql('clientes', engine, index=False)

inspector = inspect(engine)
print(inspector.get_table_names())

query = ('SELECT * '
         '  FROM clientes '
         ' WHERE Categoria_de_renda = "Empregado"')

empregados = pd.read_sql(query, engine)
empregados.to_sql('empregados', con=engine, index=False)

empregados_colunas = pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])
#print(empregados_colunas.head())


#query2 = ('SELECT * '
 #        '  FROM clientes ')

#clientes = pd.read_sql(query2, engine)

query3 = 'DELETE FROM clientes WHERE ID_Cliente = 5008804'
with engine.connect() as conn:
    conn.execute(query3)


query = 'UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    conn.execute(query)

clientes_finais = pd.read_sql_table('clientes', engine)
print(clientes_finais['Grau_escolaridade'])