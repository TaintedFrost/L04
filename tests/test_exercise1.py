import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def is_even(n):
    """true for even numbers"""
    return n % 2 == 0


def rectangle_area(width, height):
    """area of a rectangle."""
    return width * height  # Fixed: was +, should be *


def double(n):
    """twice the number n"""
    return n + n  # Fixed: was + 2, should be + n


# bug report 2
def is_even(n):
    """true for even numbers"""
    return n % 2 == 1


def rectangle_area(width, height):
    """area of a rectangle."""
    return width * height


def double(n):
    """twice the number n"""
    return n + 2


# bug report 3
double(5)  # returns 7, but should return 10
