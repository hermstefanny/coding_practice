def prime_check(number):
    
    for i in range(number):
        if number  % (i+2) == 0:
            return False
        else:
            return True
        

def main():
    for n in range(17):
        print(f'number {n+1} is {prime_check(n+1)}')


if __name__ == "__main__":
    main()