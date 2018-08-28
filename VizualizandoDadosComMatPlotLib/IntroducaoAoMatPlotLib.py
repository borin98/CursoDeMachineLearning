from matplotlib.pyplot import show
from matplotlib.pyplot import plot
from matplotlib.pyplot import figure
import numpy as np

"""
    Função que cria o módulo do gráfico
"""
def exibindoGrafico ( x ) :

    # salvando a figura
    fig = figure()

    # criando uma função do gráfico que
    plot ( x, np.sin ( x ), "r--" )
    show (  )
    fig.savefig("sin-01.png")

    return

def main (  ) :

    # chamando a função do numpy para facilitar a criação dos dados
    # gerando 100 valores aleatórios que giram entre 1 à 10, na forma de um array
    x = np.linspace ( 1, 10, 100 )

    print(x)

    exibindoGrafico ( x )

main()