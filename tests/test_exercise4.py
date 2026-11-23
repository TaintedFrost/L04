import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_admin_password_is_not_in_the_code():
    assert ADMIN_PASSWORD != "admin123"


# bug report 2
def test_r2_find_user_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('alice', 'pass123')")
    assert find_user(db, "admin' OR '1'='1") is None
