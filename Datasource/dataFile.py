
import numpy as np
import os

'RETORNA O CABEÇALHO E A MATRIZ DE VALROES'
def dataReadMatrix(name, id):
    fileName = "Datasource\\Datasets\\" + name + id + ".txt"

    with open(fileName, 'rb') as file:
        container = [float(field) for field in file.readline().split()]
        container.pop(0)

        'data = [ [ float(j) for j in i.split() ] for i in file]'
        if(name == "rect"):
            data = [[float(j)*100 for j in i.split()] for i in file]
        if(name == "square"):
            data = [[float(i)*100, float(i)*100] for i in file]

        return container, data

' REALIZA A ESCRITA DOS ARQUIVOS EM ARQUIVO - NADA AINDA IMPLEMENTADO'
def dataWrite(nome, id, container, data):
    filename = 'Datasource\\' + nome + id +'_altered.txt'
    file = open(filename, 'a+')

    [file.writelines(str("%.2f" %i)) for i in container]
    file.writelines("\n")

    [[[file.writelines(str("%.2f" %j) + ";") for j in i],file.writelines("\n")] for i in data]

    print('\nWrited!!!\n')
    print(os.path.abspath(os.curdir) + "/" + filename)
    file.close()

    'IMPRIME OS VALORES MODIFICADOS'
    print("\nRaio dos containers: ", end = '')
    [ print(str(float(i))+ ' ', end = '') for i in container]
    print("\n")

    [ print( str("%.2f " %i[0]) + str("%.2f " %i[1]) ) for i in data]