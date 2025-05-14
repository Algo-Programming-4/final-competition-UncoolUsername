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
        # helper function to generate test cases
        def remove_pieces(board):
            BOARD_SIZE = len(board)
            IGNORED_PIECES = ["KG"]
            COUNT_PER_LINE_PIECES_TO_REMOVE = [2, 6]

            from random import randint; from math import ceil
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
                    if i > BOARD_SIZE: i = BOARD_SIZE
                    selected_piece = column[i]
                    if selected_piece == None: continue
                    
                    formatted_piece = str.split(selected_piece, "_")
                    player = formatted_piece[0]; piece = formatted_piece[1]

                    # ignore the chosen piece if it exists in the IGNORED_PIECES list. 
                    if piece in IGNORED_PIECES: continue

                    list.append(selected_pieces, i)

                  # actual removal
                  for index in selected_pieces:
                     board[index] = 0

            return remove_pieces
              
                
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
        print(remove_pieces(board_start))

Gavin_Riggins_challange()
