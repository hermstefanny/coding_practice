def numberOfSteps(num: int, steps: int) -> int:
    if num == 0:
        return steps

    if num % 2 == 0:
        steps += 1
        return numberOfSteps(num / 2, steps)

    else:
        steps += 1
        return numberOfSteps(num - 1, steps)


print(numberOfSteps(123, 0))
