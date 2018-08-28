import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
    Função que produz alguns tipos de gráficos
    para exemplo 
"""
def implementacaoDoGrafico ( df ) :

    # plotando os dois gráficos
    plt.plot ( df["Year"], df["crimes.total"], "-r" )
    plt.plot ( df["Year"], df["crimes.person"], "-b")
    plt.show()

    # colocando as legendas no gráfico
    grafAux = plt.subplot()
    grafAux.plot (  df["Year"], df["crimes.total"], "-r", label = "Crimes totais" )
    grafAux.plot ( df["Year"], df["crimes.person"], "-b", label = "Crimes por pessoa")
    grafAux.legend( loc="upper left" )
    plt.show()

    # fazendo a descrição dos eixos
    aux = plt.subplot()
    aux.plot(df["Year"], df["crimes.total"], "-r", label="Crimes totais")
    aux.plot(df["Year"], df["crimes.person"], "-b", label="Crimes por pessoa")
    aux.legend(loc="upper left")
    aux.set_xlabel ( "Quantidade" )
    aux.set_ylabel("Ano")
    aux.set_title("Crimes : Total x pessoas")
    plt.show()

    # limitando a função e salvando ela
    fig = plt.figure()
    plt.plot(df["Year"], df["crimes.total"], "-r", label = "Crimes totais" )
    plt.plot(df["Year"], df["crimes.person"], "-b", label = "Crimes por pessoa" )
    plt.legend ( loc = "upper left" )
    plt.xlabel("Quantidade")
    plt.ylabel("Ano")
    plt.title("Crimes : Total x pessoas")
    plt.xlim(df["Year"].min(), df["Year"].max())
    plt.show()
    fig.savefig("Gráfico-Crime_Por_Pessoa.png")

    return

"""
    Função utilizada para imprimir os valores dos dados NaN
"""
def printDataset ( df ) :

    print("Antes do preenchimento : \n\n")

    for i in range ( len (df) ) :

        teste = np.isnan ( df["vehicle.theft"].iloc[i] )

        if ( teste == True ) :

            print( "Valor i = {0} e df[{1}] = {2}".format ( i, i, teste ) )

    return

def main (  ) :

    # carregando o dataset
    df = pd.read_csv ( "reported.csv" )

    print("Analizando o head do dataset : \n\n{}\n\n".format ( df.head (  ) ) )

    # preenchendo os valores Nan
    printDataset(df)
    df.fillna ( 0, inplace=True )
    print("Depois do preenchimento : \n\n{}\n\n".format ( df["vehicle.theft"].head ( df.__len__() ) ) )

    implementacaoDoGrafico ( df )


main()