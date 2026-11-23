import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_cube_2():
    assert cube(2) == 8


# bug report 2
def test_r2_can_ride_120():
    assert can_ride(120) == True


# bug report 3
def test_r3_fizzbuzz_15():
    assert fizzbuzz(15) == "FizzBuzz"


# bug report 4
def test_r4_median_even_list():
    assert median([1, 2, 3, 4]) == 2.5
