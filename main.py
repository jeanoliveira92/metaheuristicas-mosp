# -*- coding: cp1252 -*-
import time
from Datasource import dataFile as df
from HeuristicaConstrutiva import heuristicaConstrutiva as hc
from HeuristicaRefinamento import heuristicaRefinamento as hr
from ILS import ils as interator


def main(FILENAME, SELECT):
    print("\n#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n")
    try:
        df.dataRead(FILENAME)

        # ------------------------- MÉTODO CONSTRUTIVO ---------------------------------------#
        #---------------------------- RandonShuffle ------------------------------------------#

        print("\nRandonShuffle - Método Construtivo\n")
        # METODO CONSTRUTIVO
        timeCounter                                   = time.time()                        #INICIA O CONTADOR
        ordemPilhas, PilhasAbertas, qtdPilhasAbertas  = hc.RandonShuffle()
        timeCounter                                   = time.time() - timeCounter          #ENCERRA O CONTADOR

        #IMPRESSÃO DO MODO CONSTRUTIVO
        print("Ordem das pilhas:")
        print(ordemPilhas)
        print("Quantidade de pilhas abertas")
        print(qtdPilhasAbertas)
        print('\n[INFO]: O tempo total de execução foi}')
        print(timeCounter)

        df.dataWrite(FILENAME, 'RandonShuffle', timeCounter, PilhasAbertas, qtdPilhasAbertas)

        # ---------------------------- FirstImprovementMethod --------------------------------------#
        if(SELECT == 1):
            print("\nFirstImprovementMethod - Método de Refinamento\n")
            # METODO REFINAMENTO
            timeCounter = time.time()
            FirstImprovementMethodOrdemPilhas, FirstImprovementMethodPilhasAbertas, FirstImprovementMethodQtdPilhas = hr.FirstImprovementMethod(qtdPilhasAbertas, ordemPilhas)
            timeCounter = time.time() - timeCounter

            # IMPRESSÃO DO MODO REFINAMENTO
            print("Ordem das pilhas:")
            print(FirstImprovementMethodOrdemPilhas)
            print("Quantidade de pilhas abertas")
            print(FirstImprovementMethodQtdPilhas)
            print('\n[INFO]: O tempo total de execução foi}')
            print(timeCounter)

            df.dataWrite(FILENAME, 'FirstImprovementMethod', timeCounter, FirstImprovementMethodPilhasAbertas, FirstImprovementMethodQtdPilhas)

        # ---------------------------- RandonUpHillMethod --------------------------------------#
        elif(SELECT == 2):

            print("\nRandonUpHillMethod - Método de Refinamento\n")

            timeCounter = time.time()
            UpHillMethodOrdemPilhas, UpHillMethodPilhasAbertas, UpHillMethodQtdPilhas = hr.RandonUpHillMethod(qtdPilhasAbertas, 100)
            timeCounter = time.time() - timeCounter

            # IMPRESSÃO DO MODO REFINAMENTO
            print("Ordem das pilhas:")
            print(UpHillMethodOrdemPilhas)
            print("Quantidade de pilhas abertas")
            print(UpHillMethodQtdPilhas)
            print('\n[INFO]: O tempo total de execução foi')
            print(timeCounter)

            df.dataWrite(FILENAME, 'UpHillMethodOrdemPilhas', timeCounter, UpHillMethodPilhasAbertas, UpHillMethodQtdPilhas)
            print(UpHillMethodPilhasAbertas)
            print(UpHillMethodQtdPilhas)

        # ---------------------------- IteratedLocalSearch --------------------------------------#
        elif(SELECT == 3):
            print("[INFO] Iterated Local Search")
            timeCounter = time.time()
            ilsOrdemPilhas, isPilhasAbertas, ilsQtdPilhas = interator.IteratedLocalSearch(ordemPilhas)
            timeCounter = time.time() - timeCounter

            # IMPRESSÃO DO MODO REFINAMENTO
            print("Ordem das pilhas:")
            print(ilsOrdemPilhas)
            print("Quantidade de pilhas abertas")
            print(ilsQtdPilhas)
            print('\n[INFO]: O tempo total de execução foi')
            print(timeCounter)

            df.dataWrite(FILENAME, 'IteratedLocalSearch', timeCounter, isPilhasAbertas, ilsQtdPilhas)

    except ValueError as err:
        print("\n[ERROR]: Opção inválida. Dados ainda não carregados ...")
        raise(err)
