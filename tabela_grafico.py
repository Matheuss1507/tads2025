import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame({
    'Idade': [20, 23, 27, 31, 35],
    'Nome': ['João', 'Maria', 'José','Sofia','Helena']
})

plt.hist(tabela['Idade'])