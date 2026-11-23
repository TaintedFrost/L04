# Bug reports for exercise2.py

Line: 3
Problem: The docstring says "5 or more", which means >= 5, but the code uses > 5, so a grade of exactly 5 is not considered passing.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring says "at least 8 characters", which means >= 8, but the code uses > 8, so a password with exactly 8 characters is rejected.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The code incorrectly clamps x by using max(low, min(x, low)), which simplifies to low when x is below or equal to low, but the inner min(x, low) is wrong — it should be min(x, high), and the max should be with high. The current code has a logical error: min(x, low) will always be low or less, then max(low, ...) will always be low, which is incorrect.
Example: clamp(10, 5, 15) returns 10, which is correct, but clamp(3, 5, 15) returns 5, which is correct — wait, actually, let's test: clamp(3, 5, 15): min(3, 5) = 3, then max(5, 3) = 5 — correct. But clamp(20, 5, 15): min(20, 5) = 5, max(5, 5) = 5 — correct. But clamp(10, 1, 5): min(10, 1) = 1, max(1, 1) = 1 — should be 5. So it fails when x is above high. The issue is that min(x, low) should be min(x, high). The current code uses low twice, which is wrong.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
