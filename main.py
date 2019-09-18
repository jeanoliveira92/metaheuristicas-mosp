# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEUR�STICAS PARA PROBLEMAS DE OTIMIZA��O
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT N�COLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import time
from Datasource import dataFile as df
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hr

print("\n#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n")

def main(FILENAME):
    try:
        df.dataRead(FILENAME)

        # ------------------------- M�TODO CONSTRUTIVO ---------------------------------------#
        #---------------------------- RandonShuffle ------------------------------------------#

        print("\nRandonShuffle - M�todo Construtivo\n")
        # METODO CONSTRUTIVO
        timeCounter                                   = time.time()                        #INICIA O CONTADOR
        ordemPilhas, PilhasAbertas, qtdPilhasAbertas  = hc.RandonShuffle()
        timeCounter                                   = time.time() - timeCounter          #ENCERRA O CONTADOR

        #IMPRESS�O DO MODO CONSTRUTIVO
        print("Ordem das pilhas:")
        print(ordemPilhas)
        print("Quantidade de pilhas abertas")
        print(qtdPilhasAbertas)
        print('\n[INFO]: O tempo total de execu��o foi}')
        print(timeCounter)

        df.dataWrite(FILENAME, 'RandonShuffle', timeCounter, PilhasAbertas, qtdPilhasAbertas)

        # ---------------------------- M�TODO DE REFINAMENTO --------------------------------------#
        #---------------------------- FirstImprovementMethod --------------------------------------#

        print("\nFirstImprovementMethod - M�todo de Refinamento\n")
        #METODO REFINAMENTO
        timeCounter = time.time()
        FirstImprovementMethodOrdemPilhas, FirstImprovementMethodPilhasAbertas, FirstImprovementMethodQtdPilhas = hr.FirstImprovementMethod(qtdPilhasAbertas, ordemPilhas)
        timeCounter = time.time() - timeCounter

        #IMPRESS�O DO MODO REFINAMENTO
        print("Ordem das pilhas:")
        print(FirstImprovementMethodOrdemPilhas)
        print("Quantidade de pilhas abertas")
        print(FirstImprovementMethodQtdPilhas)
        print('\n[INFO]: O tempo total de execu��o foi}')
        print(timeCounter)

        df.dataWrite(FILENAME, 'FirstImprovementMethod', timeCounter, FirstImprovementMethodPilhasAbertas, FirstImprovementMethodQtdPilhas)

        #---------------------------- RandonUpHillMethod --------------------------------------#

        print("\nRandonUpHillMethod - M�todo de Refinamento\n")

        timeCounter = time.time()
        UpHillMethodOrdemPilhas, UpHillMethodPilhasAbertas, UpHillMethodQtdPilhas = hr.RandonUpHillMethod(qtdPilhasAbertas, 100)
        timeCounter = time.time() - timeCounter

        #IMPRESS�O DO MODO REFINAMENTO
        print("Ordem das pilhas:")
        print(UpHillMethodOrdemPilhas)
        print("Quantidade de pilhas abertas")
        print(UpHillMethodQtdPilhas)
        print('\n[INFO]: O tempo total de execu��o foi')
        print(timeCounter)

        df.dataWrite(FILENAME, 'UpHillMethodOrdemPilhas', timeCounter, UpHillMethodPilhasAbertas, UpHillMethodQtdPilhas)

    except ValueError as err:
        raise("\n[ERROR]: Op��o inv�lida. Dados ainda n�o carregados ..." + err)