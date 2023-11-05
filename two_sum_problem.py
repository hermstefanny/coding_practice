def two_sum(number, array):
    s = []
    for i in range(len(array)):
        j = i + 1
        for j in range(len(array) - 1):
            sum = array[i] + array[j]
            if sum == number:
                s.append(f"The sum of {array[i]} and {array[j]} is {sum}")

    return s


def main():
    result = two_sum(7, [7, 0, 0, 1, 9, 5, 4, 3])
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
