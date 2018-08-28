import pandas as pd
import pydataset
import matplotlib.pyplot as plt

"""
    Função que irá analisar o gráfico de pizza do arquivo populacao_brasil.csv
"""
def populacaoBrasileira (  ) :

    # carregando o dataset
    estados = pd.read_csv ( "populacao_brasil.csv" )

    print("Head do dataset Estados : \n\n{}\n\n".format(
        estados.head()
    ))

    estados["total"].hist()
    plt.show()

    # remodelando o gráfico
    aux = plt.subplot()
    plt.hist ( estados["total"], bins=15, orientation="horizontal" )

    # modelando os eixos
    aux.ticklabel_format ( style="plain" )
    plt.show (  )

    # criando uma nova coluna da porcen tagem dos sobreviventes de cada classe
    estados["percent"] = estados["total"] / estados["total"].sum()
    print("Head do estados : \n\n{}\n\n".format(
        estados.head()
    ))

    # gráfico de pizza
    plt.pie ( estados["percent"], labels=estados["estado"], autopct="%1.2f" )
    plt.show()

def main (  ) :

    # setando os dados do dataset e o dataset
    status = pydataset.data ( "titanic",show_doc =True )
    titanic = pydataset.data ( "titanic" )

    print("Informações do dataset TITANIC : \n\n{}\n".format ( status ) )
    print("Dados do dataset TITANIC : \n\n{}\n".format ( titanic.head (  ) ) )
    print("Vizualizando os values acounts do objeto class : \n\n{}\n".format (
        titanic["class"].value_counts()
    ) )

    print("Printando o gráfico de histograma para class : \n")
    titanic["class"].value_counts().plot ( kind="bar" )
    plt.show()

    print("Printando o gráfico do histograma para survived :")
    titanic["survived"].value_counts().plot(kind="bar")
    plt.show()


    print("Analizando quais sobreviventes de quais tipos de classe sobreviveram : \n{}\n".format(
        titanic.groupby ( "survived" )["class"].value_counts() ) )

    print("Fazendo esta mesma análize só que de forma gráfica \n")
    titanic.groupby("survived")["class"].value_counts().plot(kind = "bar")
    plt.show (  )

    populacaoBrasileira()


main (  )