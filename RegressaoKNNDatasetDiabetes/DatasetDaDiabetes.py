from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from math import sqrt
from sklearn.metrics import mean_squared_error

def main (  ) :

    diabetes = datasets.load_diabetes (  )

    xTreino, xTeste, yTreino, yTeste = train_test_split(
        diabetes.data,
        diabetes.target,
        test_size = 0.3,
        random_state = 42
    )

    k = ( int ) ( sqrt ( len(diabetes) ) )

    knn = KNeighborsRegressor ( n_neighbors = k  , p = 2 )
    knn.fit ( xTreino, yTreino )

    saida = knn.predict ( xTeste )
    mean_squared_error ( yTeste, saida )

    for i in range ( len( xTeste ) ) :

        print("Saída esperada : {} ".format ( yTeste[i] ) )
        print("Saída obtida : {} \n".format ( saida[i] ) )

    print("Erro quadrado médio :{}".format ( mean_squared_error(
        yTeste,
        saida
    ) ) )

main()