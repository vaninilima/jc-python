##Algoritmo para preparar leite vegetal de amendoim
#1.Verificar se o amendoim foi deixado de molho por 12 horas
#2.Colocar o amendoim em uma panela e cobrir com água para ferver
#3.Ao levantar fervura, desligar e deixar a panela fechada por 5 minutos
#4.Bater o amendoim na proporção de 1 xícara de amendoim para 3 ou 4 de água
#5.Coar o leite vegetal
#5.Deliciar-se!

#Instrução inicial
print('O leite vegetal de amendoim é uma alternativa saudável e saborosa. \n Esta aplicação irá te auxiliar a prepará-lo. \n')
print('Responda "s" para sim e "n" para não. Lembre-se: o amendoim deve ser lavado e deixado de molho de 6 a 12 horas. \n')
#Instrução sobre o periodo de molho do amendoim
molho = input('1. O amendoim está de molho por pelo menos 12 horas? \n')
if molho == 's':
    print('Lave o amendoim sem se preocupar com a casca e coloque-o em uma panela, coberto de água, em fogo médio. \n')
#Caso o amendoim tenha ficado de molho, ferva
    ferver = input('2. A água começou a ferver? \n')
    if ferver == 's':
        print('Apague o fogo e deixe a panela fechada por pelo menos 5 minutos, isto irá neutralizar o sabor do amendoim. \n')
        print('Separe o liquidificador ou mixer; um pano de prato limpo ou uma peneira fina de metal e água filtrada.\n')
#Após ferver, bata no liquidificador. O programa apresenta uma dica de como aproveitar a água utilizada na fervura
        liquidificador = input('3. Você aguardou os 5 minutos após a fervura? \n')
        if liquidificador == 's':
            print('Dica! Armazene a água da fervura em uma vasilha separada pois ela poderá ser usada para molhar as plantas. \n')
            print('Coloque o amendoim na proporção de 1 x. de amendoim para 3 x. de água filtrada. \n Bata por pelo menos 2 minutos. \n')
            print('Atenção! Caso esteja utilizando um mixer, leia as instruções para evitar o superaquecimento do equipamento. \n')
#Após bater no liquidificador ou mixer, orienta-se coar em trama fina
            coar = input('4. Você bateu o amendoim com água por 2 minutos ou mais? \n')
            if coar == 's':
                print('Coe o seu leite vegetal com a ajuda de um pano de prato, voal ou peneira fina. Prefira garrafas de vidro e lembre de higienizá-la bem. \n')
                print('Seu leite vegetal está pronto! =) Ele dura por 5 dias, no máximo, na geladeira! \n')
#Possibilidade de obter duas dicas de como aproveitar os resíduos do leite vegetal
                dica = input('5. Você quer duas dicas de como utilizar os resíduos desse leite vegetal? \n')
                if dica == 's':
                    print('Dica 1: Você pode torrar esse resíduo no forno e fazer um petisco. \n')
                    print('Dica 2: Misture resíduo com óleo de coco, aveia, açucar, banana madura amassada e passas para fazer biscoitos!\n')
#Condições no caso de alguma das etapas não ter sido concluída
                else:
                    print('Delicie-se com esse leite vegetal gostoso e barato!')
            else:
                print('Bata o amendoim por 2 minutos ou mais no liquidificador ou mixer. \n')
        else:
            print('Coloque o amendoim em uma panela coberto de água e aguarde levantar fervura.')
            print('Aguarde 5 minutos com a panela fechada e depois bata no liquidificador. \n')
    else:
        print('Coe seu leite vegetal. Lembre-se, quanto mais fina a trama, menos sedimentado é o leite. \n')
else:
    print('Repita as instruções desde o inicio. Eu costumo a deixar de molho de um dia para o outro. \n')
    print('O amendoim deve ser lavado e deixado coberto de água, de molho, de 6 a 12h. \n')
#Abre janela para finalizar o aplicativo ao final de cada fim de fluxo
quit()
