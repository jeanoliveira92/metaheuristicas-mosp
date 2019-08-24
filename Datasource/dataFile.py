
import os
from Model import geometricForm as gf
from Model import geometricCircle as gc

'RETORNA O CABEÇALHO E A MATRIZ DE VALROES'
def dataReadMatrix(name, id):
    fileName = "Datasource\\Datasets\\" + name + id + ".txt"

    try:
        with open(fileName, 'rb') as file:
            container = [gc.geometricCircle(radius= float(i)) for i in file.readline().split()]
            container.pop(0)

            if(name == "square"):
                data = [gf.geometricForm(x=float(i), y=float(i)) for i in file]

            if (name == "rect"):
                data = [ gf.geometricForm(x=float(i.split()[0]), y=float(i.split()[1])) for i in file]
    except:
        print("\nArquivo inválido!\n")

    return container, data

' REALIZA A ESCRITA DOS ARQUIVOS EM ARQUIVO - NADA AINDA IMPLEMENTADO'
def dataWrite(nome, id, container, data):
    filename = 'Datasource\\' + nome + id +'_altered.txt'
    'file = open(filename, "a+")'
    file = open(filename, 'w')

    'GRAVA OS VALORES DO CONTAINER'
    [file.writelines(str("%.2f" %i.getRadius()) + ";") for i in container]
    file.writelines("\n")

    'GRAVA OS VALORES DAS PEÇAS, SEJA ELA UM RETANGULO OU UM QUADRADO'
    [file.writelines(str("%.2f" %i.getX()) + ";" + str("%.2f" %i.getY()) + "\n") for i in data]

    'IMPRIME UMA MENSAGEM E O LOCAL ONDE FOI SALVO O ARQUIVO'
    print('\nArquivo salvo!')
    print(os.path.abspath(os.curdir) + "/" + filename+"\n")
    file.close()

' REALIZA A IMPRESSÃO DOS DADOS NA TELA '
def printMatriz(title, container, data):
    'IMPRIME O TÍTULO'
    print("\n" + title, end = '')

    'IMPRIME OS CONTAINERS'
    'PARA CADA I EM CONTAINER, ELE FAZ UM CAST PARA FLOAT E DEPOIS PARA STRING'
    [ print(str(float(i.radius))+ ' ', end = '') for i in container]
    print("\n")

    'IMPRIME OS DADOS'
    'PARA CARA I EM DATA FAZ UM CAST PARA STRING COM 2 CASAS DECIMAIS DO TIPO FLOAT'
    'ESTE É O NOVO FORMATO DE DADOS. TODOS OS QUADRADOS E RETANGULOS POSSUEM ALTURA E LARGURA'
    [ print( str("%.2f " %i.x + str("%.2f " %i.y) )) for i in data]

def alterMatriz(alter, data):
    [ [i.setX( (i.getX() * alter) ), i.setY( (i.getY() * alter) )]  for i in data]

    return data
