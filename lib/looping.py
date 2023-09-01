#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
   i = 10 
   while i > 1:
       i -= 1
       return ('Happy New Year!')

def square_integers(int_list):
    squared_list = [num * num for num in int_list]
    return squared_list

def fizzbuzz():
    # code goes here!
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num),
    