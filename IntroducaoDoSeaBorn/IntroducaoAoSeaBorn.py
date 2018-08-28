import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
"""
    Função que cria os gráficos
"""
def grafico ( x ) :

    # criando os gráficos
    plt.plot ( x, np.sin ( x ), "b--" )
    plt.plot ( x, np.cos ( x ), "r--" )
    plt.show (  )

    return

def main (  ) :

    # criando dados aleatórios
    x = np.linspace ( 1, 10, 100 )

    grafico ( x )

main()