# Importando Biblíotecas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregando base de dados para visualização
# Leitura com tratamento para que cada informação de linha fique sob sua coluna mantendo a visualização organizada

df = pd.read_csv('Base_Varejo.csv', sep=';')

print(df.head(5))
print(df.describe())