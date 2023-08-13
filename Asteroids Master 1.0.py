#Autor: Weslei Silva Santos
#Componente Curricular: EXA854 MI - Algoritmos 
#Concluido em: 24/04/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.



import pygame
import keyboard
import os
from time import sleep
from random import randint
os.system('cls')


                
def menu_inicial():
    print('*************')
    print('| ASTEROIDS |')
    print('*************')
    print('|JOGAR   (1)|')
    print('-------------')
    print('|RECORDES(2)|')
    print('-------------')
    print('|SOBRE   (3)|')
    print('-------------')
    print('|SAIR    (4)|')
    print('-------------')

def pausa():
    print('-------------')
    print('| PAUSA     |')
    print('-------------')
    print('|VOLTAR  (1)|')
    print('-------------')
    print('|RECORDES(2)|')
    print('-------------')
    print('|SOBRE   (3)|')
    print('-------------')
    print('|SAIR    (4)|')
    print('-------------')

def sobre():
    print('')
    print('---------------------------------')
    print('| Criador : Weslei Silva Santos |')
    print('| Asteroids Master 1.0          |')
    print('---------------------------------')
    print('')


# Função de exibição da tela do jogo
def tela():
    print('       ASTEROIDS') 
    print(f'VIDA: {life}      PONTOS: {score}')
    for l in range(21):
        for c in range(23):
            print(matriz[l][c], end = '')
        print()

    print(f'| NÃO DESTRUÍDOS: {nao_destruidos}   |')
    print('|||||||||||||||||||||||')



# A função 'game_over' adiciona 'FIM DE JOGO' na matriz 
def game_over():
    matriz[4][5] = 'F'
    matriz[4][6] = 'I'
    matriz[4][7] = 'M'

    matriz[4][10] = 'D'
    matriz[4][11] = 'E'
    
    matriz[4][13] = 'J'
    matriz[4][14] = 'O'
    matriz[4][15] = 'G'
    matriz[4][16] = 'O'


# A função 'try_again' adiciona 'NOVO JOGO' na matriz
def try_again():
    matriz[4][6] = 'N'
    matriz[4][7] = 'O'
    matriz[4][8] = 'V'
    matriz[4][9] = 'O'

    matriz[4][12] = 'J'
    matriz[4][13] = 'O'
    matriz[4][14] = 'G'
    matriz[4][15] = 'O'


# A função 'apaga_jogo' apaga os nomes da matriz
def apaga_jogo():
    matriz[4][5]  = ' '
    matriz[4][6]  = ' '
    matriz[4][7]  = ' '
    matriz[4][8]  = ' '
    matriz[4][9]  = ' '
    matriz[4][10] = ' '
    matriz[4][11] = ' '
    matriz[4][12] = ' '
    matriz[4][13] = ' '
    matriz[4][14] = ' '
    matriz[4][15] = ' '
    matriz[4][16] = ' '


# A função 'movimentacao_nave' adiciona a nave da matriz
def movimentacao_nave():
    matriz[16][extremidade_meio] = '*'
    matriz[17][extremidade_esquerda] = '*'
    matriz[17][extremidade_meio] = '*'
    matriz[17][extremidade_direita] = '*'     
                        

# A função 'resquicio_nave' apaga a nave da matriz
def resquicio_nave():        
    matriz[16][extremidade_meio] = ' '
    matriz[17][extremidade_esquerda] = ' '
    matriz[17][extremidade_meio] = ' '
    matriz[17][extremidade_direita] = ' '        

# Som da movimentação da nave 
def som_mov():
    pygame.init()
    pygame.mixer.music.load('mov.mp3')
    pygame.mixer.music.play()


# Som da destruição do asteroide
def som_explosao():
    pygame.init()
    pygame.mixer.music.load('explosao.mp3')
    pygame.mixer.music.play()  


# A função 'movimentacao_asteroide' apaga o asteroide na matriz
def resquicio_asteroide():
    matriz[linha4_asteroide][posicao_aleatoria] = ' '
    matriz[linha3_asteroide][posicao_aleatoria1] = ' '
    matriz[linha4_asteroide][posicao_aleatoria1] = ' '
    matriz[linha5_asteroide][posicao_aleatoria1] = ' '

    matriz[linha2_asteroide][posicao_aleatoria2] = ' '
    matriz[linha3_asteroide][posicao_aleatoria2] = ' '
    matriz[linha4_asteroide][posicao_aleatoria2] = ' '
    matriz[linha5_asteroide][posicao_aleatoria2] = ' '
    matriz[linha6_asteroide][posicao_aleatoria2] = ' '

    matriz[linha2_asteroide][posicao_aleatoria3] = ' '
    matriz[linha3_asteroide][posicao_aleatoria3] = ' '
    matriz[linha4_asteroide][posicao_aleatoria3] = ' '
    matriz[linha5_asteroide][posicao_aleatoria3] = ' '
    matriz[linha6_asteroide][posicao_aleatoria3] = ' '

    matriz[linha2_asteroide][posicao_aleatoria4] = ' '
    matriz[linha3_asteroide][posicao_aleatoria4] = ' '
    matriz[linha4_asteroide][posicao_aleatoria4] = ' '
    matriz[linha5_asteroide][posicao_aleatoria4] = ' '
    matriz[linha6_asteroide][posicao_aleatoria4] = ' '

    matriz[linha3_asteroide][posicao_aleatoria5] = ' '
    matriz[linha4_asteroide][posicao_aleatoria5] = ' '
    matriz[linha5_asteroide][posicao_aleatoria5] = ' '
    matriz[linha4_asteroide][posicao_aleatoria6] = ' '


# A função 'movimentacao_asteroide' adiciona o asteroide na matriz
def movimentacao_asteroide():
    matriz[linha4_asteroide][posicao_aleatoria] = '*'
    matriz[linha3_asteroide][posicao_aleatoria1] = '*'
    matriz[linha4_asteroide][posicao_aleatoria1] = '*'
    matriz[linha5_asteroide][posicao_aleatoria1] = '*'

    matriz[linha2_asteroide][posicao_aleatoria2] = '*'
    matriz[linha3_asteroide][posicao_aleatoria2] = '*'
    matriz[linha4_asteroide][posicao_aleatoria2] = '*'
    matriz[linha5_asteroide][posicao_aleatoria2] = '*'
    matriz[linha6_asteroide][posicao_aleatoria2] = '*'

    matriz[linha2_asteroide][posicao_aleatoria3] = '*'
    matriz[linha3_asteroide][posicao_aleatoria3] = '*'
    matriz[linha4_asteroide][posicao_aleatoria3] = '*'
    matriz[linha5_asteroide][posicao_aleatoria3] = '*'
    matriz[linha6_asteroide][posicao_aleatoria3] = '*'

    matriz[linha2_asteroide][posicao_aleatoria4] = '*'
    matriz[linha3_asteroide][posicao_aleatoria4] = '*'
    matriz[linha4_asteroide][posicao_aleatoria4] = '*'
    matriz[linha5_asteroide][posicao_aleatoria4] = '*'
    matriz[linha6_asteroide][posicao_aleatoria4] = '*'

    matriz[linha3_asteroide][posicao_aleatoria5] = '*'
    matriz[linha4_asteroide][posicao_aleatoria5] = '*'
    matriz[linha5_asteroide][posicao_aleatoria5] = '*'
    matriz[linha4_asteroide][posicao_aleatoria6] = '*'

# Asteroides não destruídos    
nao_destruidos = 0        
        
# Vida do usuário
life = 10

# Pontuação do jogador
score = 0
recordes = []

# Início do jogo
os.system('cls')
menu_inicial()
resposta = input('- ')
os.system('cls')

# Variável para adicionar o score na lista de recordes
podio = 1

while resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4':
    menu_inicial()
    resposta = input('- ')
    os.system('cls')



if resposta == '2':
    print('RECORDES:')
    print(recordes)
    print('')
    resposta = input('''JOGAR    (1)
SAIR     (4)''')
    os.system('cls')
    while resposta != '1' and resposta != '4':
        print('RECORDES:')
        print(recordes)
        print('')
        resposta = input('''JOGAR    (1)
SAIR     (4)''')
        os.system('cls')


elif resposta == '3':
    sobre()
    resposta = input('''JOGAR    (1)
SAIR     (4)''')
    os.system('cls')
    while resposta != '1' and resposta != '4':
        sobre()
        resposta = input('''JOGAR    (1)
SAIR     (4)''')
        os.system('cls')

# Variáveis demostrativas('inúteis')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
A = '*'
B = '*'
C = ' '


matriz = [['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', C, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', B, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', A, A, A, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
              ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]





    
# Variável que aleatoriza a posição da coluna do asteroide:    
posicao_aleatoria = randint(1, 15)

# Demais posições das colunas do asteroide
posicao_aleatoria1= posicao_aleatoria + 1
posicao_aleatoria2= posicao_aleatoria + 2
posicao_aleatoria3= posicao_aleatoria + 3
posicao_aleatoria4= posicao_aleatoria + 4
posicao_aleatoria5= posicao_aleatoria + 5
posicao_aleatoria6= posicao_aleatoria + 6
    
# Linhas iniciais do asteroide
linha4_asteroide = 3
linha2_asteroide = 1
linha3_asteroide = 2
linha5_asteroide = 4
linha6_asteroide = 5

# Colunas iniciais da nave    
extremidade_meio = 11 
extremidade_esquerda = 10 
extremidade_direita = 12


if resposta == '1':
    nome = input('Nome do jogador: ')
    recordes.append(nome)
    recordes.append(score)
    os.system('cls')
    try_again()
    tela()
    sleep(1)
    apaga_jogo()

# Menu principal     
while resposta == '1':
    
    while life != 0:

            # Movimentação da nave para a direita
            if keyboard.is_pressed('right'):
                som_mov()
                if extremidade_meio == 20:
                    resquicio_nave()
                    movimentacao_nave()         

                else:
                    os.system('cls')
                    resquicio_nave()

                    extremidade_meio     += 1
                    extremidade_direita  += 1
                    extremidade_esquerda += 1                        

                    movimentacao_nave()          
                    tela()
                    break


            # Movimentação da nave para a esquerda
            if keyboard.is_pressed('left'):
                som_mov()
                if extremidade_meio == 2:
                    resquicio_nave()
                    movimentacao_nave()

                else:   
                    os.system('cls')
                    resquicio_nave()

                    extremidade_meio -= 1
                    extremidade_direita -=1
                    extremidade_esquerda-=1 

                    movimentacao_nave()       
                    tela()
                    break


            # Movimentação do tiro
            tiro = extremidade_meio
            linha_do_tiro = 15
            if keyboard.is_pressed('space'):
                # Som do tiro
                pygame.init()
                pygame.mixer.music.load('tiro.mp3')
                pygame.mixer.music.play()
                os.system('cls')
                while True:
                    os.system('cls')
                    
                    matriz[linha_do_tiro][tiro] = 'o'
                    tela()           
                    matriz[linha_do_tiro][tiro] = ' '
                    linha_do_tiro -= 1
                    os.system('cls')

                    # Se o tiro chegar no final da tela, ele some
                    if linha_do_tiro == 1 :
                        break
                    
                    # Se o tiro atingir o asteroide, ambos somem e um novo asteroide é gerado
                    elif linha_do_tiro == linha6_asteroide and tiro == posicao_aleatoria2 or linha_do_tiro == linha6_asteroide and tiro == posicao_aleatoria3 or linha_do_tiro == linha6_asteroide and tiro == posicao_aleatoria4 or linha_do_tiro == linha5_asteroide and tiro == posicao_aleatoria1 or linha_do_tiro == linha5_asteroide and tiro == posicao_aleatoria5 or linha_do_tiro == linha5_asteroide and tiro == posicao_aleatoria4 or linha_do_tiro == linha5_asteroide and tiro == posicao_aleatoria3 or linha_do_tiro == linha5_asteroide and tiro == posicao_aleatoria2 or linha_do_tiro == linha4_asteroide and tiro == posicao_aleatoria6 or linha_do_tiro == linha4_asteroide and tiro == posicao_aleatoria: #or or linha_do_tiro == linha5_asteroide or linha_do_tiro == linha4_asteroide or linha_do_tiro == linha2_asteroide or linha_do_tiro == linha3_asteroide:
                        pygame.init()
                        pygame.mixer.music.load('explosao.mp3')
                        pygame.mixer.music.play()
                        os.system('cls')

                        resquicio_asteroide()

                        linha4_asteroide = 4
                        linha2_asteroide = 2
                        linha3_asteroide = 3
                        linha5_asteroide = 5
                        linha6_asteroide = 6

                        posicao_aleatoria = randint(1, 15)
                        posicao_aleatoria1= posicao_aleatoria + 1
                        posicao_aleatoria2= posicao_aleatoria + 2
                        posicao_aleatoria3= posicao_aleatoria + 3
                        posicao_aleatoria4= posicao_aleatoria + 4
                        posicao_aleatoria5= posicao_aleatoria + 5
                        posicao_aleatoria6= posicao_aleatoria + 6
                        
                        score += 10

                        recordes.pop(podio)
                        recordes.append(score)

                        break
                    tela()
                
                


             # Pausar e exibir o menu 
            if keyboard.is_pressed('esc'):
                os.system('cls')
                pausa()
                resposta = input('- ')
                # Estratégia para reduzir erros
                while resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4':
                    os.system('cls')
                    pausa()
                    resposta = input('- ')               
                
            # Mostrar recordes
            if resposta == '2':
                os.system('cls')
                print('RECORDES')
                print(recordes)       
                print(' ')
                resposta = input('VOLTAR  (1)')
                
                while resposta != '1':
                    os.system('cls')
                    print('RECORDES')
                    print(recordes)
                    print(' ')
                    resposta = input('VOLTAR  (1)')
                os.system('cls')
    

            # Mostrar sobre        
            if resposta == '3':
                os.system('cls')
                sobre()
                resposta = input('VOLTAR  (1)')
                os.system('cls')
                while resposta != '1':
                    sobre()
                    resposta = input('VOLTAR  (1)')
                    os.system('cls')

            # Voltar ao jogo
            if resposta == '1':
                os.system('cls')
                tela()
                    
            # Sair            
            if resposta == '4':
                os.system('cls')
                print('FIM DE JOGO')
                break



           
            # Movimentação do asteroide
            else:
                # Se o usuário não pressionar nada, o asteroide se move 
                if True:
                    sleep(0.6)
                    os.system('cls')
                    resquicio_asteroide()
                    
                    linha4_asteroide += 1
                    linha2_asteroide += 1
                    linha3_asteroide += 1
                    linha5_asteroide += 1
                    linha6_asteroide += 1
                    
                    movimentacao_asteroide()

                    tela()
                    
                    # Se o asteroide atigir o final da tela ele some  
                    if linha6_asteroide == 19:
                        os.system('cls')

                        resquicio_asteroide()

                        # Um novo asteroide é gerado
                        linha4_asteroide = 4
                        linha2_asteroide = 2
                        linha3_asteroide = 3
                        linha5_asteroide = 5
                        linha6_asteroide = 6

                        posicao_aleatoria = randint(1, 15)
                        posicao_aleatoria1= posicao_aleatoria + 1
                        posicao_aleatoria2= posicao_aleatoria + 2
                        posicao_aleatoria3= posicao_aleatoria + 3
                        posicao_aleatoria4= posicao_aleatoria + 4
                        posicao_aleatoria5= posicao_aleatoria + 5
                        posicao_aleatoria6= posicao_aleatoria + 6
                        # O jogador perde uma vida
                        life -= 1
                        # Mais um asteroide não destruido
                        nao_destruidos += 1
                        movimentacao_nave()
                        som_explosao()

                    #Se o asteroide bater de frente com as extremidades da nave, a vida é zerada
                    if linha6_asteroide == 16 and posicao_aleatoria2 == extremidade_meio or linha6_asteroide == 16 and posicao_aleatoria4 == extremidade_meio or linha6_asteroide == 16 and posicao_aleatoria3 == extremidade_meio or linha6_asteroide == 16 and posicao_aleatoria4 == extremidade_esquerda or linha6_asteroide == 16 and posicao_aleatoria2 == extremidade_direita or linha5_asteroide == 17 and posicao_aleatoria5 == extremidade_esquerda or linha5_asteroide == 17 and posicao_aleatoria1 == extremidade_direita or linha4_asteroide == 17 and posicao_aleatoria == extremidade_direita or linha5_asteroide == 17 and posicao_aleatoria6 == extremidade_esquerda:

                        som_explosao()
                        life = 0
                        
                    # Quando a vida for 0, o jogo acaba e é possivel acessar o menu
                    if life == 0:

                        os.system('cls')
                        # A nave é apagada da matriz
                        resquicio_nave()
                        # A o asteroide é apagado da matriz
                        resquicio_asteroide()
                        # Fim de jogo
                        game_over()
                        tela()
                        sleep(1)
                        os.system('cls')

                        # Novo menu
                        menu_inicial()
                        resposta = input('- ').upper()
                        os.system('cls')
                        # Estratégia para reduzir erros
                        while resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4':
                            menu_inicial()
                            resposta = input('- ').strip()
                            os.system('cls')                                           

                        # Todos os dados são zerados
                        apaga_jogo()
                        life = 10
                        score = 0
                        nao_destruidos = 0
                        podio += 2

                        # Um novo asteroide é gerado
                        linha4_asteroide = 4
                        linha2_asteroide = 2
                        linha3_asteroide = 3
                        linha5_asteroide = 5
                        linha6_asteroide = 6

                        posicao_aleatoria = randint(1, 15)
                        posicao_aleatoria1= posicao_aleatoria + 1
                        posicao_aleatoria2= posicao_aleatoria + 2
                        posicao_aleatoria3= posicao_aleatoria + 3
                        posicao_aleatoria4= posicao_aleatoria + 4
                        posicao_aleatoria5= posicao_aleatoria + 5
                        posicao_aleatoria6= posicao_aleatoria + 6

                        # A nave volta a posição central
                        extremidade_meio = 11 
                        extremidade_esquerda = 10 
                        extremidade_direita = 12

                        movimentacao_nave()

                            

                        # Mostrar recordes
                        if resposta == '2':
                            os.system('cls')
                            print('RECORDES')
                            print(recordes)       
                            print(' ')
                            resposta = input('''JOGAR    (1)
SAIR     (4)''')
                            # Estratégia para reduzir erros
                            while resposta != '1':
                                os.system('cls')
                                print('RECORDES')
                                print(recordes)
                                print(' ')
                                resposta = input('''JOGAR    (1)
SAIR     (4)''')
                            os.system('cls')
                                


                        # Mostrar sobre        
                        if resposta == '3':
                            os.system('cls')
                            sobre()
                            resposta = input('''JOGAR    (1)
SAIR     (4)''')
                            os.system('cls')
                            # Estratégia para reduzir erros
                            while resposta != '1' and resposta != '4':
                                sobre()
                                resposta = input('''JOGAR    (1)
SAIR     (4)''')
                                os.system('cls')

                        # Jogar novamente 
                        if resposta == '1':
                            nome = input('Nome do jogador: ')
                            recordes.append(nome)
                            recordes.append(score)
                            os.system('cls')
                            try_again()
                            tela()
                            sleep(1)
                            apaga_jogo()
                            
                            
                        

                                    
                        
                        
                       
                        

