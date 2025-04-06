def romanToInt(s: str) -> int:
    nums = 0
    num_array = []
    roman = [char for char in s]

    equivalence = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in roman:
        if i in equivalence.keys():
            num_array.append(equivalence[i])

    j = 1
    i = 0
    nums = 0

    while i < len(num_array):

        if j < len(num_array) and num_array[j] > num_array[i]:
            temp = num_array[j] - num_array[i]
            nums = nums + temp
            i += 1
            j += 1

        else:
            nums = nums + num_array[i]

        j += 1
        i += 1

    return nums


print(romanToInt("MCMXCIV"))
print(romanToInt("III"))
print(romanToInt("LVIII"))
