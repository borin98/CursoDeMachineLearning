import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from math import sqrt

"""

Função que mexe com um arquivo CSV sobre sapatos que funciona da seguinte forma :

Coluna 0 : tamanho do sapato
Coluna 1 : Peso da pessoa
Coluna 2 : Tipo de pessoa ( Senior ou fourth - primario )

"""

def main (  ) :

    # montando os dados de teste e treino
    dadosTreino = pd.read_csv ( "train.csv" )
    dadosTeste = pd.read_csv ( "test.csv" )

    # montando um numPY array dos dados de treino e teste
    col1 = ["shoe size", "height"]
    col2 = ["class"]
    xTreino = dadosTreino.as_matrix ( col1 )
    yTreino = dadosTreino.as_matrix ( col2 )
    xTeste = dadosTeste.as_matrix ( col1 )
    yTeste = dadosTeste.as_matrix ( col2 )

    # montando o parâmetro k
    k = int ( sqrt ( len ( dadosTreino ) + len ( dadosTeste ) ) )

    # montando o parâmetro knn
    knn = KNeighborsClassifier ( n_neighbors = k, weights = "distance" )
    knn.fit ( xTreino, yTreino.ravel() )

    predicao = knn.predict ( xTeste )
    acertos = np.sum ( predicao == yTeste )
    porcentagemAcertos = knn.score ( xTeste, yTeste )
    print("Quantidade de dados acertados : {} acertos de 11329 dados \n\n".format ( acertos ) )
    print("Porcentagem de acertos : {} %\n\n".format ( porcentagemAcertos*100 ) )

main()
