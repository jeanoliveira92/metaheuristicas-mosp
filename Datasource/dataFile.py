import os
import numpy as np

# ---------- RETORNA O CABEÇALHO E A MATRIZ DE VALROES  ----------------------------------------------------------------
def dataRead(filename):
    fileName = "Datasource/Datasets/" + filename + ".txt"
    try:
        with open(fileName, 'rb') as file:
            nrows, ncols = [ int(n) for n in file.readline().split() ]
            data = np.genfromtxt(file, dtype="uint32", max_rows=nrows)
    except:
        raise ValueError("\n[ERROR]: Arquivo inválido ou inexistente. Aperte enter para continuar ...")

    return nrows, ncols, data

# ----------- REALIZA A ESCRITA DOS DADOS EM ARQUIVO -------------------------------------------------------------------
def dataWrite(filename, container, data):
    filename = 'Datasource\\' + filename + '_altered.csv'
    #file = open(filename, "a+")
    file = open(filename, 'w')

    #GRAVA OS VALORES DO CABEÇALHO
    file.writelines(str(container[0]) + ";" + str(container[1]) + "\n")

    #GRAVA OS DADOS. TEMP FICTICIO PARA NÃO APRESENTAR ERRO
    temp =  [
                [
                    [
                        [
                            file.writelines( str(j) + ";")
                        ] for j in i.values() ], file.writelines("\n")
                ] for i in data.values()
            ]

    'IMPRIME UMA MENSAGEM E O LOCAL ONDE FOI SALVO O ARQUIVO'
    print('\nArquivo salvo!')
    print(os.path.abspath(os.curdir) + "/" + filename+"\n")
    file.close()

# ----------- REALIZA A IMPRESSÃO DOS DADOS NA TELA --------------------------------------------------------------------
def printMatriz(filename, container, data):
    #IMPRIME O TÍTULO
    print("\n Dataset: " + filename + "\n")

    #IMPRIME O CABEÇALHO
    print("NÚMERO DE PADROES: " + str(container[0]) + "\n"
          "NÚMERO DE PEÇAS: " + str(container[1]) + "\n")

    #IMPRiME OS DADOS. O RETORNO É FICTICIO APENAS PARA NÃO APRESENTAR ERRO.
    return [
                [
                    print(i)
                ] for i in data.values()
            ]