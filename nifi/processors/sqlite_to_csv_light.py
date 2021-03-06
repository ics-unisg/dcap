#!/usr/bin/python3

"""Reads the sqlite data for lhipa

For every user it will read the past minute of 
eye tracker data form sqlite and pass it forward to lhipa
"""

__author__ = "Martin Eigenmann"
__license__ = "unlicence"
__version__ = "0.0.1"
__email__ = "martin.eigenmann@unisg.ch"
__status__ = "Prototpye"

import sqlite3
import os 

first = True
for f in os.listdir('/data'):
    if len(f.split('-')) == 1:
        db = sqlite3.connect(f'/data/{f}')
        cursor = db.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='et'")

        if cursor.fetchone()[0]==1:
            cursor.execute("SELECT timestamp from et ORDER BY timestamp DESC LIMIT 1")

            timestamp = cursor.fetchone()[0]
            lower_bound = timestamp - 1 * 60 * 1000 # The past 60000 milliseconds

            cursor.execute("SELECT timestamp, left, right, study, subject from et where timestamp >= ? AND timestamp <= ? ORDER BY timestamp asc", (lower_bound, timestamp))
            data = [entry for entry in cursor.fetchall()]

            if len(data) > 2:
                if first:
                    first = False
                else:
                    print("---split---")
                print('timestamp,diameter_left,diameter_right,study,subject')
                for (timestamp, left, right, study, subject) in data:
                    print(f'{timestamp},{left},{right},{study},{subject}')

                
            db.close()