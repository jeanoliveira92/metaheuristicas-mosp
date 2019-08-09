
import numpy as np

'RETORNA O CABEÇALHO E A MATRIZ DE VALROES'
def dataReadMatrix(name, id):
    fileName = "Datasource/rectsandsquares/" + name + id + ".txt"

    with open(fileName, 'rb') as file:
        container = [float(field) for field in file.readline().split()]

        container.pop(0)

        'data = [ [ float(j) for j in i.split() ] for i in file]'
        data = [[float(j)*100 for j in i.split()] for i in file]

        return container, data

' REALIZA A ESCRITA DOS ARQUIVOS EM ARQUIVO - NADA AINDA IMPLEMENTADO'
def dataWrite(nome, id, container, data):
    file = open('Datasource/' + nome + id +'_altered.txt', 'a+')
    [file.writelines(str("%.2f" %i)) for i in container]
    file.writelines("\n")
    [[[file.writelines(str("%.2f" %j) + ";") for j in i],file.writelines("\n")] for i in data]
    file.close()
    print('Write')