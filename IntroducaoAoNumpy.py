import numpy as np

def operacoes ( mat, trans ) :

    newSoma = mat + mat
    print ( "\nResultado da soma entre matrizes" )
    print(newSoma)

    newSubtracao = mat - trans
    print("\nResultado da subtração entre a matriz original e sua inversa")
    print(newSubtracao)

    newMultiplicacao = mat * mat
    print("\nResultado da multiplicação entre mat e mat")
    print(newMultiplicacao)

    newSum = mat.sum()
    print("\nResposta da soma de todos os elementos")
    print(newSum)

    eleMax = mat.argmax()
    print("\nValor máximo em mat é : {}".format ( eleMax ) )

    eleMin = mat.argmin()
    print("\nValor mínimo é : {}".format ( eleMin ) )

def PegaValor (  ) :

    n = 0

    while ( n <= 0 ) :

        n = (int)(input("Digite o tamanho do vetor : "))

        if ( n <= 0 ) :

            print ( "Valor inválido !!!" )

    return n

def main ( ) :

    n = PegaValor ( )

    lista = []

    for i in range ( n ) :

        valor = (float) ( input("\nDigite o valor do índice {} : ".format ( i + 1 ) ) )
        lista.insert(i, valor )


    # adicionando o vetor para array
    inputArray = np.array( lista )
    newRow = inputArray

    # printando o tipo de array que ele é
    print ( type ( newRow ) )

    # criando uma matriz de tamanho n X n
    for i in range ( n ) :
        mat = np.vstack ( [ inputArray, newRow ] )

    # pegando um elemento da primeira linha e coluna como exemplo
    print("\nO elemento  da linha 1 e coluna 1 : {} ".format ( mat[0][0] ))

    # pegando a matriz transposta de mat
    trasn = mat.transpose()
    print("\n")
    print(trasn)

    # realizando algumas operacoes com matrizes
    operacoes ( mat, newRow )

    return

main()