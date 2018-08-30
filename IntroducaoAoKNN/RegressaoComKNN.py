from sklearn.datasets import load_boston
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
"""

Dataset que é referente aos dados de preços de casas em Boston

"""
"""

Função na qual faz o knn com o fit diretamente com os dados

"""
def precisaoComFit ( knn, boston ) :

    y = knn.fit ( boston.data, boston.target ).predict ( [
        boston.data [ i ] for i in range ( len ( boston ) )
    ] )

    for i in range ( len ( boston.data ) ) :

        acu = boston.data[i]/boston.target [ i ]

        print("( Elemento {} )Dado esperado : {} ||| Dado Previsto : {}\n\n".format(
            i + 1,
            boston.target [ i ],
            knn.predict ( [ boston.data [ i ] ] )
        ))

    print("Precisão da máquina : {}\n\n".format ( 100*acu/len ( boston.data ) ) )

"""

Função na qual fazemos a predição sem a utilização do fit diretamente com os dados
para treinar o knn

"""
def predicao ( knn, boston ) :

    acu = 0

    for i in range ( len ( boston.data ) ) :

        acu = boston.data[i]/boston.target[ i ]

        print(" ( Elemento {} ) Dado esperado : {} ||| Dado Previsto : {}\n\n".format(
            i + 1
            ,boston.target [ i ],
            knn.predict ( [ boston.data [ i ] ] )
        ))

    print(" Precisão da máquina : {}\n\n".format ( 100*acu/len ( boston.data ) ) )
    print("\n------------\n")
    return

def main (  ) :

    boston = load_boston (  )

    print("Descrição do dataset : \n\n{}\n\n".format ( boston.DESCR ) )
    print("Descrição dos dados : ( quantidade, dados por linha ) = {} \n".format(
        boston.data.shape
    ))
    print("Informação do array : \n\n{}\n\n".format ( boston.feature_names ) )

    # quantidade de dados vizinhos que iremos pegar
    knn = KNeighborsRegressor ( n_neighbors = 9 )
    knn.fit ( boston.data, boston.target )

    predicao ( knn, boston )
    precisaoComFit ( knn, boston )

    # pegando apenas os primeiros 50 dados
    x, y = boston.data[:50], boston.target[:50]
    predict = knn.fit ( x, y ).predict ( x )
    fig = plt.figure()
    plt.plot ( np.linspace ( -1, 1, 50 ), y, label = "Dado original", color = "red" )
    plt.plot(np.linspace(-1, 1, 50), predict , label="Previsto", color="blue")
    plt.title("Classificação Dos Dados")
    plt.legend(loc="upper right")
    plt.show(label=True)

main()