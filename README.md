# Mini_Projeto_Analise_Dados_T1_ValterFernandes

# 🛒 Pipeline de Limpeza, Tratamento e Análise de Dados - Varejo

Este repositório contém um script em Python focado na ingestão, higienização, tratamento de inconsistências e análise descritiva de uma base de dados do setor varejista (`Base_Varejo.csv`). Ao final do processo, o script exporta uma base limpa e pronta para modelagem ou ferramentas de BI, além de consolidar insights sobre o perfil dos clientes.

## 📌 Índice
- [Visão Geral](#-visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Funcionalidades do Script](#-funcionalidades-do-script)
- [Estrutura do Tratamento de Dados](#-estrutura-do-tratamento-de-dados)
- [Insights de Negócio Obtidos](#-insights-de-negócio-obtidos)
- [Como Executar o Projeto](#-como-executar-o-projeto)

---

## 🔍 Visão Geral

No cenário do varejo, bases de dados brutas frequentemente apresentam problemas estruturais como colunas fantasmas, registros duplicados, formatos de data inconsistentes e valores nulos. Este projeto resolve essas dores aplicando técnicas de engenharia e análise de dados com `pandas` e `re` (Expressões Regulares), garantindo a confiabilidade das métricas de vendas e do perfil demográfico dos clientes.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Manipulação, limpeza e análise estatística dos dados.
* **NumPy**: Suporte a operações matemáticas e valores nulos.
* **Matplotlib**: Preparação para visualizações gráficas.
* **Re (Regular Expressions)**: Padronização textual e extração de caracteres específicos.

---

## 🚀 Funcionalidades do Script

1.  **Leitura Organizada:** Importação do arquivo utilizando o separador correto (`sep=';'`).
2.  **Eliminação de "Colunas Fantasmas":** Remoção automática de colunas nulas criadas por delimitadores extras no final do arquivo (colunas do tipo `Unnamed`).
3.  **Higienização Textual e Numérica:** Funções preparadas com Regex para remover espaços extras, converter textos para caixa alta e extrair apenas números de strings.
4.  **Deduplicação:** Identificação e remoção de linhas 100% duplicadas para evitar a inflação artificial de métricas financeiras.
5.  **Padronização de Datas:** Conversão de strings de datas para o formato nativo `datetime64`, tratando erros de digitação de forma segura (`errors='coerce'`).
6.  **Análise Estatística Descritiva:** Cálculo detalhado de métricas (Média, Mediana, Moda, Quartis, Desvio Padrão) da coluna de número de filhos (`CL_FHL`).
7.  **Exportação:** Salvamento dos dados higienizados em um novo arquivo comprimido/formatado em `utf-8`.

---

## 📐 Estrutura do Tratamento de Dados

O script executa o fluxo de processamento dividido em etapas claras exibidas no console:

* **Análise 1 (Valores Nulos):** Mapeia a quantidade de campos vazios por coluna.
* **Análise 2 (Duplicatas):** Exibe o total de linhas repetidas e limpa o DataFrame mantendo apenas a primeira ocorrência.
* **Análise 3 (Inconsistência de Datas):** Identifica registros corrompidos e transforma a coluna `DATA` em um tipo temporal padrão.
* **Estatística Descritiva:** Gera uma tabela organizada com o perfil de filhos da base de clientes.

---

## 💡 Insights de Negócio Obtidos

Após a execução das análises de agrupamento e estatísticas, os seguintes pontos foram consolidados:

* **Predomínio do Público Feminino no Volume de Itens:** O cruzamento de dados revela que o público feminino (`F`) possui um volume de compras significativamente maior em categorias essenciais (Alimentos e Limpeza), sendo o principal motor de volume da operação.
* **Segmentação Estratégica e Frequência:** Clusters que combinam gênero e segmento de cliente (`CL_SEG`) mostram picos de visitas e geração de cupons únicos, ideais para campanhas de fidelidade direcionadas.
* **Perfil Familiar Concentrado:** A análise da coluna `CL_FHL` (número de filhos) aponta baixa variabilidade (moda e mediana baixas). Isso direciona estratégias de sortimento, como o tamanho ideal de embalagens e promoções do tipo *"Leve mais, Pague menos"*.
* **Aviso de Infraestrutura de Dados:** A presença de linhas duplicadas e colunas vazias (`Unnamed`) alerta para a necessidade de ajuste no sistema que exporta o relatório original, evitando processamento desnecessário e relatórios de faturamento superestimados.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado e as bibliotecas necessárias. Você pode instalá-las rodando:
```bash
pip install pandas numpy matplotlib
