# Importando Biblíotecas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
