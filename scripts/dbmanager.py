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
                       PRIMARY KEY (username))''')
        conn.commit()
    except sqlite3.OperationalError:
        return

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)")
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password") # keep this for testing but later we will just call the method in userapp.py
    parser.add_argument('-d', help="delete a user (requires -p)")
    parser.add_argument('-m', help="modify a user's username (requires -p and -nu)")
    parser.add_argument('-nu', help="new username")
    return parser.parse_args()

def save_new_user(username, password):
    global conn
    global cursor
    salt = str(random.random())
    digest = salt + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest() 
    row = cursor.execute ("SELECT * FROM users WHERE username=?", (username,))
    conn.commit()
    results = row.fetchall()
    if results:
        print("username already in use. please choose another one")
    else:
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                       (username, digest, salt))
        conn.commit()
        print ("user {} succesfully added".format(username))
        

def check_for_user(username, password):
    global conn
    global cursor
    salt = cursor.execute("SELECT salt FROM users WHERE username=?",
                          (username,))
    salt = salt.fetchall()
    if salt == []:
        print ("username doesn't exist")
        quit()
    salt = salt[0][0]
    digest = salt + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM users WHERE username=? and digest=?",
                          (username, digest))
    results = rows.fetchall()
    if results:
        return digest
    else:
        print("invalid password")
        quit()

def modify_username(username, password, newusername):
    global conn
    global cursor
    check_digest = check_for_user(username, password)
    row = cursor.execute ("SELECT * FROM users WHERE username=?", (newusername,))
    conn.commit()
    results = row.fetchall()
    if results:
        print("username already in use. please choose another one")
    else:
        cursor.execute('''UPDATE users
                          SET username =?
                          WHERE username=? AND digest=?''',
                          (newusername, username, check_digest))
        conn.commit()
        print ("username modified succesfully into", newusername)


def delete_username(username, password):
    global conn
    global cursor
    check_digest = check_for_user(username, password)
    cursor.execute('''DELETE FROM users
                          WHERE username=? AND digest=?''',
                          (username, check_digest))
    conn.commit()
    print ("user deleted")

if __name__ == "__main__":
    open_and_create()
    args = parse_args()
    if args.a and args.p:
        save_new_user(args.a, args.p)
    elif args.c and args.p:
        check_for_user(args.c, args.p)
    elif args.m and args.p and args.nu:
        modify_username(args.m, args.p, args.nu)
    elif args.d and args.p:
        delete_username(args.d, args.p)
    else: print ("wrong usage")
    conn.close()
# part for printing database, useful for debugging
'''username = args.a
rows = cursor.execute("SELECT * FROM users WHERE username=?",
                      (username,))
results = rows.fetchall()
print (results)'''

