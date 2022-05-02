# Data Challenge Stone 2022

Para mais informações sobre o desafio acesse: LINK

## Framework de Avaliação

### Validações iniciais

Inicialmente eu gosto de realizar uma análise descritiva das bases que estão disponíveis para trabalhar. Nesse caso nós tempos:

- portfolio_clientes
- portfolio_comunicados
- portfolio_geral
- portfolio_tpv

#### portfolio_clientes

A base deveria possuir apenas um registro por `nr_documento`, porém quando verificamos essa coluna, vemos que existem registros duplicados. Como no momento não sei como tratar esse caso, irei considerar apenas um cliente para cada um dos casos duplicados.

```python
# total de clientes
clients_wo_duplicate = clients.drop_duplicates(["nr_documento"])
clients_wo_duplicate.shape
```

```bash
(14265, 6)
```

Dessa forma, possuímos um total de **14.265 clientes** na base. E, como cada cliente pode possuir mais de um contrato, ao rapidamente analisarmos a tabela `portfolio_geral` vemos que existem um número levemente maior, **14.756 contratos**, registrados.

Essa base é composta de mais algumas variáveis categóricas, e saber como as mesmas estão distribuídas pode nos trazer bons insights para análises futuras.

##### Distribuição de Tipo da Empresa

- plot

##### Distribuição dos Estados

- plot

##### Distribuição dos Segmentos e Subsegmentos

- plot

Interessante a se notar aqui é que temos a presençã de um subsegmento chamado `None` como uma string válida, quando na verdade categoriza um missing value e não um subsegmento de fato.

#### portfolio_tpv

Essa tabela trás toda a informação de _Total Paid Value_ que representa o valor transacionado no dia por cada um dos nossos clientes. Importante salientar que essa tabela não possui todos os clientes presentes na tabela `portfolio_clientes`. Estranhamente, quando procuramos por esse `nr_documento` e relacionamos ao `contrato_id`, vemos que existe o mesmo teve pagamento.

Analisar o TPV como um todo não é muito conclusivo, temos valores muito dispersos de valor transacionado diariamente e de máximos e mínimos. Portanto, como temos maiores detalhes sobre cada um dos clientes, foi mais interessante levar isso em consideração na hora fazer a análise.

- join das bases
- qtd transacionado mensal por segmento
- valor transacionado mensal por segmento
- timeline para cada segmento

#### portfolio_comunicados

#### portfolio_geral

### Fluxo de etapas realizadas

Vamos focar inicialmente nas tabelas de `portfolio_geral` e `portfolio_comunicados` para separar a base entre contratos que receberam notificação, e contratos que não receberam nenhum comunicado durante o período de quitação da linha de crédito.

#### 1. Tratamento Qualquer

#### 2. Cruzamento nos dados

#### 3. Limpeza

#### 4. Criação de novas features

- prop_success_dsp: proporção de sucesso das comunicações que fora enviadas, dividida por cada tipo de acionamento dado.
- total_ideal_dsp: total de vezes que a msg deveria ser enviada ao cliente, por tipo de acionamento.
- mesma variável de cima, mas por dspp.
- valor total do crédito
- todos os dados sobre os clientes
- score_success_dsp
- score_success_dspp
- qtd de entregues, n-entregues e lidas por tipo de acionamento e por tipo de mensagem.

### Conclusões e Insights
