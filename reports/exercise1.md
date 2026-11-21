# Bug reports for exercise1.py

Line: 3
Problem: The function checks if n modulo 2 equals 1, which is true for odd numbers, not even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but the area of a rectangle is width times height.
Example: rectangle_area(4, 5) returns 9, expected 20.
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but it should return twice the number, i.e., n multiplied by 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
