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

def limpar_decimal(valor):
    """
    Trata strings com formatos de moeda/decimais (ex: '1.250,50' ou '1250.50')
    e converte para Float.
    """
    if pd.isna(valor):
        return None
    
    valor_str = str(valor).strip()
    
    # Se o valor contiver tanto ponto quanto vírgula (ex: 1.234,56)
    if '.' in valor_str and ',' in valor_str:
        valor_str = valor_str.replace('.', '').replace(',', '.')
    # Se contiver apenas vírgula como separador decimal (ex: 1234,56)
    elif ',' in valor_str:
        valor_str = valor_str.replace(',', '.')
        
    try:
        return float(valor_str)
    except ValueError:
        return None
