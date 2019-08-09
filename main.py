
''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

from Datasource import dataFile as dt
'from Algorithms import BinPacking'

fileType = {0:"square", 1:"rect"}
fileNumber = {0:"3",1:"3"}

container, data = dt.dataReadMatrix( fileType[1], str(fileNumber[0]) )

print(data)
print(container)

dt.dataWrite(fileType[1], str(fileNumber[0]), container, data)