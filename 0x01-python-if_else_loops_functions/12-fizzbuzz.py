#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
            else i % 5 == 0:
                print("Buzz", end=" ")
                else i % 3 == 0:
                    print("Fizz", end=" ")
                else:
                    print("{:d}".format(i), end=" ")
