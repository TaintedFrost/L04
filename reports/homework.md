# Bug reports for homework.py

Line: 3
Problem: The docstring says n to the power of 3, but the code multiplies n by 3 instead of raising it to the power of 3.
Example: cube(2) returns 6, expected 8.
Fix: return n ** 3

Line: 8
Problem: The docstring says 120 cm or more, which means 120 or above, but the code uses > so it excludes 120.
Example: can_ride(120) returns False, expected True.
Fix: return height_cm >= 120

Line: 23
Problem: The docstring says "FizzBuzz if n is divisible by 15", but the code checks n % 15 == 0 after checking n % 3 == 0 and n % 5 == 0, which means it will never return "FizzBuzz" because if n is divisible by 15, it is also divisible by 3 and 5, so the earlier conditions will catch it and return "Fizz" or "Buzz" instead.
Example: fizzbuzz(15) returns "Fizz", expected "FizzBuzz".
Fix: if n % 15 == 0:
return "FizzBuzz"

Line: 31
Problem: The docstring says the median of a non-empty list, and for an even number of values, the average of the two middle values. The code returns only the middle value when the list has an odd number of elements, but for even, it returns only one of the two middle values, not their average.
Example: median([1, 2, 3, 4]) returns 3, expected 2.5.
Fix: return (s[mid-1] + s[mid]) / 2 if len(s) % 2 == 0 else s[mid]
