def is_even(n):
    """true for even numbers"""
    return n % 2 == 0


def rectangle_area(width, height):
    """area of a rectangle."""
    return width * height  # Fixed: was +, should be *


def double(n):
    """twice the number n"""
    return n + n  # Fixed: was + 2, should be + n