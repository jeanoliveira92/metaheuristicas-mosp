
''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

from Datasource import dataFile
'from Algorithms import BinPacking'

fileType = {'square', 'rect'}
fileNumber = {3,3}

container, data = dataFile.dataReadMatrix("square", "1")

print(data)
print(container)

'bins = BinPacking.BinPacking(data, container)'
'print(bins)'