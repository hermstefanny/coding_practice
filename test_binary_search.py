from typing import List

my_array = [1, 3, 5, 7]


def my_binary_search(
    in_array: List[int], target: int, begin_index: int, end_index: int
):
    if begin_index > end_index:
        return begin_index
    first_node = (end_index + begin_index) // 2
    if in_array[first_node] == target:
        return first_node
    elif in_array[first_node] < target:
        begin_index = first_node + 1
        return my_binary_search(my_array, target, begin_index, end_index)
    elif in_array[first_node] > target:
        end_index = first_node - 1
        return my_binary_search(my_array, target, begin_index, end_index)


begin_index = 0
end_index = len(my_array) - 1

assert my_binary_search(my_array, 3, begin_index, end_index) == 1
assert my_binary_search(my_array, 7, begin_index, end_index) == 3
assert my_binary_search(my_array, 0, begin_index, end_index) == 0
assert my_binary_search(my_array, 9, begin_index, end_index) == 4
assert my_binary_search(my_array, 4, begin_index, end_index) == 2
