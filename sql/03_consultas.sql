#Visualizar todos os dados da tabela Raw
SELECT *
FROM raw_vendas;


#Contar a quantidade total de vendas
SELECT COUNT(*) AS quantidade_vendas
FROM raw_vendas;


#Faturamento por filial
SELECT
    "Branch" AS filial,
    SUM(CAST("Sales" AS NUMERIC)) AS faturamento
FROM raw_vendas
GROUP BY "Branch"
ORDER BY faturamento DESC;


#Quantidade de vendas por filial
SELECT
    "Branch" AS filial,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;


#Faturamento por linha de produto
SELECT
    "Product line" AS linha_produto,
    SUM(CAST("Sales" AS NUMERIC)) AS faturamento
FROM raw_vendas
GROUP BY "Product line"
ORDER BY faturamento DESC;


#Avaliação média por linha de produto
SELECT
    "Product line" AS linha_produto,
    AVG(CAST("Rating" AS NUMERIC)) AS avaliacao_media
FROM raw_vendas
GROUP BY "Product line"
ORDER BY avaliacao_media DESC;


#Forma de pagamento mais utilizada
SELECT
    "Payment" AS forma_pagamento,
    COUNT(*) AS quantidade
FROM raw_vendas
GROUP BY "Payment"
ORDER BY quantidade DESC;


#Valor médio das vendas
SELECT
    AVG(CAST("Sales" AS NUMERIC)) AS valor_medio_venda
FROM raw_vendas;


#Maior venda registrada
SELECT
    MAX(CAST("Sales" AS NUMERIC)) AS maior_venda
FROM raw_vendas;


 #Quantidade de vendas por dia da semana
SELECT
    TO_CHAR(TO_DATE("Date", 'MM/DD/YYYY'), 'Day') AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY TO_CHAR(TO_DATE("Date", 'MM/DD/YYYY'), 'Day')
ORDER BY quantidade_vendas DESC;