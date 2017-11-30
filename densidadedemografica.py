##Exercicio
#1. Receber a sigla do estado (input)
#2. Para cada municipio, calcular e mostrar a densidade demográfica
##Algoritmo
#1.Abrir arquivo csv com municipios
#2. Se o estado for o estado digitado:
#2.1. Calcula a desidade(habitantes/area)
#2.2. Mostra nome do municipio e a densidade calculada

#importa a biblioteca csv
import csv
#solicita ao usuário a sigla do Estado e converte para caixa alta
estado_desejado = input('Qual Estado? (sigla) ')
estado_desejado = estado_desejado.upper()
#abre o arquivo csv e cria um dict
arquivo = open('brasil.csv', encoding='utf8')
for registro in csv.DictReader(arquivo):
#compara se a sigla digitada é a mesma do registro de estado para fazer o calculo da densidade
    if registro['estado'] == estado_desejado:
#cria variavel densidade e divide os valores, convertendo para o tipo adequado
        densidade = int(registro['habitantes']) / float(registro['area'])
#apresenta valores com apenas 2 casas decimais e tipo float
print(f'Densidade de {registro["municipio"]}: {densidade:.2f} hab/km²') 
