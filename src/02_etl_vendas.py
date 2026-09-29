import pandas as pd

caminho = r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\data\raw\SuperMarket Analysis.csv"

df = pd.read_csv(caminho)

#Mostra linhas e colunas
print(df.shape)

print(df.dtypes)

print(df.isnull().sum())

print("Duplicados:", df.duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

print(df["Date"].dtype)

df["Time"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p").dt.time

print(df["Time"].dtype)

df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "Filial",
    "City": "Cidade",
    "Customer type": "tipo_cliente",
    "Gender": "Gênero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "Quantidade",
    "Tax 5%": "Imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "Avaliação"
})

print(df.columns)

print(df.dtypes)

print("Valores negativos:")
print((df[[
    "preco_unitario",
    "Quantidade",
    "Imposto",
    "valor_total",
    "custo_mercadoria",
    "receita_bruta"
]] < 0).sum())

print("Quantidade menor ou igual a zero:")
print((df["Quantidade"] <= 0).sum())

print("Avaliações fora do intervalo 0 a 10:")
print(((df["Avaliação"] < 0) | (df["Avaliação"] > 10)).sum())

valor_calculado = (
    df["preco_unitario"] * df["Quantidade"] + df["Imposto"]
)

print("Diferenças no valor total:")
print((df["valor_total"] - valor_calculado).abs().round(2).gt(0.01).sum())

df.to_csv(
    r"C:\Users\izane\OneDrive\Área de Trabalho\ESTUDO.SCTEC\projetos_vendas\data\processed\Dados_Tratados.csv",
    index=False
)