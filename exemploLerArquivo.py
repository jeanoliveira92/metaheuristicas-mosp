# ARQUIVO DE ENTRADA
#filename = input("Digite o nome do arquivo de entrada: ")
file = open("teste.txt","r")
#file = open(filename,"r")

# DISCRIMINANTE PARA O ARQUIVO DE SAÍDA
count = 0

for line in file:
    val = line.split()

    if(len(val) > 0 and val[0] != ""):
        if(len(val) == 2):
            count += 1
            fout = open("teste_{num}.txt".format(num = count),"w")
            #fout.write("{val1}{val2}\n".format(val1=val[0], val2=val[1]))
            for values in val:
                fout.write(values + " ")

            fout.write("\n")

            #print("TItulo")
        else:
            txt = ""
            for i in range(len(val)):
                txt += val[i] + " "

            fout.write(txt + "\n")
    else:
        fout.close()
        #print ("espaço!")

file.close()

