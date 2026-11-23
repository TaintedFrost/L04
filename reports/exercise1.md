# Bug reports for exercise1.py

Line: 3
Problem: The docstring says true for even numbers, but the code returns true when n % 2 == 1, which is for odd numbers.
Example: is_even(2) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The docstring says area of a rectangle, which is width times height, but the code returns width plus height.
Example: rectangle_area(4, 5) returns 9, expected 20.
Fix: return width * height

Line: 13
Problem: The docstring says twice the number n, but the code returns n + 2, which is n increased by 2, not doubled.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
