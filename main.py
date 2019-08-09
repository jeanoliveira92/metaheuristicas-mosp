
''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import sys
from Datasource import dataFile as dt

'APENAS PARA ORGANIZAÇÂO'
fileType = {0:"square", 1:"rect"}

'CHAMADA EXTERNA'
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Sem dados de entrada. Saindo....")
        exit(1)
    Type    = fileType[int(sys.argv[1])]
    number  =  str(sys.argv[2])

'REALIZA A LEITURA DO ARQUIVO'
container, data = dt.dataReadMatrix( Type, number )

'REALIZA A ESCRITA DO ARQUIVO MODIFICADO'
dt.dataWrite(Type, number, container, data)