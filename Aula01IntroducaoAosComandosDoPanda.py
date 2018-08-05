import matplotlib.pyplot as plt
import pandas as pd
import os

#   Inicializando o registro com dados simples
step_data = [3620, 7891, 9761, 3907, 4338, 5373]

#   Escrevendo o código com
step_counts = pd.Series(step_data, name='steps')

print(20 * '-' + " Forma Simples De Utilizar O Step " + 10 * "-")
print(step_counts)
print(30 * "-")

print(20 * '-' + " Forma Simples De Utilizar O Step Para Registrar ano nos registros " + 10 * "-")
step_counts.index = pd.date_range(" 20150329 ", periods=6)
print(step_counts)
print(30 * "-")

print(20 * '-' + " Forma De O Dado Pelo Dígito Do Ano " + 10 * "-")
#   Utiliza uma procura pelo "banco de dados " criado anteriormente em step_counts, porém o utiliza com a data registrada
print(step_counts['2015-04-01'])

print(20 * '-' + " Forma De O Dado Pelo índice Do Array " + 10 * "-")
#   Podemos também chamar esses dados na forma de um array, tomando o índice de exemplo como i = 3
print(step_counts[3])

print(20 * '-' + " Forma De Selecionar todos Os Dados Do Mês Desejado " + 10 * "-")
#   Selecionando Todos Os Dados Do Mês Desejado
print(step_counts['2015-04'])

print(20 * '-' + " Forma De Ver O Tipo De Dado Desejado " + 10 * "-")
#   Vendo O Tipo De Dado Desejado
print(step_counts.dtypes)

print(20 * '-' + " Exemplo De Conversão De Dado " + 10 * "-")
#   Convertendo Um Dado Para float
step_counts = step_counts.astype( float )
print( step_counts.dtypes )

print(20 * '-' + " Exemplo De Como Dados Inválidos Podem Ser Apagados E Substituidos Por Dados Válidos " + 10 * "-")
#   Criando Dado Inválido Para Exemplo
#   np é usado como um exemplo de ponto numérico qualquer
#   step_counts[1:3] = np.NaN
#   Alterado os Dados Do Registro Com Zeros
step_counts = step_counts.fillna(0.)

#   De Forma Equivalente, Temos, a seguinte forma :
#   step_counts.fillna(0., inplace=True)
print(step_counts[1:3])

#   reaproveitando a distância
cycling_data = [10.7, 0, None, 2.4, 15.3, 10.9, 0, None]

#   Cria uma tupla das datas
joined_data = list(zip(step_data,cycling_data))

print(20 * '-' + " Exemplo De Como Ver O Fluxo De Atividade De Dados Que Entraram No Dataframe" + 10 * "-")
#   Usando o Dataframe
activity_df = pd.DataFrame(joined_data)
print ( activity_df )

print(20 * '-' + " Exemplo De Como reaproveitar dados do data frame" + 10 * "-")
#   Adiciona coluna names para o dataframe
activity_df= pd.DataFrame(joined_data,index=pd.date_range('20150329',periods=6),columns=['Walking','Cycling'])
print ( activity_df )

print(20 * '-' + " Exemplo De selecionar linhas no programa pelo index" + 10 * "-")
#   Seleciona linhas dos dados pelo nome dos index
print( activity_df.loc['2015-04-01'] )

print(20 * '-' + " Exemplo De selecionar linhas no programa pelas posições inteiras  " + 10 * "-")
#   Seleciona linhas dos dados pelas posições inteiras
print ( activity_df.iloc[-3] )

print(20 * '-' + " Exemplo de printar dados pelo nome da coluna" + 10 * "-")
#   Nome da coluna
print ( activity_df['Walking'] )

print(20 * '-' + " Exemplo de print por orientação de objetos " + 10 * "-")
#   Exemplo por orientação de objetos
print ( activity_df.Walking )

print(20 * '-' + " Exemplo de print pelos dados das colunas " + 10 * "-")
#   Print dos dados da primeira coluna
print ( activity_df.iloc[:,0] )

print(20 * '-' + " Exemplo de print pegando arquivos " + 10 * "-")
#   Achando o local onde há o arquivo
filepath = "C:/Users/gabri/OneDrive/Documentos/Projetos de Programação/Machine Learning - Curso Intel/Aula 1/Intel-ML101_Class1/data/Iris_Data.csv"

#   Exemplo de como importar data para pode usar algum arquivo
pwd = os.getcwd()
os.chdir ( os.path.dirname ( filepath ) )

data = pd.read_csv( os.path.basename ( filepath ) ) # resolver como achar o caminho

#   Printando colunas até a quinta coluna
print ( data.iloc[:5] )

print(20 * '-' + " Exemplo De Como Criar Uma Nova Coluna ( Neste Caso Chamada De Sepal_Area ) " + 10 * "-")
#   Criando uma nova coluna que é um produto dos dois produtos mensurávies
data['sepal_area'] = data.sepal_length *data.sepal_width
# Printando algumas colunas
print ( data.iloc[:5, -3:] ) # 5 -> até linha 4, começa do zero || nova coluna 3 ( negativo para indicar que é a nova coluna )

print(20 * '-' + " Exemplo de print Usando A Função Lambda Para Criar Novas Colunas " + 10 * "-")
#   A função lambda pode ser apicada
#   aos dados que se segue em cada linha da coluna
#   Neste caso, iremos criar uma nova coluna onde será a abreviação depois de Iris
data['abbrev'] = (data
.species
.apply(lambda x: x.replace('Iris-',''))) # O primeiro termo será o que ele ignorará para criar a nova tabela || Já o depois da vírgula será o que irá adicionar ao lugar do termo ignorado
#     Note que há outras maneiras de fazer
#   a mesma coisa da tarefa de cima
print ( data.iloc[:5, -3:] ) # Printando novamente os dados até a quinta linha e printando a terceira coluna

print(20 * '-' + " Exemplo De Concatenar As Linhas " + 10 * "-")
#   Podemos concatenar as linhas também
#   Vamos pegar como exemplo as últimas duas linhas
small_data = pd.concat([data.iloc[:2],
data.iloc[-2:]])
print(small_data.iloc[:,-3:])
#   Perceba o método join do tipo
#   SQL para junção do dataframe

print(20 * '-' + " Exemplo Em Que Ve A Quantidade Total Que Aparace Cada Espécie " + 10 * "-")
#  Recomenda - se que se use um dataframe para contas
#  Para uso de séries, use a função .value_counts
group_sizes = (data.groupby('species').size())
print(group_sizes) # método calculado para cada linha da tabela

print(20 * '-' + " Exemplo Cálculo Da Média " + 10 * "-")
#  Calculo da média no Dataframe
print ( data.mean ( ) ) # método calculado para cada linha da tabela

print(20 * '-' + " Exemplo Cálculo Da Mediana " + 10 * "-")
#  Cálculo da mediana em série
print(data.petal_length.median())

print(20 * '-' + " Exemplo Cálculo Da Moda " + 10 * "-")
#  Cálculo da moda na série
print(data.petal_length.mode())

print(20 * '-' + " Exemplo De Cálculo De Algumas Funções Estatísticas " + 10 * "-")
# Calculo Do Desvio padrão, variança padrão e erro da média, respectivamente
print( "\nDesvio Padrão : {}".format( data.petal_length.std ( ) ) )
print( "\nVarianaça Padrão : {}".format( data.petal_length.var ( ) ) )
print( "\nErro Da Média : {}".format ( data.petal_length.sem() ) )

print(20 * '-' + " Exemplo De Print Dos Dados Quantitativos " + 10 * "-")
# Podemos Ver Também De Forma Quantitativa
print(data.quantile(0))

print(20 * '-' + "Descrevendo Todos Os Dados Da Tabela " + 10 * "-")
print(data.describe())

print(20 * '-' + "Descrevendo Dados Aleatórios Da Tabela " + 10 * "-")
# Exemplo Que Pegamos 5 Colunas Aleatórias
sample = (data
.sample(n=5,
replace=False,
random_state=42))
print(sample.iloc[:,-3:])

#   Exemplo De Print De Um Gráfico Normal
plt.plot(data.sepal_length, data.sepal_width,ls ='', marker='o')
plt.show()

#   Exemplo De Como Juntar Dois Ou Mais Gráficos De Uma Vez
plt.plot(data.sepal_length, data.sepal_width,ls ='', marker='o', label='sepal')
plt.plot(data.petal_length, data.petal_width,ls ='', marker='o', label='petal')
plt.legend()
plt.show()