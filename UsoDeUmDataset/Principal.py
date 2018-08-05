import numpy as np
import matplotlib.pyplot as plt

def sobreposicaoDosPlots ( data ) :

    plt.plot(data[100: 150, 0], c="Green", ls="--", marker="x", ms=8, label="Comprimento Sépala Iris-Virginica")
    plt.plot ( data[50 : 100, 0], c = "Black", ls = "-", marker = "o", ms = 8, label = "Comprimento Sépala Iris-Versicolor" )
    plt.plot(data[:50, 0], c="Red", ls=":", marker="s", ms=8, label="Comprimento Sépala Iris-Setosa")
    plt.legend()
    plt.show (  )

    return

def plotIrisVirgi ( data ) :

    plt.plot ( data[100 : 150, 0], c = "Green", ls = "--", marker = "x", ms = 8, label = "Comprimento Sépala Iris-Virginica" )
    plt.legend()
    plt.show ( )

    return

def plotIrisVerci ( data ) :

    plt.plot ( data[50 : 100, 0], c = "Black", ls = "-", marker = "o", ms = 8, label = "Comprimento Sépala Iris-Versicolor" )
    plt.legend()
    plt.show (  )

    return

def plotIrisSetosa ( data ) :

    # plotando apenas a primeira coluna de todos os dados da iris setosa

    plt.plot ( data[ :50, 0 ], c = "Red", ls = ":", marker = "s", ms = 8, label = "Comprimento Sépala Iris-Setosa" )
    plt.legend()
    plt.show (  )

    return

def main ( ) :

    # carregando o arquivo
    data = np.genfromtxt ( "iris.data.txt", delimiter=",", usecols= ( 0, 1, 2, 3 ) )

    plotIrisSetosa ( data )
    plotIrisVerci ( data )
    plotIrisVirgi ( data )
    sobreposicaoDosPlots ( data )

    return

main()