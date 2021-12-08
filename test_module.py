import pytest

from distance_rect import cg_distance, corner_distance


@pytest.mark.parametrize("tuple_args, result", [
    ((1, 2, 3, 0, 3, 4, 5, 2), 2.83),
    ((1, 2, 2, 1, 4, 5, 5, 4), 4.24),
    ((-1, -2, -3, 0, -3, -4, -5, -2), 2.83),
    ((0, 0, 0, 0, 0, 0, 0, 0), 0),
    ((1, 1, 1, 1, 1, 1, 1, 1), 0),
    ((1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9), 0.57)
])
def test_cg_distance_good(tuple_args, result):
    assert cg_distance(*tuple_args) == result


def test_type_error():
    with pytest.raises(TypeError):
        cg_distance('a', 'b', 'c', 'd', 'f', 'g', 'c', 'k')



@pytest.mark.parametrize("tuple_args, result", [
    ((1, 2, 3, 0, 3, 4, 5, 2), 5.66),
    ((1, 2, 2, 1, 4, 5, 5, 4), 8.49),
    ((-1, -2, -3, 0, -3, -4, -5, -2), 5.66),
    ((0, 0, 0, 0, 0, 0, 0, 0), 0),
    ((1, 1, 1, 1, 1, 1, 1, 1), 0),
    ((1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9), 1.13)
])
def test_cg_corner_good(tuple_args, result):
    assert corner_distance(*tuple_args) == result


def test_type_error_corner():
    with pytest.raises(TypeError):
        corner_distance('a', 'b', 'c', 'd', 'f', 'g', 'c', 'k')



