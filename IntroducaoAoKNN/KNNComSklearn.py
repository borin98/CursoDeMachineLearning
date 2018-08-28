from sklearn.neighbors import KNeighborsClassifier
from math import sqrt

""" 

Este programa é similar ao programa do EscolhaDoK.py.
Porém com a difença que utilizaremos a biblioteca do sklearn para fazermos
a implementação do método do knn
Além disso, iremos retirar a coluna do ano

"""
"""

Função que faz a classificação dos cados e printa o resultado da precisão

"""
def classificacao ( limite, predicao, entrada, saida ) :

    acertos, indiceLabel = 0, 0
    divisor = len ( entrada ) - limite

    for i in range ( limite, len ( entrada ) ) :

        if ( predicao [ indiceLabel ] == saida [ i ] ) :

            acertos += 1

        indiceLabel+= 1

    print("\nTotal de dados de treinamento : {}".format ( limite ) )
    print("Total de testes : {}".format ( len ( entrada ) - limite ) )
    print("Total de acertos : {}".format ( acertos ) )
    print("Precisão do modelo : {0:.2f} %".format ( (100*acertos )/divisor ) )

    return

"""

Função que monta os datasets entrada e saida

entrada possui os dados da coluna 0 e 2
enquanto saida possui os dados da coluna 3

"""

def leituraInicial ( entrada, saida ) :

    with open ( "HabermanSDataset.txt", "r" ) as f :

        for linha in f.readlines (  ) :

            atributo = linha.replace ( "\n", "" ).split ( "," )

            entrada.append ( [
                int ( atributo[0] ),
                int ( atributo[2] )
            ] )

            saida.append ( int ( atributo [3] ) )

    return

def main (  ) :

    # dados de entrada e saída
    entrada, saida = [],[]
    leituraInicial ( entrada, saida )

    # limite dos dados que serão utilizados como dados de treinamento
    limite = int ( 0.6*len ( entrada ) )

    # definindo o valor de k
    k = (int) ( sqrt ( len ( entrada ) ) )

    # criando o objeto que será o knn para treino
    knn = KNeighborsClassifier ( n_neighbors=k )

    # treinando o modelo do knn
    knn.fit ( entrada[:limite], saida[:limite] )

    # dados de predicao
    predicao = knn.predict ( entrada[limite:] )

    classificacao ( limite, predicao, entrada, saida )

main()
