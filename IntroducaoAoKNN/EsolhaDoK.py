import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pow

"""

Implementação do método de KNN

Nome do dataset : Haberman's Survival Data Set 

Link do dataset utilizado : https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival

Descrição do dataset : o dataset é referente à sobrevivência de pacientes na cirurgia de câncer de mama, realizado pela 
entre os anos de 1958 e 1970 pelo hospital de chicago billings hospital

Informações do atributo : 

1. Age of patient at time of operation (numerical) 
2. Patient's year of operation (year - 1900, numerical) 
3. Number of positive axillary nodes detected (numerical) 
4. Survival status (class attribute) 
-- 1 = the patient survived 5 years or longer 
-- 2 = the patient died within 5 year

"""

"""

---------------------------------------------------------------------------------------------------------------


"""

"""

Função que faz a implementação do KNN deste dataset

"""

def knn ( treinamento, novaAmostra, k ) :

    distancia, tamTreino = {}, len ( treinamento )

    # calculando a distância euclidiana da  nova amostra
    # para todos os outros exemplos dos conjuntos de treinamento

    for i in range ( tamTreino ) :

        d = distanciaEuclidiana ( treinamento [ i ], novaAmostra )
        distancia[i] = d

    # pegando os k divinhos mais próximos, com as menores distâncias
    k_vizinhos = sorted ( distancia, key=distancia.get )[:k]

    # fazendo a classificação dos valores de
    quantClassificacao1, quantClassificacao2, = 0, 0

    for i in k_vizinhos :

        if ( treinamento [ i ][ -1 ] == 1) :

            quantClassificacao1 += 1

        else :

            quantClassificacao2 += 1

    if ( quantClassificacao1 > 1 ) :

        return 1

    return 2

"""

Função que faz a operação de distância, utilizando a norma euclidiana

"""

def distanciaEuclidiana ( v1, v2 ) :

    soma = 0

    for i in range ( len ( v1 ) ) :

        soma += pow ( ( v1[i] - v2[i] ), 2 )

    return sqrt ( soma )

"""

Função que monta um dataset de Testes

"""
def montaDatasetTeste ( amostra, teste, tamTeste ) :

    for i in range ( ( tamTeste ), len ( amostra ) ) :

        teste.append ( amostra[i] )

    return

"""

Função que monta o dataset de treino

"""
def montaDatasetTreino ( amostra, treinamento, tamTreino ) :

    for i in range ( tamTreino ) :

        treinamento.append ( amostra[i] )

    return

"""

Função que analiza e retorna as informações do dataset 

"""

def informacoesDataset ( amostra ) :

    rotulo1, rotulo2 = 0, 0

    # criando uma nova lista para cada i
    for colunaSobrevivencia in amostra:

        if (colunaSobrevivencia[3] == 1):

            rotulo1 += 1

        else:

            rotulo2 += 1

    return rotulo1, rotulo2

"""

Função que printa o dataset 

"""

def printaDataset ( amostragem ) :

    print("----- Printando o dataset ------\n")

    for i in range ( len( amostragem ) ) :

        print ( "Linha {} = {} ".format( ( i + 1 ), amostragem [ i ] ) )


    sobreviveu, morreu = informacoesDataset ( amostragem )

    porcetagem = ( sobreviveu/len(amostragem) )*100

    print( "\nTamanho do dataset : {} dados".format ( len ( amostragem ) ) )
    print( "Quantidade de Sobreviventes da cirugia do câncer de mama : {} pessoas".format ( sobreviveu ) )
    print( "Quantidade de pessoas que morreram na cirurgia do cancer de mama : {} pessoas".format ( morreu ) )
    print( "Porcentagem de sucesso da circurgia de câncer de mama : {0:.0f} % ".format ( porcetagem ) )

    return

"""

Função que faz a leitura do txt

"""
def leituraDataset ( amostra ) :

    # carregando o dataset
    with open("HabermanSDataset.txt", "r") as f :

        # percorrendo as linhas
        for linha in f.readlines() :

            atributo = linha.replace("\n", "").split(",")
            amostra.append( [
                int( atributo[0]) , int ( atributo[1] ), int( atributo[2] ), int( atributo[3] ) ]
            )

    return

def main (  ) :

    # listra das amostras totais dos dados, para treino e para teste do treino
    amostra, treinamento, teste, resultadoKNN = [], [], [], []
    precisao = 0

    leituraDataset ( amostra )
    printaDataset ( amostra )

    # definindo o tamanho dos dados de treino deste dataset
    # neste caso, será 60% dos dados para treino e 40 % para teste
    tamTreinamento = int ( len( amostra )*0.6 )

    montaDatasetTreino ( amostra, treinamento, tamTreinamento )
    montaDatasetTeste ( amostra, teste, tamTreinamento )

    # definindo um valor para k
    k = ( int ) ( sqrt ( len ( amostra ) ) )

    if ( k % 2 == 0 ) :

        k+= 1

    # fazendo um looping para classificação dos valores
    print("\n------ Classificação por knn ------\n")
    for amostra in teste :

        classe = knn ( treinamento, amostra, k )

        if ( amostra[-1] == classe ) :

            precisao += 1

    print("Porcentagem de acerto da máquina : {0:.0f} %\n\n".format ( ( 100*precisao/len ( teste ) ) ) )

main()