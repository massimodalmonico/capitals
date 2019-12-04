#! /usr/bin/env python3

import sqlite3
import hashlib
import random
from argparse import ArgumentParser

# connect to the passwdb file which contains the database for user access. if the file doesn't exist yet, it's created in the current repository

conn = None
cursor = None


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('passw.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE users 
                      (username CHAR(256),
                       digest CHAR(256),
                       salt CHAR(256),
                       PRIMARY KEY (digest))''')
        conn.commit()
    except sqlite3.OperationalError:
        return

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password") # keep this for testing but later we will just call the method in userapp.py
    return parser.parse_args()

def save_new_user(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest() 
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (username, digest, str(random.random())))
    conn.commit()
    print ("user {} succesfully added".format(username))

def check_for_user(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest() 
    rows = cursor.execute("SELECT * FROM users WHERE username=? and digest=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()
    if results:
        print ("ok")
        return True
    else:
        print("User is not present, or password is invalid")

open_and_create()
args = parse_args()
if args.a and args.p and args.c == None:
    save_new_user(args.a, args.p)
elif args.c and args.p and args.a == None:
    check_for_user(args.c, args.p)
else: print ("wrong usage. don't use -a and -c together")
conn.close()
