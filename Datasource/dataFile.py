import numpy as np
import pandas as pd
import globals as g
import os
# ---------- RETORNA O CABEÇALHO E A MATRIZ DE VALROES  ----------------------------------------------------------------
def dataRead(filename):
    fileName = "Datasource/Datasets/" + filename + ".txt"
    try:
        with open(fileName, 'rb') as file:
             #DEFININDO AS VARIAVEIS COMO DE ACESSO GLOBAL

            g.nrows, g.ncols = [ int(n) for n in file.readline().split() ]
            g.matPaPe = np.genfromtxt(file, dtype="uint32", max_rows=g.nrows)
    except:
        raise ValueError("\n[ERROR]: Arquivo inválido ou inexistente. Aperte enter para continuar ...")

# ----------- REALIZA A ESCRITA DOS DADOS EM ARQUIVO -------------------------------------------------------------------
def dataWrite(FILENAME, method, time, data, qtdPilhasAbertas):
    #GRAVA PRIMEIRO O ARQUIVO DAS MATRIZES
    filename = 'Datasource\Results\\' + FILENAME + '_' + method + '.txt'
    #file = open(filename, "a+")
    file = open(filename, "a+")
    # GERAMOS A MATRIZ RESULTADO COM A COLUNA DE PILHAS A DIREITA
    #matrixPilhas = np.c_[ df.matPaPe[ordem, :], qtdPilhasAbertas]
    matrixPilhas = np.c_[ data, qtdPilhasAbertas]
    # SALVA A MATRIZ NO ARQUIVO
    np.savetxt(file, matrixPilhas , fmt='%s')
    file.writelines(f"Tempo Total de Execução: {time:.3}ms\n\n")
    #'IMPRIME UMA MENSAGEM E O LOCAL ONDE FOI SALVO O ARQUIVO'
    file.close()

    #ESSA SEGUNDA PARTE GRAVA AS ESTATISTICAS DOS ALGORITMOS EM CSV

    filename = 'Datasource\Results\\' + FILENAME + '_' + method + '.csv'

    # CRIA O CABEÇALHO NA CRIACAO DO ARQUIVO PELA PRIMEIRA VEZ
    if os.path.isfile(os.path.abspath(os.curdir) + "/" + filename) == False:
        file = open(filename, "w+")
        file.writelines("MAIOR PILHA, TEMPO\n")
    else:
        file = open(filename, "a+")

    soma = np.max(qtdPilhasAbertas, 0)
    file.writelines(f"{soma}, {time:.3}\n")
    #'IMPRIME UMA MENSAGEM E O LOCAL ONDE FOI SALVO O ARQUIVO'
    print('\nArquivo salvo!')
    print(os.path.abspath(os.curdir) + "/" + filename)
    file.close()

    df_new = pd.read_csv(os.path.abspath(os.curdir) + "/" + filename, encoding='latin-1')
    writer = pd.ExcelWriter(os.path.abspath(os.curdir) + '/Datasource/Results/Excel/' + FILENAME + '_' + method  + '.xlsx')
    df_new.to_excel(writer, index=False)
    writer.save()

# ----------- REALIZA A IMPRESSÃO DOS DADOS NA TELA --------------------------------------------------------------------
def printMatriz(filename, container, data):
    #IMPRIME O TÍTULO
    print("\n Dataset: " + filename + "\n")

    #IMPRIME O CABEÇALHO
    print("NÚMERO DE PADROES: " + str(container[0]) + "\n"
          "NÚMERO DE PEÇAS: " + str(container[1]) + "\n")

    #IMPRiME OS DADOS. O RETORNO É FICTICIO APENAS PARA NÃO APRESENTAR ERRO.
    return [
                [ print(i) ] for i in data.values()
            ]