        # Com base no que venho aprendendo sobre a linguagem python, começo o meu primeiro projeto,
        # Nele vou usar Módulos, tipos primitivos, comandos básicos, operadores aritiméticos e lógicos,
        # estruturas condicionais básicas e coleçõae
import random
print("=-" *15)
print(" \033[4;34mCALCULADORA IMC PARA ADULDOS\033[m")
print("=-" * 15)

nome = str(input('Informe o seu nome : '))
peso = float(input('Informe o seu peso Kg : '))
altura = float(input('Informe a sua altura : ' ))

imc = peso / (altura ** 2)

sorteios = {
    'abaixo' : ['Você está abaixo do peso!', 'Precisa ganhar um kilos!', 'Tem que comer mais feijão!'],
    'normal' : ['Seu peso está normal de acordo com a tabela.', 'Voçê está saudável!','Paraéns, continue assim.'],
    'sobrepe' : ['Está um puco acima.', 'Umas corridinhas cairia bem!', 'Melhor ficar de olho!'],
    'obesi1' : ['É bom começar a se exercitar!', 'Começe a regular a alimentação.', 'Preste atenção nas calorias.'],
    'obesi2' : ['Já esta em um grau um pouco mais alto de obesidade, começe a se cuidar.', 'Vá em um nutricionista para regrar a alimentação.',
                'Coma comidas mais saudáveis.'],
    'obesi3' : ['Você está em um grau muito avançado de obesidade, vá a um médico.',
                'Caso crítico de obesidade, começe imediatamente a se exercitar e se alimentar de forma saudável.'
                'Caso grave e de risco, você precisa perder peso!']

}

cores = { 'limpa' : '\033[m',
          'vermelho' : '\033[1;31m',
          'amarelo' : '\033[1;33m',
          'verde' : '\033[1;32m' }

if imc <= 18.5:
    print ('{}, o seu IMC é de {}{:.1f}{}'.format(nome, cores['amarelo'], imc, cores['limpa']))
    categoria = 'abaixo'
    sorteio = random.choice(sorteios[categoria])
    print (sorteio)
elif imc >= 18.6 and imc <= 24.9 :
    print ('{}, o seu IMC é de {}{:.1f}{}'.format(nome, cores['verde'], imc, cores['limpa']))
    categoria = 'normal'
    sorteio = random.choice(sorteios[categoria])
    print (sorteio)
elif imc >= 25.0 and imc <= 29.9:
    print ('{}, o seu IMC é de {}{:.1f}{}'.format(nome, cores['amarelo'], imc, cores['limpa']))
    categoria = 'sobrepe'
    sorteio = random.choice(sorteios[categoria])
    print (sorteio)
elif imc >=30.0 and  imc <= 34.9:
    print ('{}, o seu IMC é de {}{:.1f}{}'.format(nome, cores['amarelo'],imc,cores['limpa']))
    categoria = 'obesi1'
    sorteio = random.choice(sorteios[categoria])
elif imc >=35.0 and imc <= 39.9:
    print ('{}, o seu IMC é de {}{:.1f}{}'.format(nome, cores['vermelho'], imc, cores['limpa']))
    categoria = 'obesi2'
    sorteio = random.choice(sorteios[categoria])
    print (sorteio)
elif imc >=40.0:
    print('{}, o seu IMC é de {}{:.1f}'.format(nome, cores['vermelho'], imc, cores['limpa']))
    categoria = 'obesi3'
    sorteio = random.choice(sorteios[categoria])
    print (sorteio)
