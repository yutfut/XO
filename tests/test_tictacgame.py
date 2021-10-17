import pytest

from game.game_xo import TicTacGame

test_game = TicTacGame()


@pytest.mark.parametrize(
    "test_dictionary, answer",
    [
        (test_game.game_board, False),
        (
            {
                1: "x", 2: "x", 3: "x",
                4: None, 5: None, 6: None,
                7: None, 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: "x", 5: "x", 6: "x",
                7: None, 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: None, 5: None, 6: None,
                7: "x", 8: "x", 9: "x",
            },
            True,
        ),
        (
            {
                1: "x", 2: None, 3: None,
                4: "x", 5: None, 6: None,
                7: "x", 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: "x", 3: None,
                4: None, 5: "x", 6: None,
                7: None, 8: "x", 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: "x",
                4: None, 5: None, 6: "x",
                7: None, 8: None, 9: "x",
            },
            True,
        ),
        (
            {
                1: "x", 2: None, 3: None,
                4: None, 5: "x", 6: None,
                7: None, 8: None, 9: "x",
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: "x",
                4: None, 5: "x", 6: None,
                7: "x", 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: "o", 2: "o", 3: "o",
                4: None, 5: None, 6: None,
                7: None, 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: "o", 5: "o", 6: "o",
                7: None, 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: None, 5: None, 6: None,
                7: "o", 8: "o", 9: "o",
            },
            True,
        ),
        (
            {
                1: "o", 2: None, 3: None,
                4: "o", 5: None, 6: None,
                7: "o", 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: "o", 3: None,
                4: None, 5: "o", 6: None,
                7: None, 8: "o", 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: "o",
                4: None, 5: None, 6: "o",
                7: None, 8: None, 9: "o",
            },
            True,
        ),
        (
            {
                1: "o", 2: None, 3: None,
                4: None, 5: "o", 6: None,
                7: None, 8: None, 9: "o",
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: "o",
                4: None, 5: "o", 6: None,
                7: "o", 8: None, 9: None,
            },
            True,
        ),
        (
            {
                1: "o", 2: "x", 3: "o",
                4: None, 5: None, 6: None,
                7: None, 8: None, 9: None,
            },
            False,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: "x", 5: "x", 6: "o",
                7: None, 8: None, 9: None,
            },
            False,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: None, 5: None, 6: None,
                7: "o", 8: "o", 9: "x",
            },
            False,
        ),
        (
            {
                1: "o", 2: None, 3: None,
                4: "x", 5: None, 6: None,
                7: "o", 8: None, 9: None,
            },
            False,
        ),
        (
            {
                1: None, 2: "o", 3: None,
                4: None, 5: "o", 6: None,
                7: None, 8: "x", 9: None,
            },
            False,
        ),
        (
            {
                1: None, 2: None, 3: "o",
                4: None, 5: None, 6: "x",
                7: None, 8: None,  9: "o",
            },
            False,
        ),
        (
            {
                1: "o", 2: None, 3: None,
                4: None, 5: "x", 6: None,
                7: None, 8: None, 9: "o",
            },
            False,
        ),
        (
            {
                1: None, 2: None, 3: "x",
                4: None, 5: "o", 6: None,
                7: "o", 8: None, 9: None,
            },
            False,
        ),
        (
            {
                1: "o", 2: "x", 3: "o",
                4: None, 5: "x", 6: None,
                7: None, 8: "x", 9: None,
            },
            True,
        ),
        (
            {
                1: None, 2: None, 3: None,
                4: "x", 5: "x", 6: "o",
                7: "x", 8: "0", 9: None,
            },
            False,
        ),
        (
            {
                1: None, 2: "x", 3: None,
                4: None, 5: None, 6: None,
                7: "o", 8: "o", 9: "x",
            },
            False,
        ),
        (
            {
                1: "o", 2: None, 3: "x",
                4: "x", 5: "x", 6: None,
                7: "o", 8: None, 9: "x",
            },
            False,
        ),
        (
            {
                1: None, 2: "o", 3: None,
                4: "o", 5: "o", 6: None,
                7: None, 8: "x", 9: None,
            },
            False,
        ),
        (
            {
                1: "o", 2: None, 3: "o",
                4: "o", 5: "o", 6: "x",
                7: None, 8: None, 9: "o",
            },
            True,
        ),
        (
            {
                1: "o", 2: "o", 3: "o",
                4: "x", 5: "x", 6: None,
                7: "x", 8: "x", 9: "o",
            },
            True,
        ),
        (
            {
                1: "x", 2: "o", 3: "x",
                4: "x", 5: "o", 6: "o",
                7: "o", 8: "x", 9: "o",
            },
            False,
        ),
    ],
)
def test_check_winner(test_dictionary, answer):
    test_game.game_board = test_dictionary
    assert test_game.check_winner() == answer


@pytest.mark.parametrize(
    "test_dictionary, item, symbol, answer",
    [
        (test_game.game_board, 1, 'x', True),
        (test_game.game_board, 1, 'x', False),
        (test_game.game_board, 1, 'o', False),
        (test_game.game_board, 2, 'x', True),
        (test_game.game_board, 2, 'x', False),
        (test_game.game_board, 2, 'o', False),
        (test_game.game_board, 3, 'x', True),
        (test_game.game_board, 3, 'x', False),
        (test_game.game_board, 3, 'o', False),
        (test_game.game_board, 4, 'x', True),
        (test_game.game_board, 4, 'x', False),
        (test_game.game_board, 4, 'o', False),
        (test_game.game_board, 5, 'x', True),
        (test_game.game_board, 5, 'x', False),
        (test_game.game_board, 5, 'o', False),
        (test_game.game_board, 6, 'x', True),
        (test_game.game_board, 6, 'x', False),
        (test_game.game_board, 6, 'o', False),
        (test_game.game_board, 7, 'x', True),
        (test_game.game_board, 7, 'x', False),
        (test_game.game_board, 7, 'o', False),
        (test_game.game_board, 8, 'x', True),
        (test_game.game_board, 8, 'x', False),
        (test_game.game_board, 8, 'o', False),
        (test_game.game_board, 9, 'x', True),
        (test_game.game_board, 9, 'x', False),
        (test_game.game_board, 9, 'o', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 1, 'o', True),
        (test_game.game_board, 1, 'o', False),
        (test_game.game_board, 1, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 2, 'o', True),
        (test_game.game_board, 2, 'o', False),
        (test_game.game_board, 2, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 3, 'o', True),
        (test_game.game_board, 3, 'o', False),
        (test_game.game_board, 3, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 4, 'o', True),
        (test_game.game_board, 4, 'o', False),
        (test_game.game_board, 4, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 5, 'o', True),
        (test_game.game_board, 5, 'o', False),
        (test_game.game_board, 5, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 6, 'o', True),
        (test_game.game_board, 6, 'o', False),
        (test_game.game_board, 6, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 7, 'o', True),
        (test_game.game_board, 7, 'o', False),
        (test_game.game_board, 7, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 8, 'o', True),
        (test_game.game_board, 8, 'o', False),
        (test_game.game_board, 8, 'x', False),
        ({
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            }, 9, 'o', True),
        (test_game.game_board, 9, 'o', False),
        (test_game.game_board, 9, 'x', False)
    ]
)
def test_validate_input(test_dictionary, symbol, item, answer):
    test_game.game_board = test_dictionary
    assert test_game.validate_input(symbol, item) == answer


if __name__ == '__main__':
    pytest.main()
