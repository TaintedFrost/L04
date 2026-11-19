# Bug reports for exercise2.py

Line: 3
Problem: The function checks if the grade is greater than 5, but the docstring says "5 or more", which means it should include 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The function requires at least 8 characters but uses > 8, which excludes passwords of exactly 8 characters.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The clamp function incorrectly uses min(x, low) and max(low, min(x, low)), which results in x being clamped to low regardless of high.
Example: clamp(10, 5, 15) returns 5, expected 10.
Fix: return max(low, min(x, high))
