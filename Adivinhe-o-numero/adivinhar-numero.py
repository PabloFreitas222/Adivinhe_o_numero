#Inicio do projeto
from random import randint
from time import sleep
import os
# Limpa a tela para começar o jogo com uma tela limpa
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    # Exibe a pergunta inicial sobre interesse em participar do jogo
    print(''' \033[1;35mVOCÊ TEM INTERESSE EM PARTICIPAR DO JOGO?\033[m
          
          \033[4;32msim\033[m
          \033[4;31mnão\033[m
    
''')
    # Solicita a opção do usuário (sim ou não)
    opicao = str(input('\033[4;33mopição [sim/nao]:\033[m')).upper().strip()
    # Verifica se a entrada é válida
    if opicao != 'SIM' and opicao != 'NAO':
        print('\033[1;31mTente Novamente.\033[m')
    # Continua pedindo a entrada até que seja válida
    while opicao != 'SIM' and opicao != 'NAO':
        opicao = str(input('\033[4;33mopição [sim/nao]:\033[m')).upper().strip()
        if opicao != 'SIM' and opicao != 'NAO':
            print('\033[1;31mTente Novamente.\033[m')
    # Se o usuário escolher 'NAO', encerra o loop e o programa
    if opicao == 'NAO':
        break
    # Exibe mensagem de carregamento
    print('''
          CARREGANDO...''')
    sleep(2.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Explica as regras do jogo
    print('''\033[1;34m
         + O JOGO É O SEGUINTE +\033[m''')
    sleep(2.5)
    print('''
         TRATA-SE DE UM JOGO DE ADIVINHAÇÕES DE NUMEROS 
         UM NUMERO ENTRE 1 A 3 ONDE 
         VOCÊ E O COMPUTADOR JOGAM. AMBOS TÊM QUE
         ADIVINHAR O NUMERO DO OUTRO, E QUEM FIZER
         3 PONTOS PRIMEIRO GANHA O JOGO.
''')
    sleep(2)
    # Confirmação para iniciar o jogo
    print('("ok" para confirmar.)')
    confirmacao = str(input('👍?')).upper().strip()
    if confirmacao != 'OK':
        print('\033[1;31mTente Novamente.\033[m')
    # Continua pedindo a confirmação até que seja 'OK'
    while confirmacao != 'OK':
        confirmacao = str(input('👍?')).upper().strip()
        if confirmacao != 'OK':
            print('\033[1;31mTente Novamente.\033[m')
        if confirmacao == 'OK':
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1.5)
    print('''
          \033[1;34mVAMOS LÁ\033[m''')
    sleep(2)
    ponto_pessoa = 0
    ponto_computador = 0   
    # Loop do jogo até que alguém atinja 5 pontos
    while ponto_pessoa < 1 and ponto_computador < 1:
        # Solicita o número escolhido pelo jogador
        while True:
            num_escolhido_pessoa = (input('''    
                \033[1;32mNúmero entre 1 a 3:\033[m'''))
            sleep(2)
            if not num_escolhido_pessoa.strip() or not num_escolhido_pessoa.isdigit() or not (1 <= int(num_escolhido_pessoa) <= 3):
                print('''        \033[1;31mResposta inválida.\033[m''')
            elif 1 <= int(num_escolhido_pessoa) <= 3:
                break     
        num_da_pesssoa = int(num_escolhido_pessoa)
        numeros_computador = randint(1, 3)       
        # Exibe os números escolhidos pelo jogador e pelo computador
        print(f'''
            \033[1mVocê falou\033[m \033[4;33m{num_da_pesssoa}\033[m \033[1me o computador pensou\033[m \033[4;33m{numeros_computador}\033[m.
        ''')      
        # Verifica se o jogador acertou o número do computador
        if num_da_pesssoa != numeros_computador:
            sleep(2)
            print('\033[1;31mvocê errou\033[m')
        else:
            sleep(2)
            ponto_pessoa += 1
            print('\033[1;36m+1 Ponto pra você\033[m')
            if ponto_pessoa == 3:
                print('Você venceu!')
        print(f'Sua pontuação atual: {ponto_pessoa}')   
        sleep(2)
        if ponto_pessoa == 3:
            break       
        print('''\033[1;33m
                            \SUA VEZ/\033[m''')  
        # Solicita o número que o jogador pensa que o computador escolheu
        while True:
            pessoa_computador = (input('''    
                \033[1;32mQue número você está pensando?\033[m'''))
            sleep(2)
            if not pessoa_computador.strip() or not pessoa_computador.isdigit() or not (1 <= int(pessoa_computador) <= 3):
                print('''        \033[1;31mResposta inválida.\033[m''')
            elif 1 <= int(pessoa_computador) <= 3:
                break      
        p_computador = int(pessoa_computador)
        numeros_computador = randint(1, 3)      
        # Exibe os números escolhidos pelo computador e pelo jogador
        print(f'''
            \033[1mComputador falou\033[m \033[4;33m{numeros_computador}\033[m \033[1me você pensou\033[m \033[4;33m{p_computador}\033[m.
        ''')     
        # Verifica se o computador acertou o número do jogador
        if p_computador != numeros_computador:
            sleep(2)
            print('\033[1;31mcomputador errou\033[m')
        else:
            sleep(2) 
            ponto_computador += 1
            print('\033[1;36m+1 Ponto pro computador\033[m')
            if ponto_computador == 3:
                print('O computador venceu!')
        print(f'Pontuação do computador: {ponto_computador}')   
        sleep(2)
     # Pergunta se o jogador quer jogar novamente
    jogar_d_novo = input('\033[1mGostaria de jogar de novo [sim/nao]?\033[m').strip().upper()

    if jogar_d_novo == 'SIM':
        sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')  
    elif jogar_d_novo == 'NAO':
        break
    else:
        while jogar_d_novo != 'NAO' and jogar_d_novo != 'SIM':
            print('resposta invalida.')
            jogar_d_novo = input('\033[1mGostaria de jogar de novo [sim/nao]?\033[m').strip().upper()
            if jogar_d_novo == 'SIM':
                sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')  
            elif jogar_d_novo == 'NAO':
                 break
# Mensagem de despedida
sleep(1)
print('\033[1;36mobrigado por participar!\033[m')