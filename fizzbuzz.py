def fizzbuzz(limit):
    for i in range(limit + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        else:
            if i % 5 == 0:
                print("Buzz")
            else:
                print(i)


def main():
    fizzbuzz(100)


if __name__ == "__main__":
    main()
