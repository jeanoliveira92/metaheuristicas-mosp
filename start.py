# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:
          CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''
import sys
import main
import globals as g
import random

#PARAMETROS DE ARGUMENTO
#RECEBE O NOME DO ARQUIVO A SER ABERTO, SENAO, SOLICITA UM

if __name__ == "__main__":
    if len(sys.argv) > 1:
        FILENAME = sys.argv[0]
        QTD = sys.argv[1]
        random.seed = int(sys.argv[2]) #INICIALIZA O SEED


    # MODO MANUAL
    else:
        FILENAME    = input("[INFO]: Qual nome do dataset: ")
        QTD         = int(input("[INFO]: Quantas vezes irá rodar: "))
        random.seed = int(input("[INFO]: Qual é o valor da seed: ")) #INICIALIZA O SEED
        SELECT      = input("[INFO]: Selecione:\n\t0 Para Heuristica Construtiva"+
                                              "\n\t1 Para Heuristica de Refinamento - First Improvement Method" +
                                              "\n\t2 Para Heuristica de Refinamento - Randon UpHill Method" +
                                              "\n\t3 Para Metaheuristica - IteratedLocalSearch\n[INFO]: ")

        #FILENAME = 'scoop-A_AP-9.d_3'
        #QTD = 1
        #random.seed = 1992
        #SELECT = 3


try:
    counter = 0
    while(counter <= int(QTD)):
        main.main(FILENAME, SELECT)
        counter += 1

except ValueError as err:
    print("\n[ERROR]: Opção inválida. Dados ainda não carregados ... \n[ERROR] " + str(err))

print("[INFO]: Encerrando.. .")