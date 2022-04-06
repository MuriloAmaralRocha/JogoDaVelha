from socket import *
from Jogo import GameState
serverPort = 1200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
vitoria = ""

while True: 

    print ("Aguardando conexao")
    connectionSocket, addr = serverSocket.accept()

    try:
        tabuleiro = GameState()

        tabuleiro.moveRandom('o')
        print('Eu joguei:')
        tabuleiro.print()

        connectionSocket.sendall(tabuleiro.save().encode('utf-8'))
        while True:
            data = connectionSocket.recv(1024)

            if not data: break
            tabuleiro.restore(data.decode('utf-8'))

            print('Jogada do oponente')
            tabuleiro.print()
            tabuleiro.PassarRodadas()
            print(tabuleiro.empate())
            if tabuleiro.ganhou():
                print('Oponente venceu.')
                vitoria = "1"
                connectionSocket.sendall(tabuleiro.save().encode('utf-8'))
                connectionSocket.send(vitoria.encode('utf-8'))
                break

            tabuleiro.moveRandom('o')
            print('Eu joguei:')
            tabuleiro.print()
            tabuleiro.PassarRodadas()
            print(tabuleiro.empate())
            if tabuleiro.ganhou():
                print('Servidor venceu!')
                vitoria = "0"
                connectionSocket.sendall(tabuleiro.save().encode('utf-8'))
                connectionSocket.send(vitoria.encode('utf-8'))
                break
            

            connectionSocket.sendall(tabuleiro.save().encode('utf-8'))
            if tabuleiro.empate():
                print('Empate, ninguem venceu')
                break

    finally:
        connectionSocket.close()
