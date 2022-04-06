from socket import *
import sys
from Jogo import GameState

serverName = "127.0.0.1"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

tabuleiro = GameState()
try:
    while True:
        data = clientSocket.recv(1024)
        tabuleiro.restore(data.decode('utf-8'))
        
        if tabuleiro.ganhou():
            tabuleiro.print()
            data = clientSocket.recv(1024)
            if data.decode('utf-8') == "1":
                print('Voce venceu!')
                break
            else:
                print('Servidor venceu.')
                break
        if tabuleiro.empate():
                print('Empate, ninguem venceu')
                break
        

        print('Jogada do servidor:')
        tabuleiro.print()
        tabuleiro.PassarRodadas()

        print('Sua vez:')
        print('------------------')

        suaVez = True
        while suaVez:
            linha = int(input('Linha: '))
            coluna = int(input('coluna: '))

            suaVez = False
            try:
                tabuleiro.move(linha, coluna, 'x')
                tabuleiro.PassarRodadas()
            except:
                suaVez = True
                print('Posicao invalida, tente nomavente')
                
        clientSocket.sendall(tabuleiro.save().encode('utf-8'))

finally:
    print('encerrando conexao')
    clientSocket.close()
