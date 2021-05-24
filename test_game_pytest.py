import pytets
from game import TicTacToe

game = TicTacToe()

game.board[3] = 'X'
game.board[6] = 'O'


def test_move_available():
    assert 4 not in game.available_moves()
    assert 3 in game.available_moves()


def test_make_move():
    assert game.make_move(square=4, letter='X') is True
    assert game.make_move(square=6, letter='X') is False

    with pytest.raises(IndexError):
        assert game.make_move(9, 'X')

    with pytest.raises(TypeError):
        assert game.make_move(square='X', letter=2)
        assert game.make_move(square=3, letter=1)
