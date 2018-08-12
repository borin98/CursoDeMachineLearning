import pandas as pd
import numpy as np

def op ( database ) :

    primaryDfGroupby = database.groupby (
        ["state", "party", "candidate"]
    ).sum()

    # descartando as colunas do fips e fraction_votes
    del primaryDfGroupby["fips"]
    del primaryDfGroupby["fraction_votes"]
    primaryDfGroupby.reset_index ( inplace=True )

    return primaryDfGroupby

def config (  ) :

    pd.set_option("display.max_rows", 100)
    pd.set_option("display.max_columns", 10)
    pd.set_option("display.max_colwidth", 10)
    pd.set_option("display.width", None)

def main (  ) :

    # configurando o display dos dados
    config()

    # carregando o database
    database = pd.read_csv ( "primary-results.csv" )

    # analizando os nomes únicos dos candidatos
    print("analizando os nomes únicos dos candidatos : \n{}\n".format (
        database["candidate"].unique()
    ) )

    # iremos organizar os dados da forma estado, partido e candidato onde serão a soma dos elementos
    pivotTable = pd.pivot_table(
        database, index=["state", "party", "candidate"], values=["votes"],
        aggfunc={"votes":np.sum}
    )

    print("Printando os dados do pivotTable : \n{}\n ".format ( pivotTable ) )

    # iremos melhorar este pivotTable, criando um Ranking

    database["rank"] = database.groupby (
        ["county", "party"]
    )["votes"].rank(ascending=False)

    print("iremos melhorar este pivotTable, criando um Ranking : \n{}\n".format ( database[ database["county"] ==
                                                                                  "Los Angeles"] )  )

    # organizando os dados
    primaryDfGroupby = op(database)
    print("Fazendo o printo do novo dataframe : \n{}\n".format ( primaryDfGroupby.head (  ) ) )

    # organizando por ranking os dados do primary group
    primaryDfGroupby["rank"] = primaryDfGroupby.groupby(
        ["state", "party"]
    )["votes"].rank( ascending=False )

    print("Printando os dados do primaryDfGroupby de forma melhorada : \n{}\n".format ( primaryDfGroupby.head ( 7 ) ) )

    # criando a pivotTable desta coluna
    ranking = pd.pivot_table (
        primaryDfGroupby, index=["state", "party", "candidate"],
        values=["rank", "votes"]
    )

    print("Printando o database de ranking pivotado : \n{}\n".format ( ranking ) )

    # pegando os valores onde o ranking foi em primeiro lugar
    print("pegando os valores onde o ranking foi em primeiro lugar : \n{}\n".format(
        primaryDfGroupby[ primaryDfGroupby["rank"] == 1 ]["candidate"].value_counts()
    ))

main()