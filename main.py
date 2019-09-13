# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEUR�STICAS PARA PROBLEMAS DE OTIMIZA��O
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT N�COLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import sys
from Datasource import dataFile as dt
from HeuristicaConstrutiva import heuristicaConstrutiva as hc

runType = 0

#VERIFICA SE H� ARGUMENTOS EXTERNOS
if __name__ == "__main__":
    if len(sys.argv) == 1:
        runType = 1

# MODO ARGUMENTO
if runType == 0:
    filename    = sys.argv[1]

    #REALIZA A LEITURA DO ARQUIVO
    container, data = dt.dataReadMatrix( filename )

    dt.dataWrite(filename + "fromArgv", container, data)

# MODO MANUAL
elif runType == 1:
    #LOOPING INFINITO AT� QUE O USU�RIO SELECIONE PARA SAIR
    while(1):
        #MENU INFORMATIVO
        select = input("\n\n#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n\n"
                      "Selecione:\n\t"
                      "1: Ler um arquivo\n\t"
                      "2: Escrever um arquivo\n\t"
                      "3: Imprimir um arquivo\n\t"
                      "4: Heur�stica Construtiva\n\t"
                      "0: Sair\n>>>: ")

        # CASE 0: ENCERRA O PROGRAMA
        if select == '0':
            exit()

        # CASE 1: LEITURA DO DATASET'
        elif select == "1":
            try:
                #'filename = input("Qual nome do dataset: ")
                filename = "scoop-A_AP-9.d_3"
                #'REALIZA A LEITURA DO ARQUIVO'
                container, data = dt.dataRead(filename)
            except:
                input("Erro ao carregar os dados. Aperte enter para continuar...")

        # ENTRA APENAS SE OS DADOS ESTIVEREM CARREGADOS NA MEM�RIA
        else:
            try:
                if len(data) >= 0:
                    if select == "2":
                        dt.dataWrite(filename, container, data)

                    elif select == "3":
                        dt.printMatriz(filename, container, data)

                    elif select == "4":
                        hc.heuristicaConstrutivaEmbaralhar(container, data)

            except:
                    input("\nOp��o inv�lida. Dados ainda n�o carregados. Aperte enter para continuar...")

print("Encerrando...")