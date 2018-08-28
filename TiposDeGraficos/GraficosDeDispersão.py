from matplotlib.pyplot import show, plot, scatter
import pandas as pd
import numpy as np
import pydataset
import seaborn as sns

"""
    
    Função que é chamada no apply da iris da seguinte forma :
    faz um looping que passa por todos os elementos do dataset e classifica cada coluna em ?
    0 - setosa
    1 - versicolor
    2 - caso contrário
    
"""
def classificaSentosa ( iris ) :

    if ( iris == "setosa" ) :

        return 0

    elif ( iris == "versicolor" ) :

        return 1

    return 2

"""
    Função que trata o dataset da iris
"""

def funcaoIris (  ) :

    iris = pydataset.data("iris")

    print("Fazendo o printo do head dad iris : \n\n{}\n\n".format ( iris.head ( 40 ) ) )

    # fazendo o gráfico de disperção da iris
    scatter ( iris["Sepal.Length"],
              iris["Sepal.Width"],
              sizes = 10 * iris["Petal.Length"] )
    show (  )

    # criando nova coluna para a classificação das setosas
    # estamos aplicando a função de classificação para cada elemento
    iris["SpeciesNumber"] = iris["Species"].apply ( classificaSentosa )
    scatter(iris["Sepal.Length"],
            iris["Sepal.Width"],
            sizes=20 * iris["Petal.Length"],
            c = iris["SpeciesNumber"],
            cmap="viridis",
            alpha=0.4)
    show()

def main (  ) :

    # carregando o dataset
    df = pydataset.data ( "AirPassengers" )

    print("Analizando o head dos 12 elementos de df : \n\n{}\n\n".format( df.head ( 12 ) ) )

    # fazendo o plot da dispersão de df
    scatter ( df["time"], df["AirPassengers"] )
    show()

    funcaoIris()

main()