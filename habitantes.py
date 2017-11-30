#Receber a sigla de um estado (input)
#Somar os habitantes do município desse estado
#Mostrar o total de habitantes do estado

import csv
estado = input("Digite o estado que deseja saber o número total de habitantes: \n")
estado = estado.upper()
pop_estado = 0
arquivo = open('brasil.csv', encoding='utf8')
for registro in csv.reader(arquivo):
    municipio = registro[0]
    if municipio == estado:
        habitantes = registro[2]
        pop_estado += (int(habitantes))
print('O número de habitantes no estado '+(estado)+ ' é: ' + str(pop_estado))
