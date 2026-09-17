# Calculadora de IMC

Programa em Python que calcula o Índice de Massa Corporal (IMC) do usuário e exibe o resultado de forma colorida no terminal, junto com uma mensagem sorteada de acordo com a categoria do IMC.

## Como funciona

1. O programa pede o nome, peso (kg) e altura (m) do usuário.
2. Calcula o IMC com a fórmula: `IMC = peso / (altura ** 2)`.
3. Mostra o resultado no terminal com uma cor diferente dependendo da faixa do IMC (verde, amarelo ou vermelho).
4. Sorteia aleatoriamente uma entre três frases relacionadas à categoria do IMC (abaixo do peso, normal, sobrepeso, obesidade grau 1, 2 ou 3).

## Categorias de IMC

| Categoria | Faixa de IMC |
|---|---|
| Abaixo do peso | até 18.5 |
| Peso normal | 18.6 a 24.9 |
| Sobrepeso | 25.0 a 29.9 |
| Obesidade grau 1 | 30.0 a 34.9 |
| Obesidade grau 2 | 35.0 a 39.9 |
| Obesidade grau 3 | 40.0 ou mais |

## Tecnologias e conceitos utilizados

- **Python**
- Biblioteca `random` (para sortear as mensagens)
- Coleções (dicionários e listas) para organizar as mensagens e as cores
- Formatação de strings com `.format()`
- Estruturas condicionais (`if` / `elif`)
- Códigos ANSI para colorir o texto no terminal

## Observação

Este é um projeto de estudo, feito para praticar lógica de programação, estruturas condicionais e uso de bibliotecas em Python.
