import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print N_NUMBERS random numbers
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')
    print()  # Add a newline at the end


if __name__ == '__main__':
    main()