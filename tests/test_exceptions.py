import pytest

from game_xo import exceptions


@pytest.mark.parametrize('item, answer', [('1', 1),
                                          ('2', 2),
                                          ('3', 3),
                                          ('4', 4),
                                          ('5', 5),
                                          ('6', 6),
                                          ('7', 7),
                                          ('8', 8),
                                          ('9', 9),
                                          (1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5),
                                          (6, 6),
                                          (7, 7),
                                          (8, 8),
                                          (9, 9),
                                          ('1.0', None),
                                          ('', None),
                                          (' ', None),
                                          ('  ', None),
                                          ('q', None),
                                          ('qw', None),
                                          ('qwe', None),
                                          ('q1', None),
                                          ('qw1', None),
                                          ('qwe3', None)])
def test_validate_input(item, answer):
    assert exceptions.custom_ValueError(item) == answer


test_dictionary = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}


@pytest.mark.parametrize('item, answer', [(1, True),
                                          (2, True),
                                          (3, True),
                                          (4, True),
                                          (5, True),
                                          (6, True),
                                          (7, True),
                                          (8, True),
                                          (9, True),
                                          (0, False),
                                          (-1, False),
                                          (10, False),
                                          (2.1, False),
                                          (10 / 3, False),
                                          ('1.0', False),
                                          ('', False),
                                          (' ', False),
                                          ('  ', False),
                                          ('q', False),
                                          ('qw', False),
                                          ('qwe', False),
                                          ('q1', False),
                                          ('qw1', False),
                                          ('qwe3', False)])
def test_find_in_dict(item, answer):
    assert exceptions.custom_KeyError(item, test_dictionary) == answer


if __name__ == "__main__":
    pytest.main()
