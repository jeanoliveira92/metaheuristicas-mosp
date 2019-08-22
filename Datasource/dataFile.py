
import numpy as np
import os

'RETORNA O CABEÇALHO E A MATRIZ DE VALROES'
def dataReadMatrix(name, id):
    fileName = "Datasource\\Datasets\\" + name + id + ".txt"

    try:
        with open(fileName, 'rb') as file:
            container = [float(field) for field in file.readline().split()]
            container.pop(0)

            if(name == "rect"):
                data = [[float(j) for j in i.split()] for i in file]
            if(name == "square"):
                data = [[float(i), float(i)] for i in file]
    except:
        print("\nArquivo inválido!\n")
        return [0,0]

    return container, data

' REALIZA A ESCRITA DOS ARQUIVOS EM ARQUIVO - NADA AINDA IMPLEMENTADO'
def dataWrite(nome, id, container, data):
    filename = 'Datasource\\' + nome + id +'_altered.txt'
    'file = open(filename, "a+")'
    file = open(filename, 'w')

    'GRAVA OS VALORES DO CONTAINER'
    [file.writelines(str("%.2f" %i) + ";") for i in container]
    file.writelines("\n")

    'GRAVA OS VALORES DAS PEÇAS, SEJA ELA UM RETANGULO OU UM QUADRADO'
    [[[file.writelines(str("%.2f" %j) + ";") for j in i],file.writelines("\n")] for i in data]

    'IMPRIME UMA MENSAGEM E O LOCAL ONDE FOI SALVO O ARQUIVO'
    print('\nArquivo salvo!')
    print(os.path.abspath(os.curdir) + "/" + filename+"\n")
    file.close()

' REALIZA A IMPRESSÃO DOS DADOS NA TELA '
def printMatriz(title, container, data):
    'IMPRIME O TÍTULO'
    print("\n" + title, end = '')

    'IMPRIME OS CONTAINERS'
    'PARA CADA I EM CONTAINER, ELE FAZ UM CAST PARA FLOAT E DEPOIS PARA STRING'
    [ print(str(float(i))+ ' ', end = '') for i in container]
    print("\n")

    'IMPRIME OS DADOS'
    'PARA CARA I EM DATA FAZ UM CAST PARA STRING COM 2 CASAS DECIMAIS DO TIPO FLOAT'
    'ESTE É O NOVO FORMATO DE DADOS. TODOS OS QUADRADOS E RETANGULOS POSSUEM ALTURA E LARGURA'
    [ print( str("%.2f " %i[0]) + str("%.2f " %i[1]) ) for i in data]
    print("\n")

def alterMatriz(alter, data):
    return [[j*alter for j in i] for i in data]
