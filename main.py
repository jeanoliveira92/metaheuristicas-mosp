
''' DISCIPLINA: COM936 - METAHEURÍSTICAS PARA PROBLEMAS DE OTIMIZAÇÃO
    PROFESSOR:  RAFAEL DE MAGALHAES DIAS FRINHANI
    ALUNOS:     JEAN CARLOS DE OLIVEIRA     35138
                ROBERT NÍCOLAS MENDES       2018012810
                VICTOR PEREIRA MOREIRA      2016012632
    TEMA:       CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE)'''

import sys
from Datasource import dataFile as dt
from HeuristicaConstrutiva import heuristicaConstrutiva as hc

'APENAS PARA ORGANIZAÇÂO'
fileType = {0:"square", 1:"rect"}

'''
    Essa variável define como o codigo vai rodar.
    Se ela permanecer em 0, vai quer dizer que o comando veio externo e vai rodar automaticamente
    Se ela mudar para 1, vai exibir um menu e continuar em loop ate encerrar
'''
runType = 0

'CHAMADA EXTERNA - RECEBENDO OS ARGUMENTOS ENVIADOS VIA TERMINAL'
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Sem dados de entrada. Saindo....\nAbrindo o menu para seleção:")
        runType = 1

if runType == 0:
    Type    = fileType[int(sys.argv[1])]
    number  =  str(sys.argv[2])

    'REALIZA A LEITURA DO ARQUIVO'
    container, data = dt.dataReadMatrix( Type, number )

    'REALIZA A ESCRITA DO ARQUIVO MODIFICADO'
    dt.dataWrite(Type + "fromArgv", number, container, data)

elif runType == 1:
    print("#### CUTTING STOCK (PROBLEMA DE CORTE DE ESTOQUE) ####\n")

    'LOOPING INFINITO ATÉ QUE O USUÁRIO SELECIONE PARA SAIR'
    while(1):
        'MENU INFORMATIVO'
        print("\nSelecione:\n\t1: Ler um arquivo\n\t2: Alterar um arquivo\n\t3: Escrever um arquivo\n\t4: Imprimir um arquivo\n\t5: Heurística Construtiva\n\t0: Saída")
        select = input(">>>: ")

        'FECHAR CASO RECEBA 0'
        if select == '0':
            exit()

        'CASE PARA LEITURA'
        if select == "1":
            try:
                # COMENTADO TEMPORARIAMENTE
                #name = input("\nDigite 0 para Quadrado ou 1 para Retangulo: ")
                #name = fileType[int(name)]

                #id = input("Qual o número do dataset: ")

                'REALIZA A LEITURA DO ARQUIVO'
                container, data = dt.dataReadMatrix('square', '1')

            except:
                print("Dataset inválido....")

        'VALIDA SE JA FOI REALIZADAA LEITURA'
        try:
            if len(data) >= 0:
                'ALTERAR OS DADOS'
                if select == "2":
                    try:
                        value = input("\nDigite um valor a multiplicar os itens do arquivo: ")
                        data = dt.alterMatriz(float(value), data)
                    except:
                        print("\nMultiplicação inválida. Talvez tenha escrito uma letra.")

                'REALIZA A ESCRITA EM ARQUIVO DO ARQUIVO MODIFICADO'
                if select == "3":
                    dt.dataWrite(Type, number, container, data)

                'REALIZA A IMPRESSÃO DO ARQUIVO MODIFICADO'
                if select == "4":
                    dt.printMatriz('Raio dos containers: ', container, data)

                if select == "5":
                    hc.heuristicaConstrutiva(data, container)
                    #break
            else:
                print("\nDados ainda não carregados\n")

        except:
                print("\nOpção inválida. Dados ainda não carregados\n")



print("Encerrado...")