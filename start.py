# -*- coding: cp1252 -*-

''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       PROBLEMA DE MINIMIZAÇÃO DE PILHAS ABERTAS'''

import sys, main, random

# PARAMETROS DE ARGUMENTO
if __name__ == "__main__":
    '''
    if len(sys.argv) > 1:
        FILENAME     = sys.argv[0]      # NOME DO ARQUIVO
        QTDITERACOES = int(sys.argv[1]) # QUANTIDADE DE VEZES QUE IRÁ EXECUTAR O METODO
        SEEDVALUE    = int(sys.argv[2]) # INICIALIZA O SEED
        SELECT       = int(sys.argv[3]) # ALGORITMO

    # MODO MANUAL
    else:
        FILENAME     = input("[INFO]: Qual nome do dataset: ")
        QTDITERACOES = int(input("[INFO]: Quantas vezes irá rodar: "))
        SEEDVALUE    = int(input("[INFO]: Qual é o valor da seed: "))
        SELECT       = int(input("[INFO]: Selecione:"
                           "\n\t0 Heuristica Construtiva"+
                           "\n\t1 Heuristica de Refinamento - First Improvement Method" +
                           "\n\t2 Heuristica de Refinamento - Randon UpHill Method" +
                           "\n\t3 Metaheuristica - Iterated Local Search - First Improvement Method"+
                           "\n\t4 Metaheuristica - Iterated Local Search - Randon UpHill Method" +
                           "\n\t5 Metaheuristica - Grasp - First Improvement Method: " +
                           "\n\t6 Metaheuristica - Grasp - Randon UpHill Method" +
                           "\n\t7 Metaheuristica - Grasp - PathRelinkForward" +
                           "\n\t8 Metaheuristica - Grasp - PathRelinkBackward" +
                           "\n\t9 Metaheuristica - Grasp - PathRelinkMixed:\n" +
                            "[INFO]:"))
    '''

try:
    FILENAME = 'scoop-A_AP-9.d_3'
    QTDITERACOES = 30
    SEEDVALUE = 1
    SELECT = 5

    random.seed(SEEDVALUE) #INICIALIZA O SEED

    for counter in range(QTDITERACOES):
        print("[INFO]: Rodada " + str(counter))
        main.main(FILENAME, SELECT)

except ValueError as err:
    print("\n[ERROR] " + str(err))

print("\n[INFO]: Execuração encerrada.")