import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from math import sqrt

"""

        Informações do dataset
        
link do dataset : https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival

informação do dataset :

This data set was generated to model psychological experimental results. 
Each example is classified as having the balance scale tip to the right, tip to the left, or be balanced. 
The attributes are the left weight, the left distance, the right weight, and the right distance. 
The correct way to find the class is the greater of (left-distance * left-weight) and (right-distance * right-weight). 
If they are equal, it is balanced.

informações do atributo :

1. Class Name: 3 (L, B, R) 
2. Left-Weight: 5 (1, 2, 3, 4, 5) 
3. Left-Distance: 5 (1, 2, 3, 4, 5) 
4. Right-Weight: 5 (1, 2, 3, 4, 5) 
5. Right-Distance: 5 (1, 2, 3, 4, 5)


São 625 exemplos dos quais, na coluna 0
Onde tem "L" corresponde ao valor 1
"B" corresponde ao valor 2
"R" corresponde ao valor 3 

"""

def main (  ) :

    # carregando o arquvio pegando apenas os dados da coluna 1 à 4
    entrada = np.genfromtxt ( "dataset.data", delimiter = ",", usecols = ( 1, 2, 3, 4 ) )
    saida = np.genfromtxt ( "dataset.data", delimiter = ",", usecols = (0) )

    print("Tamanho do dados de entrada : {} dados\n\n".format(len(entrada)))
    print("Tamanho dos dados de saída : {}\n\n".format(len(saida)))

    print("Dados de entrada : {}\n\n".format(entrada))
    print("Dados de saída : {}\n\n".format(saida))

    # criando os modelos de treino e teste do dataset
    # 30 % dos dados serão para testes e 40 % para treino
    entradaTreino, entradaTeste, saidaTreino, saidaTeste = train_test_split ( entrada, saida,
                                                                              test_size=0.3, random_state=42)

    # parâmetro k do knn e o knn terá norma euclidiana
    k = int ( sqrt ( len ( entrada ) ) )
    knn = KNeighborsClassifier ( k, p=2 )

    # fazendo o treino do modelo
    knn.fit ( entradaTreino, saidaTreino )

    # criando a predição
    predicao = knn.predict ( entradaTeste )

    acertos = np.sum ( predicao == saidaTeste )
    porcentagemAcertos = knn.score( entradaTeste, saidaTeste )

    print("Quantidade de acertos : {} acertos de {} dados\n\n".format ( acertos, len ( entradaTeste ) ) )
    print("Porcentagem de acertos : {0:.2f} %\n\n".format( 100 * porcentagemAcertos ) )



main()