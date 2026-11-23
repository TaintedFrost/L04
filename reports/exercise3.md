# Bug reports for exercise3.py

Line: 3
Problem: The docstring says an empty list has average 0, but the code crashes on an empty list because len(numbers) is 0.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The docstring says "" if the text is empty, but the code returns the first word of an empty split, which crashes on an empty text.
Example: first_word("") raises IndexError, expected "".
Fix: return text.split()[0] if text else ""

Line: 12
Problem: The docstring says the result is 0 if total is 0, but the code divides by total, which causes a division by zero.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total else 0
