
import numpy as np

' RETORNA A MATRIZ DE VALROES '
def dataReadMatrix(name, id):
    fileName = "Datasource/rectsandsquares/" + name + id + ".txt"

    with open(fileName, 'rb') as file:
        'PEGA A PRIMEIRA LINHA DO ARQUIVO'
        container = [float(field) for field in file.readline().split()]

        'PEGA O VALOR RESPECTIVO A QUATIDADE DE ITENS DO ARQUIVO'
        nrows = container[0]

        'REMOVE A PRIMEIRA LINHA DO VETOR REFERENTE AS INFORMCÕES DO ARQUIVO'
        container.pop(0)

        'CRIA A MATRIZ DE DADOS USANDO O ARQUIVO DE DADOS'
        data = np.genfromtxt(file, dtype="float", max_rows = nrows)

    'RETORNA O CABEÇALHO E A MATRIZ DE DADOS'
    return container, data

' REALIZA A ESCRITA DOS ARQUIVOS EM ARQUIVO - NADA AINDA IMPLEMENTADO'
def dataWrite(nome, id):
    file = open('Datasource/' + nome + id +'.txt', 'a+')
    file.writelines('Resultado' + '\n')
    file.close()
    print('Write')