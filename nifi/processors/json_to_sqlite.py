#!/usr/bin/python3

"""Stores data in sqlite per user.

Reads stdin json data and stores that in a local sqlite.
This sqlite file is different per study-subject combination
"""

__author__ = "Martin Eigenmann"
__license__ = "unlicence"
__version__ = "0.0.1"
__email__ = "martin.eigenmann@unisg.ch"
__status__ = "Prototpye"

import json
import sys
import hashlib
import sqlite3

for line in sys.stdin:
    data = json.loads(line)
    name = hashlib.sha256("".join([data['study'], data['subject']]).encode('utf-8'))
    db = sqlite3.connect(f'/data/{name.hexdigest()}.db')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS et (id INTEGER PRIMARY KEY, ingres_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, timestamp INTEGER, left FLOAT, right FLOAT, type STRING, subject STRING, study STRING)')
    cursor.execute('INSERT INTO et (timestamp, left, right, type, subject, study) VALUES (?,?,?,?,?,?)', (data['timestamp'], data['diameter']['left'], data['diameter']['right'], data['type'], data['subject'], data['study']))

db.commit()
cursor.close()
db.close()