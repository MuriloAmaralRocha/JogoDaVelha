import numpy as np
from random import *

class GameState:
    def __init__(self):
        self.board = [[''] * 3 for n in range(3)]
        self.rounds = 0

    def save(self):
        """
        Salva os dados do tabuleiro para uma string.    
        """
        return ';'.join([';'.join(x) for x in self.board])

    def restore(self, data):
        """
        Restaura os dados do tabuleiro a partir de uma string.
        """
        self.board = np.reshape(data.split(';'), (3,3)).tolist()

    def print(self):
        """
        Imprime o tabuleiro em um formato visual.
        """
        print("+---+---+---+")
        for row in self.board:
            print('|{}|{}|{}|'.format(row[0].center(3, ' '), row[1].center(3, ' '), row[2].center(3, ' ')))
            print("+---+---+---+"
                  )

    def move(self, row, col, piece):
        """
        Faz uma jogada no tabuleiro, nas posições dadas.        
        """

        # Valida os parâmetros de entrada
        if row < 0 or row > 2:
            raise RuntimeError('Número de linha inválido: {}'.format(row))
        if col < 0 or col > 2:
            raise RuntimeError('Número de coluna inválido: {}'.format(col))
        piece = piece.lower()
        if piece != 'x' and piece != 'o':
            raise RuntimeError('Peça inválida: {}'.format(piece))

        # Verifica se a posição jogada está vazia
        if self.board[row][col] != '':
            raise RuntimeError('Posição do tabuleiro já preenchida: {}x{}'.format(row, col))

        # Faz a jogada
        self.board[row][col] = piece

    # -------------------------------------------------
    def moveRandom(self, piece):
        """
        Faz uma jogada aleatória no tabuleiro, em uma das posições vazias.
        """

        # Cria uma lista com as posições vazias
        options = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    options.append((row, col))

        # Faz uma permutação aleatória nessa lista
        shuffle(options)

        # Faz a jogada na primeira posição da lista
        if len(options) > 0:
            row = options[0][0]
            col = options[0][1]
            self.move(row, col, piece)

    def PassarRodadas(self):
        self.rounds += 1

    def empate(self):
        if self.rounds >= 8:
            return True
        
    def ganhou(self):
        #checando linhas
        for i in range(3):
            resultado = self.board[i][0]+self.board[i][1]+self.board[i][2]
            if resultado=='xxx' or resultado =='ooo':
                return True

        #checando colunas
        for i in range(3):
            resultado = self.board[0][i]+self.board[1][i]+self.board[2][i]
            if resultado=='xxx' or resultado =='ooo':
                return True

        #checando diagonais
        diagonal1 = self.board[0][0]+self.board[1][1]+self.board[2][2]
        diagonal2 = self.board[0][2]+self.board[1][1]+self.board[2][0]
        if diagonal1=='xxx' or diagonal1=='ooo' or diagonal2=='xxx' or diagonal2=='ooo':
            return True

        return False

