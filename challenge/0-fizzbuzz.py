#!/usr/bin/python3
import sys


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            s = "FizzBuzz"
        elif i % 3 == 0:
            s = "Fizz"
        elif i % 5 == 0:
            s = "Buzz"
        else:
            s = str(i)

        if i != n:
            print(s, end=" ")
        else:
            print(s, end="")
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            max_n = int(sys.argv[1])
        except ValueError:
            print("Usage: ./0-fizzbuzz.py <number>")
            sys.exit(1)
    else:
        max_n = 100

    fizzbuzz(max_n)

