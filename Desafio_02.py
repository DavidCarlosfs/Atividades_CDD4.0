#Criar um jogo de pedra, papel e tesoura
jokenpo = ['Pedra', 'Papel', 'Tesoura']
cont1 = 0
cont2 = 0
empate = 0

for x in range(3):
    player1 = int(input("Digite: \n"
                    "0 para Pedra\n"
                    "1 para Papel\n"
                    "2 para Tesoura: "))

    player2 = int(input("Digite: \n"
                    "0 para Pedra\n"
                    "1 para Papel\n"
                    "2 para Tesoura: "))

    if player1 == 0:
        if player2 ==0:
            empate+=1
            print("Empatou!")
        if player2 == 1:
            cont2+=1
            print("Jogador 2 venceu essa rodada!")
        if player2 == 2:
            cont1+=1
            print("Jogador 1 venceu essa rodada!")
    elif player1 == 1:
        if player2 ==0:
            cont1+=1
            print("Jogador 1 venceu essa rodada!")
        if player2 == 1:
            empate+=1
            print("Empatou!")
        if player2 == 2:
            cont2+=1
            print("Jogador 2 venceu essa rodada!")
    elif player1 == 2:
        if player2 ==0:
            cont2+=1
            print("Jogador 2 venceu essa rodada!")
        if player2 == 1:
            cont1+=1
            print("Jogador 1 venceu essa rodada!")
        if player2 == 2:
            empate+=1
            print("Empatou!")

    if cont1 == 2:
        print("Jogador 1 venceu o jogo!")
        exit()
    elif cont2 == 2:
        print("Jogador 2 venceu o jogo!")
        exit()
    elif empate == 3:
        print("O jogo terminou em empate!")
