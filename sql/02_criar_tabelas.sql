CREATE TABLE raw_vendas (
    "Invoice ID" VARCHAR(50),
    "Branch" VARCHAR(10),
    "City" VARCHAR(100),
    "Customer type" VARCHAR(50),
    "Gender" VARCHAR(20),
    "Product line" VARCHAR(150),
    "Unit price" VARCHAR(50),
    "Quantity" VARCHAR(50),
    "Tax 5%" VARCHAR(50),
    "Sales" VARCHAR(50),
    "Date" VARCHAR(50),
    "Time" VARCHAR(50),
    "Payment" VARCHAR(50),
    "cogs" VARCHAR(50),
    "gross margin percentage" VARCHAR(50),
    "gross income" VARCHAR(50),
    "Rating" VARCHAR(50)
);

CREATE TABLE tratada_vendas (
    id_venda VARCHAR(50) PRIMARY KEY,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50) NOT NULL,
    genero VARCHAR(20) NOT NULL,
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario > 0),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    imposto NUMERIC(10,2) NOT NULL CHECK (imposto >= 0),
    valor_total NUMERIC(10,2) NOT NULL CHECK (valor_total >= 0),
    data_venda DATE NOT NULL,
    hora_venda TIME NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(10,2) NOT NULL CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2) NOT NULL CHECK (margem_percentual >= 0),
    receita_bruta NUMERIC(10,2) NOT NULL CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(3,1) NOT NULL CHECK (avaliacao >= 0 AND avaliacao <= 10)
);