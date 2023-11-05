
clean_array = []

def sum_nested_arrays(array, clean_array):
    for item in array:
        if isinstance(item, list):
            sum_nested_arrays(item, clean_array)
        else:
            clean_array.append(item)
    return clean_array


def main():
    result = sum_nested_arrays([1, 1, 1, [3, 4, [8]], [5]], clean_array)
    print(sum(result))


if __name__ == "__main__":
    main()
