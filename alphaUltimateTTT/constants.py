# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Game/Python implementation/Constants.ipynb.

# %% auto 0
__all__ = ['SIZE', 'NEXT_SYMBOL_INDEX', 'CONSTRAINT_INDEX', 'RESULT_INDEX', 'X_STATE_VALUE', 'O_STATE_VALUE', 'DRAW_STATE_VALUE',
           'UNCONSTRAINED_STATE_VALUE', 'MAPPING']

# %% ../nbs/Game/Python implementation/Constants.ipynb 3
#Copyright 2024 Gerardo Guerrero


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

