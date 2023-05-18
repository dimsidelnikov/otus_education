import pytest
from src.triangle import Triangle


@pytest.mark.parametrize('a_side, b_side, c_side, expected_perimeter, expected_area',
                         [
                             (5, 5, 5, 15, 10.83),
                             (3, 4, 5, 12, 6),
                             (10, 10, 5, 25, 24.21)
                         ],
                         ids=[
                             'equilateral triangle',
                             'right triangle',
                             'isosceles triangle'
                         ])
def test_positive_create_triangle(a_side, b_side, c_side, expected_perimeter, expected_area):
    triangle = Triangle(a_side, b_side, c_side)
    assert triangle.name == 'Triangle', 'Correct name is Triangle'
    assert triangle.perimeter == expected_perimeter, f'Correct perimeter is {expected_perimeter}'
    assert triangle.area == expected_area, f'Correct area is {expected_area}'


@pytest.mark.parametrize('a_side, b_side, c_side',
                         [
                             (5, 'b_side', 5),
                             (3, 4, 0),
                             (10, 10, -5),
                             (2, 3, 6)
                         ],
                         ids=[
                             'one side is str',
                             'one side is zero',
                             'one side is negative',
                             'sum of two sides is less than thirds'
                         ])
def test_negative_create_triangle(a_side, b_side, c_side):
    with pytest.raises(ValueError):
        Triangle(a_side, b_side, c_side)


def test_sum_two_triangle_areas():
    expected_sum = 16.83
    triangle_1 = Triangle(5, 5, 5)
    triangle_2 = Triangle(3, 4, 5)
    assert triangle_1.add_area(triangle_2) == expected_sum, f'Correct sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [5, 'triangle', [1, 'two']], ids=['integer', 'str', 'list'])
def test_negative_sum_two_triangle_areas(some_other_class):
    triangle_1 = Triangle(5, 5, 5)
    with pytest.raises(ValueError):
        triangle_1.add_area(some_other_class)
