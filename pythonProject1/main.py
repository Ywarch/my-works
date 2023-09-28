#importar a pasta random e time
import random
import time
import os

import commands

#definir as escolhas possíveis do jogo e colocar o reinicializador while
while True:
    escolhe = ["pedra","papel","tesoura"]

#definir qual foi a escolha do computador
    computador = random.choice(escolhe)
    jogador = None

    while not jogador:
        jogador = input("Vamos ver se você ganha da máquina! Escolha entre pedra, papel ou tesoura: \n")
        # para caso a resposta não seja nada dentro de "escolhe"
        if jogador.lower() not in escolhe:
            commands.texto_slowed("Eiii, digite apenas 'pedra', 'papel' ou 'tesoura'! Senão o jogo não funciona :(")
            jogador = None

        
#para caso as respotas sejam iguais
    if jogador.lower() == computador:
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Temos um empate!\n")
    
#para caso o jogador escolha pedra

    elif jogador.lower() == "pedra" and computador == "papel":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Infelizmente a máquina venceu, tente novamente :(\n")

    elif jogador.lower() == "pedra" and computador == "tesoura":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Parabéns, você ganhou! Jogue novamente!\n")

#para caso o jogador escolha papel

    elif jogador.lower() == "papel" and computador == "tesoura":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Infelizmente a máquina venceu, tente novamente :(\n")
    
    elif jogador.lower() == "papel" and computador == "pedra":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Parabéns, você ganhou! Jogue novamente\n")

#para caso o jogador escolha tesoura

    elif jogador.lower() == "tesoura" and computador == "pedra":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Infelizmente a máquina venceu, tente novamente :(\n")
    
    elif jogador.lower() == "tesoura" and computador == "papel":
        commands.texto_slowed(f"Jogador escolheu...{jogador.lower()}!")
        commands.texto_slowed(f"O computador escolheu...{computador}!")
        print("Parabéns, você ganhou! Jogue novamente\n")
        
    jogar_de_novo = input("Você deseja jogar de novo??? (sim/não) \n").lower()
    
    if jogar_de_novo != "sim":
        print("Muito obrigado por jogar pedra, papel, tesoura comigo!")
        break
        
    else:
        commands.texto_slowed("Vamos jogar de novo!!!")
    

