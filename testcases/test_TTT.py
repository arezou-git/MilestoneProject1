'''
Created on 20 Jan 2020

@author: Arezo
'''
from TicTacToe import *
import unittest

class Test_TicTacToe(unittest.TestCase):
    
    def test_display_board(self):
        test_board = ['#','X','O','X','O','X','O','X','O','X']
        display_board(test_board)

    def test_player_input(self):
        ply = 'testName'
        player1_marker, player2_marker = player_input(ply)
        self.assertEqual(player1_marker, 'x')
        self.assertEqual(player2_marker, 'o')
    
    def test_place_marker(self):
        test_board = ['#','X','O','X','O','X','O','X','O','X']
        place_marker(test_board, 'test', 4)
        self.assertEqual(test_board, ['#','X','O','X','test','X','O','X','O','X'])
     
 
    def test_win_check(self):
        test_board = ['#','X','X','X','O','X','O','X','O','X']
        self.assertTrue(win_check(test_board, 'X'))

    
    def test_choose_first(self):
        name1, name2 = choose_first()
        self.assertTrue(name1)
        self.assertTrue(name2)

                         
    def test_space_check_true(self):
        test_board = ['#','1','X','X','O','X','O','X','8','X']
        self.assertTrue(space_check(test_board, 8))
    
    def test_soace_check_false(self):
        test_board = ['#','1','X','X','O','X','O','X','8','X']
        self.assertFalse(space_check(test_board, 2))  
     
    def test_full_board_check_true(self):
        test_board = ['#','O','X','X','O','X','O','X','O','X']
        self.assertTrue(full_board_check(test_board))
    
    def test_full_board_check_false(self):
        test_board = ['#','1','X','X','O','X','O','X','O','X']
        self.assertFalse(full_board_check(test_board))    
              
    def test_player_choice_outof_range(self):
        board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        position = player_choice(board, 'Dear Tester')
        self.assertTrue(position<10 or position>0)

    def test_player_choice_isNotinteger(self):
        board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        position = player_choice(board, 'Dear Tester')
        self.assertEqual(type(position), int)
                
    def test_replay(self):
        print('enter y')
        self.assertTrue(replay())
        print('enter n')
        self.assertFalse(replay())
    


if __name__ == '__main__':
    unittest.main()      