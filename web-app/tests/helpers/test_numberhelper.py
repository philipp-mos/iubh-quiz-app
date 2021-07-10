import pytest

from src.helpers.NumberHelper import NumberHelper


@pytest.mark.parametrize(
    'character,expected',
    [
        pytest.param('A', 1),
        pytest.param('a', 1),
        pytest.param('B', 2),
        pytest.param('b', 2),
        pytest.param('C', 3),
        pytest.param('D', 4),
        pytest.param('E', 5),
        pytest.param('f', 6),
        pytest.param('Z', 26),
        pytest.param('z', 26)
    ]
)
def test_convert_char_to_number(character, expected):
    converted = NumberHelper.convert_from_char_to_number(character)

    assert converted == expected


@pytest.mark.parametrize(
    'number,to_upper,expected',
    [
        pytest.param(1, True, 'A'),
        pytest.param(1, False, 'a'),
        pytest.param(2, True, 'B'),
        pytest.param(2, False, 'b'),
        pytest.param(26, True, 'Z'),
        pytest.param(26, False, 'z')
    ]
)
def test_convert_number_to_char(number, to_upper, expected):
    converted = NumberHelper.convert_from_number_to_char(number, to_upper)

    assert converted == expected
