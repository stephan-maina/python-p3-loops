Control Flow: Loops
This README provides a brief overview of the control flow constructs related to loops in Python, along with some key vocabulary and practical examples.

Basic Loops in Python
While Loop
A while loop in Python repeatedly executes a block of code as long as a given condition is True.

python
Copy code
i = 0
while i < 5:
    print("Looping!")
    i += 1
For Loop
A for loop in Python is used to iterate over an iterable (e.g., list, tuple, range) and execute a block of code for each item.

python
Copy code
for i in range(10):
    print("Looping!")
    print(f"i is: {i}")
List Comprehensions
List comprehensions provide a concise way to create lists by applying an expression to each item in an existing iterable.

python
Copy code
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008]
inch_heights = [height * 7920 for height in player_heights]
Practice
In the provided looping.py file, you can practice writing Python code for the following tasks:

Create a function happy_new_year() that counts down from 10 to 1 and then prints "Happy New Year!"
Create a function square_integers() that squares each element in a list of integers.
Implement a function fizzbuzz() that prints numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both with "FizzBuzz."
Remember to run pytest -x to check your solutions.

These exercises help you become familiar with Python's control flow constructs and list comprehensio

## Resources

- [Python For Loops](https://wiki.python.org/moin/ForLoop)
- [Python While Loops](https://wiki.python.org/moin/WhileLoop)
- [List Comprehension vs. For Loop](https://www.programiz.com/python-programming/list-comprehension)
