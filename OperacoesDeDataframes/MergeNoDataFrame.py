import pandas as pd

def main (  ) :

    # criando os dataframes

    alunos1 = pd.DataFrame(
        {
            'nome': ['Maria', 'Sofia'],
            'nota': [8, 9],
        }
    )
    alunos2 = pd.DataFrame(
        {
            'nome': ['João', 'Pedro', 'Maria'],
            'cod': [1, 2, 3],
        }
    )

    # fazendo o merge com nome, pegando apenas a interseção dos nomes

    alunosTotal = pd.merge ( alunos1, alunos2, on = "nome" )
    print ( "fazendo o merge com nome, pegando apenas a interseção dos nomes : \n{}\n".format ( alunosTotal ) )

    # fazendo o merge do nome com todos os elementos dos dataframes

    print("fazendo o merge do nome com todos os elementos dos dataframes : \n{}\n".format ( pd.merge(
        alunos1, alunos2, how = "outer" ) )
         )

    # pegando apenas os dados referentes aos alunos1  alunos2 e os dados comuns entre eles
    print("pegando apenas os dados referentes aos alunos1  alunos2 e os dados comuns entre eles : \n{}\n".format ( pd.merge(
        alunos1,alunos2, how= "left"
    ) ) )

    # pegando apenas os dados referentes aos alunos1  alunos2 e os dados comuns entre eles
    print("pegando apenas os dados referentes aos alunos1  alunos2 e os dados comuns entre eles : \n{}\n".format( pd.merge(
        alunos1,alunos2,how="right"
    ) ) )

main()