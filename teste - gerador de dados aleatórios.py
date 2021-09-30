import random
import pandas as pd

a = []
# for i in range(0,4000):
#     a.append(random.triangular(2300,2400,2450))
#     i = i + 1

# b = []
# for i in range(0,4990):
#     b.append(random.triangular(2176,2280,2228))
#     i = i + 1

# lista = a + b

for i in range(0,8990):
    try:
        a.append(random.triangular(217.6,228.0,222.8))
        i = i + 1
    except:
        pass

dataframe = pd.DataFrame(a)
dataframe.to_excel('dados_aleatórios.xlsx')
print("excel gerado com sucesso")