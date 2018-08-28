import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
import locale

"""
    Função que cria o gráfico de df
"""
def grafico ( df ) :

    ax = plt.subplot()

    plt.plot_date ( df.index.to_pydatetime(),
                    df["views"],
                    "b-")

    # fazendo o plot da função
    locale.setlocale(locale.LC_ALL, "pt_BR")
    ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5, 32, 5)))
    ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
    ax.xaxis.grid(True, which="minor")
    ax.yaxis.grid()
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
    plt.tight_layout()
    plt.show()



"""
    Função que faz somas de tempos e retorna o valor em hora
"""
def retornaHora ( v ) :

    return dt.datetime(2017, 1, 1) + dt.timedelta ( hours=v )

def main (  ) :

    # carregando o dataset
    df = pd.read_csv("ppz-jan-fev-2017.csv")

    print("Vendo o head do dataset : \n\n{}\n\n".format ( df.head ( df.__len__() ) ) )

    # criando uma nova coluna de datas
    df["date"] = df["hour"].apply(retornaHora)
    print("Analisando o novo dataset : \n\n{}\n\n".format( df.head ( df.__len__() ) ) )
    del df["hour"]

    # criando um novo índice utilizando a data
    df.set_index( ["date"], inplace=True )
    print("Analisando o novo dataset : \n\n{}\n\n".format(df.head(df.__len__())))

    grafico ( df )

main()
