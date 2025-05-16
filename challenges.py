import random
from typing import List, Tuple
from player import Player


def olisort_challenge() -> Tuple[bool, str, str]:
    """
    Challenge: sort a list of random integers.

    Steps:
      1. Generate a random list of 10 ints between 0 and 100.
      2. Call Player.olisort to get the player's sorted list.
      3. Compute the expected sorted list using Python's sorted().
      4. Compare and return (passed, expected_str, actual_str).
    """
    # 1) generate input
    data: List[int] = [random.randint(0, 100) for _ in range(10)]

    # 2) get player's result via stub
    # We assume Player.olisort is implemented in player.py
    player = Player((0, 0), 0, 0)  # dummy position and bounds
    player_result: List[int] = player.olisort(data)

    # 3) expected result
    expected: List[int] = sorted(data)

    # 4) compare and return
    passed: bool = player_result == expected
    return passed, str(expected), str(player_result)

def Gavin_Riggins_challange():
        # helper functios to generate test cases
        def remove_pieces(board):
            from random import randint; 
            BOARD_SIZE = len(board)
            IGNORED_PIECES = ["KG"]
            COUNT_PER_LINE_PIECES_TO_REMOVE = [2, 6]

            removed_pieces = []
            selected_pieces = []
            w_points = 39
            b_points = 39

            # removes random pieces from the board, and appends them 
            # to the removed_pieces table
            for column in board:
                amount_to_displace = randint(COUNT_PER_LINE_PIECES_TO_REMOVE[0], COUNT_PER_LINE_PIECES_TO_REMOVE[1])

                # select indexes to remove
                for i in range(0, amount_to_displace):
                    selected_piece = column[i]
                    if randint(COUNT_PER_LINE_PIECES_TO_REMOVE[0], COUNT_PER_LINE_PIECES_TO_REMOVE[1]) == selected_piece: continue
                    if selected_piece == None: continue


                    formatted_piece = str.split(selected_piece, "_")
                    player = formatted_piece[0]; piece = formatted_piece[1]

                    # ignore the chosen piece if it exists in the IGNORED_PIECES list. 
                    if piece in IGNORED_PIECES: continue

                    selected_pieces.append(i)
                #   actual removal
                for index in selected_pieces:
                    if column[index] == None: continue

                    removed_pieces.append(column[index])
                    column[index] = None
                
            return board, removed_pieces
              
        # Places a piece on a random spot on the board. 
        def destribute_pieces(pieces, board, randomRemovalCount = 0):
            from random import randint; 
            BOARD_SIZE  = len(board)
            x = 0; y = 0

            for piece in pieces:
                while True:
                    if randomRemovalCount != 0 and randint(0, randomRemovalCount) == 1: continue
                    x = randint(0, BOARD_SIZE - 1)
                    y = randint(0, BOARD_SIZE - 1)

                    if board[y][x] == None: break

                board[y][x] = piece

            return board

        board_start = [
            ["b_RK", "b_KT", "b_BP", "b_QN", "b_KG", "b_BS", "b_KT", "b_RK",], # H
            ["b_PN", "b_PN", "b_PN", "b_PN", "b_PN", "b_PN", "b_PN", "b_PN",], # G
            [None, None, None, None, None, None, None, None,], # F 
            [None, None, None, None, None, None, None, None,], # E
            [None, None, None, None, None, None, None, None,], # D
            [None, None, None, None, None, None, None, None,], # C
            ["w_PN", "w_PN", "w_PN", "w_PN", "w_PN", "w_PN", "w_PN", "w_PN",], # B
            ["w_RK", "w_KT", "w_BS", "w_QN", "w_KG", "w_BS", "w_KT", "w_RK",], # A
            #1     2     3     4     5     6     7     8
        ]

        # Logic to suffle the board
        killed_pieces = remove_pieces(board_start) # removes pieces, returns board & list of removed

        board = killed_pieces[0]
        peice_list = killed_pieces[1]
        
        final_board = destribute_pieces(peice_list, board, 0) # destributes pieces from killed pieces & returns updated board
        
        print("\nBOARD SUFFLED")
        for collumn in final_board:
            print(collumn)

Gavin_Riggins_challange()
