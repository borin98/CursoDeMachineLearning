import pandas as pd

def main ( ) :

    n = 0

    df = pd.DataFrame ( columns = [ "Nome", "Estrelas" ] )

    # criando o dataframe

    while ( n <= 0 ) :

        n = ( int ) ( input("Digite o tamanho do dataframe : ") )

        if ( n <= 0 ) :

            print("Valor inválido !!!!\n")


    for i in range ( n ) :

        elemento = input("Digite o nome do elemento {} : ".format ( i + 1 ) )
        nota = ( int ) ( input ( "Digite a nota do elemento {} : ".format ( i + 1 ) ) )
        df.loc[i] = [elemento, nota]

    print(df)

    print("Pegando a coluna Nome\n")
    print(df["Nome"])

    print("\nPegando a coluna Estrelas\n")
    print(df['Estrelas'])

    print("\nPegando a média das estrelas : {}\n".format ( df["Estrelas"].mean() ) )
    print("\nPegando a mediana das estrelas : {} \n".format ( df["Estrelas"].median() ) )

    # nesse caso, ele retorna um dicionário
    print("\nPegando os elementos de uma linha\n")
    print(df.iloc[0])

main()