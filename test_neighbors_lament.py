import neighbors_lament
import pytest

# take an integer as input, and output the largest integer below that uses the same digits.
# example: input 53442, output is 53424
# 34278 -> 32874

def test_valid_neighbor_too_small():
    assert(neighbors_lament.lesser_neighbor(9)) == None

def test_valid_neighbor_for_small_numbers():
    assert(neighbors_lament.lesser_neighbor(10)) == 1
    assert(neighbors_lament.lesser_neighbor(11)) == None
    assert(neighbors_lament.lesser_neighbor(12)) == None
    assert(neighbors_lament.lesser_neighbor(19)) == None
    assert(neighbors_lament.lesser_neighbor(20)) == 2
    assert(neighbors_lament.lesser_neighbor(21)) == 12 
    assert(neighbors_lament.lesser_neighbor(22)) == None

def test_valid_neighbor_nothing_lower():
    assert(neighbors_lament.lesser_neighbor(11)) == None
    assert(neighbors_lament.lesser_neighbor(999)) == None
    assert(neighbors_lament.lesser_neighbor(123456789)) == None
    assert(neighbors_lament.lesser_neighbor(1122)) == None

def test_valid_neighbor_case_1():
    assert(neighbors_lament.lesser_neighbor(9998)) == 9989

def test_valid_neighbor_case_2():
    assert(neighbors_lament.lesser_neighbor(53442)) == 53424

def test_valid_neighbor_case_3():
    assert(neighbors_lament.lesser_neighbor(34278)) == 32874

def test_swap_value_i_with_next_highest_value():
    assert(neighbors_lament.swap_value_i_with_next_highest_value([5,1,2,3,4], 0)) == [4,1,2,3,5]
    assert(neighbors_lament.swap_value_i_with_next_highest_value([5,1,2,4,3], 0)) == [4,1,2,5,3]
    assert(neighbors_lament.swap_value_i_with_next_highest_value([5,4,2,4,1], 2)) == [5,4,1,5,2]
    assert(neighbors_lament.swap_value_i_with_next_highest_value([9,9,8,9,9], 0)) == [8,9,9,9,9]
    assert(neighbors_lament.swap_value_i_with_next_highest_value([9,9,8,8,9], 1)) == [9,8,9,8,9]
    assert(neighbors_lament.swap_value_i_with_next_highest_value([1,1,2,3,4], 0)) == None
    assert(neighbors_lament.swap_value_i_with_next_highest_value([1,1,2], 0)) == None
