# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Game/ultimatettt.ipynb.

# %% auto 0
__all__ = ['SIZE', 'NEXT_SYMBOL_INDEX', 'CONSTRAINT_INDEX', 'RESULT_INDEX', 'X_STATE_VALUE', 'O_STATE_VALUE', 'DRAW_STATE_VALUE',
           'UNCONSTRAINED_STATE_VALUE', 'MAPPING', 'Move', 'UltimateTicTacToe', 'utttError']

# %% ../nbs/Game/ultimatettt.ipynb 3
#0-80 squares, 81-89 result of each subgame, 90 next symbol, 91 subgame constraint, 92 result of uttt
SIZE = 93 
NEXT_SYMBOL_INDEX = 90
CONSTRAINT_INDEX = 91
RESULT_INDEX = 92

X_STATE_VALUE = 1
O_STATE_VALUE = 2
DRAW_STATE_VALUE = 3
UNCONSTRAINED_STATE_VALUE = 9
MAPPING ={
#First subgame
(1,1): 0, (1,2): 1, (1,3): 2, 
(2,1):3, (2,2): 4, (2,3): 5,
(3,1):6, (3,2):7, (3,3):8, 

#Second subgame
(1,4):9, (1,5):10, (1,6):11, 
(2,4):12, (2,5):13, (2,6):14,
(3,4):15, (3,5):16, (3,6):17,

#Third subgame
(1,7):18, (1,8):19, (1,9):20, 
(2,7):21, (2,8):22, (2,9):23,
(3,7):24, (3,8):25, (3,9):26,

#Fourth subgame
(4,1):27, (4,2):28, (4,3):29, 
(5,1):30, (5,2):31, (5,3):32,
(6,1):33, (6,2):34, (6,3):35,

#Fifth subgame
(4,4):36, (4,5):37, (4,6):38, 
(5,4):39, (5,5):40, (5,6):41,
(6,4):42, (6,5):43, (6,6):44,

#Sixth subgame
(4,7):45, (4,8):46, (4,9):47, 
(5,7):48, (5,8):49, (5,9):50,
(6,7):51, (6,8):52, (6,9):53,

#Seventh subgame
(7,1):54, (7,2):55, (7,3):56, 
(8,1):57, (8,2):58, (8,3):59,
(9,1):60, (9,2):61, (9,3):62,

#Eighth subgame
(7,4):63, (7,5):64, (7,6):65, 
(8,4):66, (8,5):67, (8,6):68,
(9,4):69, (9,5):70, (9,6):71,

#Ninth subgame
(7,7):72, (7,8):73, (7,9):74, 
(8,7):75, (8,8):76, (8,9):77,
(9,7):78, (9,8):79, (9,9):80,
}


# %% ../nbs/Game/ultimatettt.ipynb 4
class Move:
    def __init__(self,
                symbol: int, # X_STATE_VALUE = 1 or O_STATE_VALUE = 2
                index: int): # int from 0 to 80
        '''A move contains the symbol (represented as an int) and the index (int from 0 to 80) where the symbol will be placed.'''
        self.symbol = symbol  # X_STATE_VALUE or O_STATE_VALUE
        self.index = index  # int from 0 to 80

    def is_symbol_X(self) -> bool:
        return self.symbol == X_STATE_VALUE

    def is_symbol_O(self) -> bool:
        return self.symbol == O_STATE_VALUE

    def __str__(self):
        output = '{cls}(symbol={symbol}, index={index})'
        output = output.format(
            cls=self.__class__.__name__,
            symbol={X_STATE_VALUE: 'X', O_STATE_VALUE: 'O'}[self.symbol],
            index=self.index,
        )
        return output

# %% ../nbs/Game/ultimatettt.ipynb 5
class UltimateTicTacToe:
    def __init__(self,
                state:list() = None): #If no state is given, it generates a new one. 
        '''The state is a list of 93 elements. \n
        The first 81 elements are the state of each square, 0 for empty, 1 for X and 2 for O. \n
        The next 9 elements are the result of each subgame: 0 while being played, 1 is win for X, 2 is a win for O and 3 for draw.\n 
        The next element is the next symbol to play: 1 for X and 2 for O.\n 
        The next element is the index of the subgame that is constrained, 9 for no subgame constraint. \n
        The last element is the result of the UTTT: 0 while being played, 1 is win for X, 2 is a win for O and 3 for draw.'''
        if state:
            self.state = state
        else:
            self.state = [0] * SIZE
            self.state[NEXT_SYMBOL_INDEX] = X_STATE_VALUE #X always starts the game
            self.state[CONSTRAINT_INDEX] = UNCONSTRAINED_STATE_VALUE #no subgame is constrained at the beginning


    @property
    def result(self) -> int:
        return self.state[RESULT_INDEX]
    
    @property
    def next_symbol(self) -> int:
        return self.state[NEXT_SYMBOL_INDEX]
    
    @property
    def constraint(self) -> int:
        return self.state[CONSTRAINT_INDEX]

    def is_game_over(self) -> bool:
        '''Returns True if the game is over, False otherwise.'''
        return bool(self.state[RESULT_INDEX])
    
    def is_constrained(self) -> bool:
        '''Returns True if a subgame is constrained, False otherwise.'''
        return self.state[CONSTRAINT_INDEX] != UNCONSTRAINED_STATE_VALUE
      
    def _verify_move(self, move: Move):
        illegal_move = f"Illegal move {move} - "
        if not (0 <= move.index < 81):
            raise utttError(illegal_move + "index outside the valid range")
        if self.is_constrained() and self.constraint != move.index // 9:
            raise utttError(illegal_move + f"violated constraint = {self.constraint}")
        if self.state[81 + move.index // 9]:
            raise utttError(illegal_move + "index from terminated subgame")
        if self.state[move.index]:
            raise utttError(illegal_move + "index already taken")
        
    def _get_subgame_result(self,
                            subgame_index: int) -> int:   #Index of the subgame from 0 to 8
        '''Returns the result of the subgame.''' 
        return self.state[81 + subgame_index]
        
    def _update_state(self,
                      move: Move): #Updates the state of the game after a move.
        '''Updates the state of the game after a move. It also verifies if the subgame and the game are over.'''
        self.state[move.index] = move.symbol
        self.state[NEXT_SYMBOL_INDEX] = X_STATE_VALUE + O_STATE_VALUE - move.symbol

        self._verify_subgame_result(move)
        self._verify_game_result(move)

        if not self.is_game_over():
            #Check if the subgame on index move.index % 9 is still being played. If it is, constraint to it. Else, unconstrain the game.
            subgame_index = move.index % 9
            if not self._get_subgame_result(subgame_index):
                self.state[CONSTRAINT_INDEX] = subgame_index
            else:
                self.state[CONSTRAINT_INDEX] = UNCONSTRAINED_STATE_VALUE

    def make_move(self,
                move: Move, #Receives a move and updates the state of the game.
                verify: bool = True): #A boolean to verify if the move is valid.
        '''Makes a move in the game. It verifies if the move is valid'''
        if verify:
            if self.is_game_over():
                raise utttError("Illegal move " + str(move) + ' - The game is over')
            self._verify_move(move)

        self._update_state(move)
        self._verify_game_result(move)
        if self.is_game_over():
            print('The game is over')
            if self.state[RESULT_INDEX] == DRAW_STATE_VALUE:
                print('The game is a draw')
            elif self.state[RESULT_INDEX] == X_STATE_VALUE:
                print('X is the winner')
            else:
                print('O is the winner')

    def is_winning_position(self,
                            game:list) -> bool: #Receives a list of 9 elements and returns True if it is a winning position, False otherwise.
        '''Returns True if the game is a winning position, False otherwise.'''
        return game[0] == game[1] == game[2] != 0 or game[3] == game[4] == game[5] != 0 or game[6] == game[7] == game[8] != 0 or game[0] == game[3] == game[6] != 0 or game[1] == game[4] == game[7] != 0 or game[2] == game[5] == game[8] != 0 or game[0] == game[4] == game[8] != 0 or game[2] == game[4] == game[6] != 0

    def is_drawn_position(self,
                          game:list) -> bool: #Receives a list of 9 elements and returns True if it is a drawn position, False otherwise.
        '''Returns True if the game is a drawn position, False otherwise.'''
        return 0 not in game
    
    def _verify_subgame_result(self, move):
        '''Verifies if the subgame is over and updates the state of the subgame.'''
        subgame_index = move.index // 9
        subgame = self.state[subgame_index * 9 : subgame_index * 9 + 9]
        if self.is_winning_position(subgame):
            self.state[81 + subgame_index] = move.symbol
        elif self.is_drawn_position(subgame):
            self.state[81 + subgame_index] = DRAW_STATE_VALUE
    
    def _verify_game_result(self,move):
        '''Verifies if the game is over and updates the state of the game.'''
        symbol = move.symbol
        game = self.state[81:90]
        if self.is_winning_position(game):
            self.state[RESULT_INDEX] = symbol
        elif self.is_drawn_position(game):
            self.state[RESULT_INDEX] = DRAW_STATE_VALUE
    
    def is_winner(self, index: int) -> bool:
        '''Returns True if the symbol in the index is the winner, False otherwise.'''
        return self.state[81 + index] == 1 or self.state[81 + index] == 2
    
    def get_legal_indexes(self) -> list:
        '''Returns a list with the indexes of the legal moves.'''
        if not self.is_constrained():
            ## If the game is not constrained, all the empty squares are legal moves, except the ones from subgames that are already over.
            legal = []
            for subgame_index in range(9):
                if not self._get_subgame_result(subgame_index):
                    for i in range(subgame_index * 9, subgame_index * 9 + 9):
                        if not self.state[i]:
                            legal.append(i)
            return legal
        else:
            subgame_index = self.state[CONSTRAINT_INDEX]
            return [i for i in range(subgame_index * 9, subgame_index * 9 + 9) if not self.state[i]]

    def __str__(self):
        state_values_map = {
            X_STATE_VALUE: 'X',
            O_STATE_VALUE: 'O',
            DRAW_STATE_VALUE: '=',
            0: '·',
        }

        subgames = [state_values_map[s] for s in self.state[:81]]
        supergame = [state_values_map[s] for s in self.state[81:90]]

        if not self.is_game_over():
            legal_indexes = self.get_legal_indexes()
            for legal_index in legal_indexes:
                subgames[legal_index] = '•'

            if self.is_constrained():
                supergame[self.constraint] = '•'
            elif self.constraint == UNCONSTRAINED_STATE_VALUE:
                supergame = ['•' if s == '·' else s for s in supergame]

        sb = lambda l, r: ' '.join(subgames[l : r + 1])
        sp = lambda l, r: ' '.join(supergame[l : r + 1])

        subgames_str = [
            '    1 2 3   4 5 6   7 8 9',
            '  1 ' + sb(0, 2)   + ' │ ' + sb(9, 11) +  ' │ ' + sb(18, 20),
            '  2 ' + sb(3, 5)   + ' │ ' + sb(12, 14) + ' │ ' + sb(21, 23),
            '  3 ' + sb(6, 8)   + ' │ ' + sb(15, 17) + ' │ ' + sb(24, 26),
            '    ' + '—' * 21,
            '  4 ' + sb(27, 29) + ' │ ' + sb(36, 38) + ' │ ' + sb(45, 47),
            '  5 ' + sb(30, 32) + ' │ ' + sb(39, 41) + ' │ ' + sb(48, 50),
            '  6 ' + sb(33, 35) + ' │ ' + sb(42, 44) + ' │ ' + sb(51, 53),
            '    ' + '—' * 21,
            '  7 ' + sb(54, 56) + ' │ ' + sb(63, 65) + ' │ ' + sb(72, 74),
            '  8 ' + sb(57, 59) + ' │ ' + sb(66, 68) + ' │ ' + sb(75, 77),
            '  9 ' + sb(60, 62) + ' │ ' + sb(69, 71) + ' │ ' + sb(78, 80),
        ]

        supergame_str = [
            '  ' + sp(0, 2),
            '  ' + sp(3, 5),
            '  ' + sp(6, 8),
        ]

        subgames_str = '\n'.join(subgames_str)
        supergame_str = '\n'.join(supergame_str)

        next_symbol = state_values_map[self.next_symbol]
        constraint = 'None' if self.constraint == UNCONSTRAINED_STATE_VALUE else str(self.constraint+1)
        result = 'In Game'
        if self.result == X_STATE_VALUE:
            result = 'X won'
        elif self.result == O_STATE_VALUE:
            result = 'O won'
        elif self.result == DRAW_STATE_VALUE:
            result = 'Draw'

        output = f'{self.__class__.__name__}(\n'
        output += f'  subgames:\n{subgames_str}\n'
        if not self.is_game_over():
            output += f'  next player: {next_symbol}\n'
            output += f'  constraint: {constraint}\n'
        output += f'  supergame:\n{supergame_str}\n'
        output += f'  result: {result}\n)'
        return output
    
    def map_matrix_to_subgame(self, matrix_index: int) -> int:
        digit_1 = matrix_index // 10 
        digit_2 = matrix_index % 10
        subgame_index = MAPPING[(digit_1, digit_2)]
        return subgame_index

    def play(self, matrix_index: int):
        '''Plays the game. Receives a matrix index and makes a move in the corresponding state index.'''
        index = self.map_matrix_to_subgame(matrix_index)
        self.make_move(Move(self.next_symbol, index))
        print(self)

# %% ../nbs/Game/ultimatettt.ipynb 6
class utttError(Exception):
    pass
