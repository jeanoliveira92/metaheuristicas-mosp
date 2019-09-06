import math

def heuristicaConstrutiva(dados, container):
    [ print(veriificarSeCabeWL(container[0].getRadius(), dt.getX(), dt.getY())) for dt in dados]
    print(" - ----------------------------------")
    [ print(veriificarSeCabLW(container[0].getRadius(), dt.getX(), dt.getY())) for dt in dados]




def veriificarSeCabeWL(raio, width, lenght):
    return [(-1)*(math.sqrt( ( math.pow(raio,2) - ( pow(width,2)/4)))-(lenght/2)), (math.sqrt( ( math.pow(raio,2) - ( pow(width,2)/4)))-(lenght/2))]

def veriificarSeCabLW(raio, width, lenght):
    return [(-1)*(math.sqrt( ( math.pow(raio,2) - ( pow(lenght,2)/4)))-(width/2)), (math.sqrt( ( math.pow(raio,2) - ( pow(lenght,2)/4)))-(width/2))]
