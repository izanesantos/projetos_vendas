

import pandas as pd

# Caminho dos dados tratados
caminho = r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\data\processed\Dados_Tratados.csv"

# Lê os dados
df = pd.read_csv(caminho)

# Converte a data
df["data_venda"] = pd.to_datetime(df["data_venda"])

# Mostra o tamanho da base
print("Tamanho da base:", df.shape)


#Qual filial apresentou o maior faturamento?
faturamento_filial = (
    df.groupby("Filial")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n1. Faturamento por filial:")
print(faturamento_filial)


#Qual filial realizou a maior quantidade de vendas?
quantidade_filial = (
    df.groupby("Filial")
    .size()
    .sort_values(ascending=False)
)

print("\n2. Quantidade de vendas por filial:")
print(quantidade_filial)


#Qual linha de produto apresentou o maior faturamento?
faturamento_produto = (
    df.groupby("linha_produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n3. Faturamento por linha de produto:")
print(faturamento_produto)


#Qual linha de produto recebeu a melhor avaliação média?
avaliacao_produto = (
    df.groupby("linha_produto")["Avaliação"]
    .mean()
    .sort_values(ascending=False)
)

print("\n4. Avaliação média por linha de produto:")
print(avaliacao_produto)


#Qual foi a forma de pagamento mais utilizada?
forma_pagamento = (
    df["forma_pagamento"]
    .value_counts()
)

print("\n5. Formas de pagamento:")
print(forma_pagamento)


#Qual foi o valor médio das vendas?
valor_medio = df["valor_total"].mean()

print("\n6. Valor médio das vendas:")
print(f"R$ {valor_medio:.2f}")


#Qual foi a maior venda registrada?
maior_venda = df["valor_total"].max()

print("\n7. Maior venda registrada:")
print(f"R$ {maior_venda:.2f}")


#Em qual dia da semana ocorreu a maior quantidade de vendas?
df["dia_semana"] = df["data_venda"].dt.day_name()

vendas_dia_semana = (
    df["dia_semana"]
    .value_counts()
)

print("\n8. Quantidade de vendas por dia da semana:")
print(vendas_dia_semana)
