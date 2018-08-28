from matplotlib.pyplot import show, plot, scatter
import pandas as pd
import numpy as np
import pydataset
import seaborn as sns
import mplleaflet as mp

def main (  ) :

    # setando o dataframe
    df = pd.read_csv ( "copacabana_lat_lng.csv" )

    print("Analizando o head do dataframe : \n\n{}\n\n".format ( df.head (  ) ) )
    print("Tamanho do dataframe : \n\n{}\n\n".format ( df.__len__() ) )


    # montando o gráfico de dispersão
    scatter( df["lng"],
             df["lat"],
             marker=".")

    mp.show()

main (  )