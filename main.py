# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import time
from Datasource import dataFile as dt
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hr


print("\n#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n")

def main(FILENAME):
    try:
        dt.dataRead(FILENAME)

        # ------------------------- MÉTODO CONSTRUTIVO ---------------------------------------#
        #---------------------------- RandonShuffle ------------------------------------------#

        print("\nRandonShuffle - Método Construtivo\n")
        # METODO CONSTRUTIVO
        timeCounter                    = time.time()                         #INICIA O CONTADOR
        ordemPilhas, quantidadePilhas  = hc.RandonShuffle()
        timeCounter                    = time.time() - timeCounter          #ENCERRA O CONTADOR

        #IMPRESSÃO DO MODO CONSTRUTIVO
        print("Ordem das pilhas:")
        print(ordemPilhas)
        print("Quantidade de pilhas abertas")
        print(quantidadePilhas)
        print('\n[INFO]: O tempo total de execução foi}')
        print(timeCounter)

        # ---------------------------- MÉTODO DE REFINAMENTO --------------------------------------#
        #---------------------------- FirstImprovementMethod --------------------------------------#

        print("\nFirstImprovementMethod - Método de Refinamento\n")
        #METODO REFINAMENTO
        timeCounter = time.time()
        FirstImprovementMethodOrdemPilhas, FirstImprovementMethodQtdPilhas = hr.FirstImprovementMethod(quantidadePilhas, ordemPilhas)
        timeCounter = time.time() - timeCounter

        #IMPRESSÃO DO MODO REFINAMENTO
        print("Ordem das pilhas:")
        print(FirstImprovementMethodOrdemPilhas)
        print("Quantidade de pilhas abertas")
        print(FirstImprovementMethodQtdPilhas)
        print('\n[INFO]: O tempo total de execução foi}')
        print(timeCounter)

        #---------------------------- RandonUpHillMethod --------------------------------------#

        print("\nRandonUpHillMethod - Método de Refinamento\n")

        timeCounter = time.time()
        UpHillMethodOrdemPilhas, UpHillMethodQtdPilhas = hr.RandonUpHillMethod(quantidadePilhas, 100)
        timeCounter = time.time() - timeCounter

        #IMPRESSÃO DO MODO REFINAMENTO
        print("Ordem das pilhas:")
        print(UpHillMethodOrdemPilhas)
        print("Quantidade de pilhas abertas")
        print(UpHillMethodQtdPilhas)
        print('\n[INFO]: O tempo total de execução foi}')
        print(timeCounter)

    except ValueError as err:
        raise("\n[ERROR]: Opção inválida. Dados ainda não carregados ..." + err)