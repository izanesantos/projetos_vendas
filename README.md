**Projeto de Análise de Vendas**

Projeto desenvolvido para analisar dados de vendas de um supermercado usando Python, Pandas, SQL e PostgreSQL.

**Objetivo**

Tratar os dados e responder algumas perguntas sobre as vendas, como faturamento por filial, produtos mais vendidos, formas de pagamento e valores das vendas.

**Tecnologias**

* Python

* Pandas

* Matplotlib

* PostgreSQL

* SQL

* Git e GitHub

**Estrutura**

projetos_vendas/

├── data/

│   ├── raw/

│   └── processed/

├── sql/

├── src/

├── Resultados/

├── README.md

├── requirements.txt

└── .gitignore

**Tratamento dos dados**

A base possui 1.000 registros e 17 colunas.

Foram verificadas informações como valores nulos, duplicados, valores negativos, quantidade e avaliação. Também foram ajustados os tipos de data e hora e os nomes das colunas.

**Principais resultados**

* Filial com maior faturamento: **Giza**

* Filial com mais vendas: **Alex**, com 340 vendas

* Produto com maior faturamento: **Food and beverages**

* Melhor avaliação média: **Food and beverages**

* Forma de pagamento mais utilizada: **Ewallet**, com 345 vendas

* Valor médio das vendas: **R$ 322,97**

* Maior venda: **R$ 1.042,65**

* Dia com mais vendas: **sábado**, com 164 vendas

Os gráficos gerados estão na pasta `Resultados`.

**Execução**

Para instalar as bibliotecas:

```bash

pip install -r requirements.txt

```

Depois, os arquivos Python da pasta `src` podem ser executados para realizar a leitura, tratamento e análise dos dados.

**Projeto**

Atividade avaliativa de Análise de Dados com Python — SCT/SESI.