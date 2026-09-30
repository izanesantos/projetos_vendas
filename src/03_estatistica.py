

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

# Estatística descritiva das vendas
print("\nEstatística descritiva:")

print("Média:", df["valor_total"].mean())
print("Mediana:", df["valor_total"].median())
print("Mínimo:", df["valor_total"].min())
print("Máximo:", df["valor_total"].max())
print("Desvio padrão:", df["valor_total"].std())

import matplotlib.pyplot as plt

# Gráfico de faturamento por filial
faturamento_filial = df.groupby("Filial")["valor_total"].sum()

faturamento_filial.plot(kind="bar")

plt.title("Faturamento por filial")
plt.xlabel("Filial")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\faturamento_por_filial.png"
)

plt.show()

# Gráfico de quantidade de vendas por filial
quantidade_filial = df["Filial"].value_counts()

quantidade_filial.plot(kind="bar")

plt.title("Quantidade de vendas por filial")
plt.xlabel("Filial")
plt.ylabel("Quantidade de vendas")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\quantidade_vendas_por_filial.png"
)

plt.show()


# Gráfico de faturamento por linha de produto
faturamento_produto = (
    df.groupby("linha_produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

faturamento_produto.plot(kind="bar")

plt.title("Faturamento por linha de produto")
plt.xlabel("Linha de produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\faturamento_por_produto.png"
)

plt.show()

# Gráfico de avaliação média por produto
avaliacao_produto = (
    df.groupby("linha_produto")["Avaliação"]
    .mean()
    .sort_values(ascending=False)
)

avaliacao_produto.plot(kind="bar")

plt.title("Avaliação média por linha de produto")
plt.xlabel("Linha de produto")
plt.ylabel("Avaliação média")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\avaliacao_media_produto.png"
)

plt.show()

# Gráfico de formas de pagamento
forma_pagamento = df["forma_pagamento"].value_counts()

forma_pagamento.plot(kind="bar")

plt.title("Formas de pagamento utilizadas")
plt.xlabel("Forma de pagamento")
plt.ylabel("Quantidade de vendas")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\formas_pagamento.png"
)

plt.show()

# Gráfico de vendas por dia da semana
vendas_dia_semana = (
    df["data_venda"]
    .dt.day_name()
    .value_counts()
)

vendas_dia_semana.plot(kind="bar")

plt.title("Quantidade de vendas por dia da semana")
plt.xlabel("Dia da semana")
plt.ylabel("Quantidade de vendas")
plt.tight_layout()

plt.savefig(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\resultados\vendas_por_dia_semana.png"
)

plt.show()

