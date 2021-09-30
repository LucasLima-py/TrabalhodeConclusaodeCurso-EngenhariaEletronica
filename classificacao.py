import pandas as pd
import numpy as np
from scipy import linalg
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import cross_validate
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.cluster import DBSCAN, KMeans
from sklearn.mixture import GaussianMixture
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from lazypredict.Supervised import LazyClassifier
from sklearn import datasets
from pandas import ExcelWriter
import graphviz
from datetime import date
import itertools
import xlrd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_excel(r'dataset teste.xlsx', engine='openpyxl')

print(base.columns.values)
print(base.describe())
print(f"""O dataframe base possui:
- {base.shape[0]} registros; e
- {base.shape[1]} atributos, incluindo a variável resposta ("Saida").
""")

previsores = base.iloc[:,:12].values #ESCOLHER QUAL COLUNA QUER AGRUPAR
#classe = base.iloc[:,9:10].values
classe = base['Classe'].values

print(classe)

X,Y = previsores,classe
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 10)
def Lazy():
    clf = LazyClassifier(predictions = True)
    models, predictions = clf.fit(X_train,X_test,Y_train,Y_test)
    print(list(models))
    tabela_resultados = pd.DataFrame(models)
    print(tabela_resultados)

    tabela_resultados.to_excel('resultados-classificacao.xlsx')
    print("excel gerado com sucesso")

def modelo():
    modelo = LinearSVC() #modelo está suceptível a variações escalonárias (devemos fazer um ajuste na escala)
    # modelo.fit(previsores,classe)
    # misterioso = [2567.3, 2608.2, 2792.1, 1793.8, 2736.02, 2696.5, 2739.2, 2545.1, 2699.3, 2831.9, 2738.7, 2696.5]
    # resultado = modelo.predict(misterioso)
    # print("o resultado foi: ", resultado)
    modelo.fit(X_train,Y_train)
    previsoes = modelo.predict(X_test)
    tabela1 = list(X_test)
    tabela = pd.DataFrame(tabela1)
    misterioso_teste = tabela.iloc[0,:].values.tolist()
    # print(misterioso_teste)
    # result = modelo.predict(misterioso_teste)
    # print("o resultado foi: ", misterioso_teste)
    #tabela.to_excel('teste xtest.xlsx')
    print(previsoes)
    acuracia = accuracy_score(Y_test, previsoes) *100
    print("A acuracia da rede foi de: %.2f" %acuracia)
    # misterioso = [2567.3, 2608.2, 2792.1, 1793.8, 2736.02, 2696.5, 2739.2, 2545.1, 2699.3, 2831.9, 2738.7, 2696.5]
    # misterioso3 = [2465,2330,2537,1725,2858,2858,2804,2805,2887,2887,2829,2829]
    # misterioso2 = [1,1,1,1,1,1,1,1,1,1,1,1]
    # teste = [misterioso3,misterioso2]
    # resultado = modelo.predict(teste)
    # print("o resultado foi: ", resultado)
    

modelo()
#Lazy()
