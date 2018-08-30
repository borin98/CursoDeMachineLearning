import numpy as np
from sklearn import neighbors
from sklearn.model_selection import train_test_split

"""

Programa que iremos utilizar o dataset da Iris para classificarmos ele com sklearn

Informações do dataset : This is perhaps the best known database to be found in the pattern recognition literature. 
Fisher's paper is a classic in the field and is referenced frequently to this day. 
(See Duda & Hart, for example.) 
The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. 
One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 
Predicted attribute: class of iris plant. 
This is an exceedingly simple domain. 

Informações dos atributos do datset : 

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
    1 =  Iris Setosa 
    2 = Iris Versicolour 
    3 =  Iris Virginica
"""

def main (  ) :

    dadosEntrada = np.genfromtxt("iris.data", delimiter = ",", usecols= ( 0, 1, 2, 3) )
    dadosResposta = np.genfromtxt("iris.data", delimiter=",", usecols=(4))

    entradaTreino, entradaTeste, saidaTreino, saidaTeste = train_test_split(dadosEntrada, dadosResposta,
                                                                            test_size=0.3, random_state=42)

    knn = neighbors.KNeighborsClassifier ( n_neighbors = 3 )
    knn.fit ( entradaTeste, saidaTeste )

    predicao = knn.predict ( entradaTeste )
    acertos = np.sum ( predicao == saidaTeste )

    print("\nTotal de acertos : {} acertos de 45 dados".format ( acertos ) )
    print("Precisão de acertos : {} % ".format ( 100 * knn.score ( entradaTeste, saidaTeste ) ) )

main()
