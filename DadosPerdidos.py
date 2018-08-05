import pandas as pd
import numpy as np

def main ( ) :

    # utilizando um modelo de exemplo de dataframe
    dados = {
        'nome': ['João', 'Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
        'sexo': ['M', 'F', 'M', np.nan, 'M', 'M', np.nan],
        'idade': [14, 13, np.nan, np.nan, 15, 13, 14],
        'nota': [4, 10, 7, np.nan, 8, 9, 7]
    }
    df = pd.DataFrame(dados)

    # removendo a linha que contém pelo menos um NaN
    print("removendo a linha que contém pelo menos um NaN : \n\n{}\n".format ( df.dropna() ) )

    # removendo a linha que contém todos seus elementos como NaN
    print("removendo a linha que contém todos seus elementos como NaN : \n\n{}\n".format ( df.dropna(how = "all") ) )

    # criando uma coluna de elementos vazios
    df["series"] = np.nan
    print("criando uma coluna de elementos vazios : \n\n{}\n".format ( df ) )

    # dando drop em uma coluna
    print("dando drop em uma coluna : \n\n{}\n".format ( df.dropna(how = "all", axis = 1) ) )

    # retirando o dado caso aparece pelo pelos 3 NaN
    print("retirando o dado caso aparece pelo pelos 3 NaN : \n\n{}\n".format ( df.dropna ( thresh = 3 ) ) )

    # preenchendo os dados faltantes com outro valor
    df["series"].fillna(8, inplace=True)
    print("preenchendo os dados faltantes com outro valor : \n\n{}\n".format ( df ) )

    # preenchendo os dados faltantes da coluna idade com a média
    df["idade"].fillna(df["idade"].mean( ), inplace=True)
    print("preenchendo os dados faltantes com a média : \n\n{}\n")

    # fazendo filtro para remover os dados Nan nas colunas nome e sexo, Neste caso iremos não deixar null nome e sexo
    print("fazendo filtro para remover os dados Nan nas colunas nome e sexo : \n\n{}\n".format ( df[df["nome"].notnull ( ) & df["sexo"].notnull()] ) )

main()