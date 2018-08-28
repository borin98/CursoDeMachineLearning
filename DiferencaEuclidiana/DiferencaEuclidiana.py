from math import sqrt

def distanciaEuclidiana ( v1, v2, tam ) :

    vetorResultado = []
    soma = 0

    for i in range ( tam ) :

        vetorResultado.insert ( i, ( v1[i] - v2[i] ) )

    for i in range ( tam ) :

        soma += vetorResultado[i]*vetorResultado[i]

    print("A distância é : {}".format ( sqrt ( soma ) ) )


def montaVetor ( v, tam ) :

    for i in range(tam):

        componenteV = (float)(input("Digite o valor do elemento {} : ".format(i + 1)))
        v.insert(i, componenteV)

def main (  ) :

    tam = (int)(input("Digite o tamamho do vetor : "))

    v1 = []
    v2 = []

    while (tam <= 0):

        print("Valor inválido !!!")
        tam = (int)(input("Digite o tamamho do vetor : "))

    print("------ Vetor V1 ------\n")
    montaVetor ( v1, tam )
    print("------ Vetor V2 ------\n")
    montaVetor ( v2, tam )
    distanciaEuclidiana ( v1, v2, tam )

main (  )