
import pandas as pd

# Caminho do dataset original
caminho = "C:\\Users\\izane\\OneDrive\\Área de Trabalho\\ESTUDO.SCTEC\\projetos_vendas\\data\\raw\\SuperMarket Analysis.csv"

# Ler o arquivo CSV
df = pd.read_csv(caminho)

# Mostrar as primeiras linhas
print(df.head())

#Mostrar o número de linhas e colunas do DataFrame
print(df.shape)

#Mostrar os nomes das colunas.
print(df.columns)

#Mostrar os tipos de dados de cada coluna.
print(df.dtypes)

#Mostrar informacoes gerais.
print(df.info())

#Valores Nulos
print(df.isnull().sum())

#Mostra valores duplicados
print(df.duplicated().sum())

#Mostrar estatísticas descritivas 
print(df.describe().T.to_string())


