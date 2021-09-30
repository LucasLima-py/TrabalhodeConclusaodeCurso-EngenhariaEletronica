import pandas as pd
import numpy as np
from scipy import linalg
import xlrd
import matplotlib.pyplot as plt
import seaborn as sns
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
import itertools

base = pd.read_excel(r'dataset preparado.xlsx', engine='openpyxl')

print(base.columns.values)

moda = base.mode()
moda = moda.iloc[0:1]#.values
print(moda)

print(base.describe())

print(f"""O dataframe base possui:
- {base.shape[0]} registros; e
- {base.shape[1]} atributos, incluindo a variável resposta ("Saída").
""")

# sns.pairplot(base, diag_kind="hist")
# sns.set(style="ticks", color_codes=True)
# plt.show()

previsores = base.iloc[:,:11].values #ESCOLHER QUAL COLUNA QUER AGRUPAR
#classe = base.iloc[:,9:10].values
classe = base['Classe'].values
# teste = base.iloc[8991:,0].values
# teste_2 = base.iloc[8991:,10].values
# plt.scatter(teste, teste_2)
# plt.show()

def numeroClusters(previsores):
    wcss = []
    for i in range(1, 6):
        kmeans = KMeans(n_clusters = i, init = 'random')
        kmeans.fit(previsores)
        print(i,kmeans.inertia_)
        wcss.append(kmeans.inertia_)  

    plt.plot(range(1, 6), wcss)
    plt.title('O Metodo Elbow')
    plt.xlabel('Numero de Clusters')
    plt.ylabel('WSS') #within cluster sum of squares
    plt.show()

def a_kmeans(X):
    kmeans = KMeans(n_clusters = 2, init = 'random')
    kmeans.fit(previsores)
    plt.scatter(X[:, 0], X[:,10], s = 10, c = kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 10], s = 500, c = 'red',label = 'Centroids')
    plt.title('Clusters and Centroids - Zona 1 e 6')
    plt.xlabel('SepalLength')
    plt.ylabel('SepalWidth')
    plt.legend()

    plt.show()


def gmm(X):
    gmm = GaussianMixture(n_components=5, covariance_type='full')
    gmm.fit(X)


def a_dbscan(X):
    dbscan = DBSCAN(eps=2, min_samples=100)
    dbscan.fit(previsores)
    print(dbscan.labels_)
    print(dbscan.core_sample_indices_)
    print(dbscan.components_)
    plt.scatter(X[:,0], X[:,10], s = 10, c = dbscan.labels_)
    plt.title('Clusters and Centroids')
    plt.xlabel('SepalLength')
    plt.ylabel('SepalWidth')
    plt.legend()
    plt.show()

numeroClusters(previsores)
a_kmeans(previsores)
#gmm(previsores)
#a_dbscan(previsores)

