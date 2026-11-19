# Bug reports for exercise2.py

Line: 13
Problem: clamp incorrectly uses min(x, low) and max(low, min(x, low)), which results in x being clamped to low or below, not to the range from low to high.
Example: clamp(3, 1, 10) returns 1, expected 3.
Fix: return max(low, min(x, high))
