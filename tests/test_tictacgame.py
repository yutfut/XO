import pytest

from game_xo.game_xo import TicTacGame

test_game = TicTacGame()


@pytest.mark.parametrize(
    'test_dictionary, answer', [
        (test_game.game_board, False),

        ({1: 'x', 2: 'x', 3: 'x',
          4: None, 5: None, 6: None,
          7: None, 8: None, 9: None, }, True),
        ({1: None, 2: None, 3: None,
          4: 'x', 5: 'x', 6: 'x',
          7: None, 8: None, 9: None, }, True),
        ({1: None, 2: None, 3: None,
          4: None, 5: None, 6: None,
          7: 'x', 8: 'x', 9: 'x', }, True),
        ({1: 'x', 2: None, 3: None,
          4: 'x', 5: None, 6: None,
          7: 'x', 8: None, 9: None, }, True),
        ({1: None, 2: 'x', 3: None,
          4: None, 5: 'x', 6: None,
          7: None, 8: 'x', 9: None, }, True),
        ({1: None, 2: None, 3: 'x',
          4: None, 5: None, 6: 'x',
          7: None, 8: None, 9: 'x', }, True),
        ({1: 'x', 2: None, 3: None,
          4: None, 5: 'x', 6: None,
          7: None, 8: None, 9: 'x', }, True),
        ({1: None, 2: None, 3: 'x',
          4: None, 5: 'x', 6: None,
          7: 'x', 8: None, 9: None, }, True),

        ({1: 'o', 2: 'o', 3: 'o',
          4: None, 5: None, 6: None,
          7: None, 8: None, 9: None, }, True),
        ({1: None, 2: None, 3: None,
          4: 'o', 5: 'o', 6: 'o',
          7: None, 8: None, 9: None, }, True),
        ({1: None, 2: None, 3: None,
          4: None, 5: None, 6: None,
          7: 'o', 8: 'o', 9: 'o', }, True),
        ({1: 'o', 2: None, 3: None,
          4: 'o', 5: None, 6: None,
          7: 'o', 8: None, 9: None, }, True),
        ({1: None, 2: 'o', 3: None,
          4: None, 5: 'o', 6: None,
          7: None, 8: 'o', 9: None, }, True),
        ({1: None, 2: None, 3: 'o',
          4: None, 5: None, 6: 'o',
          7: None, 8: None, 9: 'o', }, True),
        ({1: 'o', 2: None, 3: None,
          4: None, 5: 'o', 6: None,
          7: None, 8: None, 9: 'o', }, True),
        ({1: None, 2: None, 3: 'o',
          4: None, 5: 'o', 6: None,
          7: 'o', 8: None, 9: None, }, True),

        ({1: 'o', 2: 'x', 3: 'o',
          4: None, 5: None, 6: None,
          7: None, 8: None, 9: None, }, False),
        ({1: None, 2: None, 3: None,
          4: 'x', 5: 'x', 6: 'o',
          7: None, 8: None, 9: None, }, False),
        ({1: None, 2: None, 3: None,
          4: None, 5: None, 6: None,
          7: 'o', 8: 'o', 9: 'x', }, False),
        ({1: 'o', 2: None, 3: None,
          4: 'x', 5: None, 6: None,
          7: 'o', 8: None, 9: None, }, False),
        ({1: None, 2: 'o', 3: None,
          4: None, 5: 'o', 6: None,
          7: None, 8: 'x', 9: None, }, False),
        ({1: None, 2: None, 3: 'o',
          4: None, 5: None, 6: 'x',
          7: None, 8: None, 9: 'o', }, False),
        ({1: 'o', 2: None, 3: None,
          4: None, 5: 'x', 6: None,
          7: None, 8: None, 9: 'o', }, False),
        ({1: None, 2: None, 3: 'x',
          4: None, 5: 'o', 6: None,
          7: 'o', 8: None, 9: None, }, False),

        ({1: 'o', 2: 'x', 3: 'o',
          4: None, 5: 'x', 6: None,
          7: None, 8: 'x', 9: None, }, True),

        ({1: None, 2: None, 3: None,
          4: 'x', 5: 'x', 6: 'o',
          7: 'x', 8: '0', 9: None, }, False),

        ({1: None, 2: 'x', 3: None,
          4: None, 5: None, 6: None,
          7: 'o', 8: 'o', 9: 'x', }, False),

        ({1: 'o', 2: None, 3: 'x',
          4: 'x', 5: 'x', 6: None,
          7: 'o', 8: None, 9: 'x', }, False),

        ({1: None, 2: 'o', 3: None,
          4: 'o', 5: 'o', 6: None,
          7: None, 8: 'x', 9: None, }, False),

        ({1: 'o', 2: None, 3: 'o',
          4: 'o', 5: 'o', 6: 'x',
          7: None, 8: None, 9: 'o', }, True),

        ({1: 'o', 2: 'o', 3: 'o',
          4: 'x', 5: 'x', 6: None,
          7: 'x', 8: 'x', 9: 'o', }, True),

        ({1: 'x', 2: 'o', 3: 'x',
          4: 'x', 5: 'o', 6: 'o',
          7: 'o', 8: 'x', 9: 'o', }, False),
    ]
)
def test_check_winner(test_dictionary, answer):
    test_game.game_board = test_dictionary
    assert test_game.check_winner() == answer


if __name__ == "__main__":
    pytest.main()
