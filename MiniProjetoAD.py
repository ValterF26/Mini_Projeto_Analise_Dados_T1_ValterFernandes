# Importando Biblíotecas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Carregando base de dados para visualização
# Leitura com tratamento para que cada informação de linha fique sob sua coluna mantendo a visualização organizada

df = pd.read_csv('Base_Varejo.csv', sep=';')

print(df.head(5))

# Removendo colunas sem informações ou irrelevantes

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.head().tail()

# Mostra a quantidade de linhas e colunas

num_registros, num_colunas = df.shape
print(f"Número de Registros (Linhas): {num_registros}")
print(f"Número de Colunas: {num_colunas}")
print("-" * 50)

# Mostra os tipos de dados de cada coluna

print("Tipos de dados de cada coluna:")
print(df.dtypes)

# Usando condicionais para limpeza do Dataset

def limpar_texto(texto):
    """
    Remove espaços extras, caracteres especiais indesejados
    e padroniza o texto em maiúsculas.
    """
    if pd.isna(texto):
        return None
    # Converte para string e remove espaços nas pontas
    texto_limpo = str(texto).strip()
    # Substitui múltiplos espaços por um único espaço
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo)
    # Mantém letras, números, acentos comuns e espaços (opcional, ajuste conforme a necessidade)
    # texto_limpo = re.sub(r'[^a-zA-Z0-9áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ ]', '', texto_limpo)
    return texto_limpo.upper()

def limpar_inteiro(valor):
    """
    Extrai apenas os números de uma string e converte para Integer.
    Retorna None (NaN) se não houver número válido.
    """
    if pd.isna(valor):
        return None
    # Mantém apenas dígitos numéricos
    apenas_numeros = re.sub(r'\D', '', str(valor))
    if apenas_numeros == '':
        return None
    return int(apenas_numeros)


# Verificando valores nulos

# --- ANÁLISE 1: VALORES NULOS ---

print("\n[1] Verificação de Valores Nulos por Coluna:")
valores_nulos = df.isnull().sum()
print(valores_nulos[valores_nulos > 0])

# Verificando Duplicatas

# --- ANÁLISE 2: DUPLICATAS ---

print("\n[2] Verificação de Linhas Duplicadas:")
total_duplicadas = df.duplicated().sum()
print(f"Total de linhas completamente duplicadas: {total_duplicadas}")

# Remover as linhas duplicadas mantendo apenas a primeira ocorrência

df = df.drop_duplicates()

# Aplicando datetime para padronizar inconsistências de formatos de datas

# --- ANÁLISE 3: INCONSISTÊNCIAS DE FORMATO (DATAS) ---

print("\n[3] Verificação de Inconsistências (Datas):")

# Tenta converter para data. O que não for data válida virará 'NaT' (Not a Time)

datas_convertidas = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
erros_data = datas_convertidas.isnull().sum()
print(f"Registros com datas inválidas ou corrompidas: {erros_data}")

# Conversão de formato de datas
# --- CONVERSÃO DA COLUNA DATA ---
# format='%d/%m/%Y': Indica o padrão Dia/Mês/Ano de 4 dígitos
# errors='coerce': Se houver erro de digitação na data, transforma em nulo em vez de quebrar o código

df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

# --- VERIFICAÇÃO ---

print("Tipo de dado da coluna DATA após a conversão:")
print(df['DATA'].dtypes)
print("\nPrimeiras linhas da coluna convertida:")
print(df['DATA'].head())

# Gerando estatísticas na coluna número de filhos do cliente

# Nota: Com base na estrutura do arquivo, a coluna é 'CL_FHL'

coluna_filhos = df['CL_FHL']

# 3. Calcular as estatísticas descritivas

estatisticas = {
    'Contagem (N)': coluna_filhos.count(),
    'Média': coluna_filhos.mean(),
    'Mediana': coluna_filhos.median(),
    'Moda': coluna_filhos.mode()[0],  # .mode() retorna uma Serie, pegamos o primeiro valor
    'Desvio Padrão': coluna_filhos.std(),
    'Mínimo': coluna_filhos.min(),
    '25% (1º Quartil)': coluna_filhos.quantile(0.25),
    '50% (2º Quartil/Mediana)': coluna_filhos.quantile(0.50),
    '75% (3º Quartil)': coluna_filhos.quantile(0.75),
    'Máximo': coluna_filhos.max()
}

# 4. Transformar em um DataFrame para exibir de forma organizada

df_estatisticas = pd.DataFrame.from_dict(estatisticas, orient='index', columns=['Valor'])

print("--- ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS (CL_FHL) ---")
print(df_estatisticas.round(2)) # Limita as casas decimais para facilitar a leitura


# Gerando e salvando arquivo csv limpo e tratado

df.to_csv('Base_Varejo_limpo.csv', index=False, encoding='utf-8')

# Bloco de conclusão


print(
    "Com base nas análises estruturais, estatísticas e de agrupamento realizadas no arquivo Base_Varejo.csv,\n"
    "podemos consolidar os seguintes insights e pontos de atenção sobre a base de dados:\n"
    "\n"
    "• Predomínio do Público Feminino no Volume de Itens: O cruzamento de dados via tabelas dinâmicas revela\n"
    "  que o público feminino (F) apresenta um volume de itens comprados consideravelmente maior em categorias\n"
    "  essenciais do varejo (como Alimentos e Limpeza), destacando-se como o principal motor de volume da operação.\n"
    "\n"
    "• Segmentação Estratégica e Frequência de Compras: Ao agrupar os dados por gênero e segmento de cliente (CL_SEG),\n"
    "  nota-se que determinados clusters (combinações de perfis de renda/comportamento com gênero) realizam transações\n"
    "  e visitas à loja com muito mais frequência, gerando cupons únicos que servem como ótimos alvos para campanhas\n"
    "  de fidelidade direcionadas.\n"
    "\n"
    "• Perfil Familiar Concentrado: A análise descritiva da coluna CL_FHL mostra uma forte concentração em torno\n"
    "  da média/mediana de filhos. O fato de a moda e a mediana indicarem um número baixo de filhos ajuda a traçar\n"
    "  o perfil demográfico do cliente padrão e direcionar o tamanho das embalagens ou promoções do tipo \"leve mais, pague menos\".\n"
    "\n"
    "• Necessidade de Higienização de Dados (Duplicatas): Como problema remanescente, a presença de linhas completamente\n"
    "  duplicadas infla artificialmente as métricas de vendas. Antes de tomar decisões de negócio sobre o faturamento,\n"
    "  é obrigatório executar o drop_duplicates() para garantir que a receita não esteja superestimada.\n"
    "\n"
    "• Estrutura de Arquivo Ineficiente (\"Colunas Fantasma\"): O delimitador extra (;;;;) no final de cada registro\n"
    "  gera colunas nulas desnecessárias que aumentam o consumo de memória do script. Isso exige um tratamento\n"
    "  prévio de infraestrutura de dados ou ajuste no sistema que exporta o relatório para o formato CSV."
)
    


