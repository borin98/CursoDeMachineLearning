import numpy as np

# criando uma função com apenas algumas das operações não tanto triviais entre matrizes
def OperacoesMatrizes ( mat1, mat2 ) :

    print("Divisao entre a matriz m1 e m2 {} ".format ( mat1/mat2 ) )
    print("Arredondando a divisão da matriz m1 e m2 {} ".format ( np.matrix.round ( mat1/mat2 ) ) )

def PegaValor (  ) :

    n = 0

    while ( n <= 0 ) :

        n = (int)(input("Digite o tamanho do vetor : "))

        if ( n <= 0 ) :

            print ( "Valor inválido !!!" )

    return n

def main ( ) :

    n = PegaValor ( )

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    for i in range ( n ) :

        valor = (float) ( input("\nDigite o valor do índice {} : ".format ( i + 1 ) ) )
        lista1.insert(i, valor )

    lista2 = lista3 = lista4 = lista1

    # criando a matriz denominada pontos
    pontos = np.array( [lista1, lista2, lista3, lista4] )
    print ( pontos, end="\n" )

    # criando um dataset que é um vetor que começa em zero e vai até n - 1
    dataset = np.arange(0, n)
    print("criando um dataset que é um vetor que começa em zero e vai até n - 1")
    print ( dataset, end="\n" )

    # remodelando o vetor dataset para uma matriz 2 X n
    print("remodelando o vetor dataset para uma matriz 2 X n")
    mat1 = np.resize ( dataset, (2, n) )
    print(mat1)

    # pegando o último ítem da mat1
    print("pegando o último ítem da mat1")
    print(mat1.item ( n-1 ), end="\n" )

    OperacoesMatrizes ( mat1, pontos )

main()

