#! /usr/bin/env python3

import sqlite3
import hashlib
import random
from argparse import ArgumentParser

# connect to the passwdb file which contains the database for user access.
# if the file doesn't exist yet, it's created in the current repository


# global variables

conn = None
cursor = None

# function to open database or create it if it doens't exist yet


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('passw.db')
    cursor = conn.cursor()

# this tries to create a new database

    try:
        cursor.execute('''CREATE TABLE users
                      (username CHAR(256),
                       digest CHAR(256),
                       salt CHAR(256),
                       PRIMARY KEY (username))''')
        conn.commit()

# exception: database already exists

    except sqlite3.OperationalError:
        return

# define arguments for usage


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-a', '--add', help="add a usernamename (requires -p)")
    parser.add_argument('-p', '--password', help="the username password",
                        required=True)
    parser.add_argument('-d', '--delete', help="delete a user (requires -p)")
    parser.add_argument('-m', '--modify',
                        help='''modify a user's username (requires -p and -nu)
                             or password (requires -p and -np)''')
    parser.add_argument('-nu', '--newusername', help="new username")
    parser.add_argument('-np', '--newpassword', help="new password")
    return parser.parse_args()


def save_new_user(username, password):
    global conn
    global cursor

# add salt to each new user to compute password hash

    salt = str(random.random())
    digest = salt + password

# hash is computed 100000 times repeatedly

    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    row = cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    conn.commit()

# checks if username is already in use

    results = row.fetchall()
    if results:
        print("username already in use. please choose another one")
    else:
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                       (username, digest, salt))
        conn.commit()
        print ("user {} succesfully added".format(username))

# function used for checking username and password


def check_for_user(username, password):
    global conn
    global cursor

# first of all, get salt from username (if this exists)

    salt = cursor.execute("SELECT salt FROM users WHERE username=?",
                          (username,))
    salt = salt.fetchall()
    if salt == []:
        print ("username doesn't exist")
        quit()

# compute the hash with password inserted + salt retrieved from database

    salt = salt[0][0]
    digest = salt + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

# check whether digests correspond

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

# first check username and password

    check_digest = check_for_user(username, password)

# check if new username is already in use

    row = cursor.execute(
        "SELECT * FROM users WHERE username=?", (newusername,))
    conn.commit()
    results = row.fetchall()
    if results:
        print("username already in use. please choose another one")

# modify username

    else:
        cursor.execute('''UPDATE users
                          SET username =?
                          WHERE username=? AND digest=?''',
                       (newusername, username, check_digest))
        conn.commit()
        print ("username modified succesfully into", newusername)


def modify_pw(username, password, newpw):
    global conn
    global cursor

# first check username and password

    check_digest = check_for_user(username, password)

# compute new digest

    salt = cursor.execute("SELECT salt FROM users WHERE username=?",
                          (username,))
    salt = salt.fetchall()[0][0]
    new_digest = salt + newpw
    for i in range(100000):
        new_digest = hashlib.sha256(new_digest.encode('utf-8')).hexdigest()

# save new password (digest)

    cursor.execute('''UPDATE users
                          SET digest =?
                          WHERE username=?''',
                   (new_digest, username))
    conn.commit()
    print ("password modified succesfully into", newpw)


def delete_username(username, password):
    global conn
    global cursor

# first check username and password

    check_digest = check_for_user(username, password)

# delete user

    cursor.execute('''DELETE FROM users
                          WHERE username=? AND digest=?''',
                   (username, check_digest))
    conn.commit()
    print ("user deleted")

# calling right functions at the right time


if __name__ == "__main__":
    open_and_create()
    args = parse_args()
    if args.add and args.password:
        save_new_user(args.add, args.password)
    elif args.modify and args.password and args.newusername:
        modify_username(args.modify, args.password, args.newusername)
    elif args.delete and args.password:
        delete_username(args.delete, args.password)
    elif args.modify and args.password and args.newpassword:
        modify_pw(args.modify, args.password, args.newpassword)
    else:
        print ("wrong usage")
    conn.close()

# code for printing database, useful for debugging
'''username = args.a
rows = cursor.execute("SELECT * FROM users WHERE username=?",
                      (username,))
results = rows.fetchall()
print (results)'''
