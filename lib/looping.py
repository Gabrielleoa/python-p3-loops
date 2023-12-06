#!/usr/bin/env python3
import math

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1


happy_new_year()
print('Happy New Year!')

def square_integers(int_list):
     int_list = [math.pow(int, 2) for int in int_list]
     print(int_list)
square_integers([1,2,3,4,5])
def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
     print("FizzBuzz")
    elif(num % 3 == 0):
     print("Fizz")
    elif(num % 5 == 0) :
     print("Buzz")
    else:
     print(num)         
fizzbuzz(55)