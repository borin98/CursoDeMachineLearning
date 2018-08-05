import pandas as pd
import numpy as np

"""
    Função que retorna um dataframe de apenas somas de dados maiores que 300000
"""
def fraction_votes_filter ( x ) :

    return x["votes"].sum() > 300000

def main() :
    # carregando os resultados
    df = pd.read_csv ( "primary-results.csv" )
    pd.option_context("max_info_columns", 8)

    # analizando o cabeçalho do arquivo
    print("analizando o cabeçalho do arquivo : \n\n{}\n".format( df.head ( ) ) )

    # tamanho dos dados
    print("tamanho dos dados : \n\n{}\n".format ( df ) )

    # agrupando sobre a coluna candidato sobre a média, máximo e mínimo dos votos de cada candidato
    print("agrupando sobre a coluna candidato : \n\n{}\n".format ( df.groupby("candidate").aggregate(
        {"votes" : [min, np.mean, max]}
    ) ) )

    # procurando onde na linha a candidata Hillary conseguiu seus votos máximos
    print("procurando onde na linha a candidata Hillary conseguiu seus votos máximos : \n\n{}\n".format ( df[
    df ["votes"] == 590502
    ] ) )

    # fração de votos de cada candidato nos municípios
    print("fração de votos de cada candidato nos municípios : \n\n{}\n".format ( df.groupby("candidate").aggregate(
        {"fraction_votes" : [min, np.mean, max]}
    ) ) )

    # analizando o local onde os conseguiram votos de 100%
    print("analizando o local onde a candidata Hillary conseguiu votos de 100% : \n\n{}\n".format(df[
    df ["fraction_votes"] == 1
    ] ) )

    # analizando os locais onde a candidata Hillary conseguiu votos de 100%
    print("analizando os locais onde a candidata Hillary conseguiu votos de 100% : \n\n{}\n".format(df[
    (df["fraction_votes"] == 1) & ( df["candidate"] == "Hillary Clinton" )
    ] ) )

    # agrupando pelo estado com a soma de votos acima de 300000
    print("agrupando pelo estado com a soma de votos acima de 300000 : \n\n{}\n".format (
    df.groupby("state").filter(fraction_votes_filter)
    ) )

    # fazendo a verificação do resultado anterior
    print("fazendo a verificação do resultado anterior : \n\n{}\n".format ( df[
    df["state_abbreviation"] == "AL"]["votes"].sum()
    ) )

    # fazendo um agrupamento por state_abbreviation e candidates por soma
    print("fazendo um agrupamento por state_abbreviation e candidates por soma : \n\n{}\n".format (
    df.groupby ( ["state_abbreviation", "candidate"] )["votes"].sum()
    ) )

main()