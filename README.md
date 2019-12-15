# ```capitals``` introduction

The basic function of this library is to obtain the capital or country name of any European State. 
Using optional parameter you may also be able to:
- change the verbosity level;
- choose a different .csv file from which the library obtains capitals/countries information;
- request some additional information, obtained through an API request: country's population, area (KM^2), languages and currencies;
- have the information returned for storing instead of printed.

# Getting started

First things first.

The library supports a login function, therefore you will need to input a valid username and password every time you execute.
To setup username and password, you will need ```scripts/dbmanager.py```.

# ```dbmanager.py```: setting up users and passwords

Always call ```dbmanager.py``` from the ```capitals``` repository. this will enable you to:
- add a new username with a password
- modify existing usernames or passwords
- delete a username

Helper:

```[12/15/19]seed@VM:~/.../capitals$ scripts/dbmanager.py -h
usage: dbmanager.py [-h] [-a ADD] -p PASSWORD [-d DELETE] [-m MODIFY]
                    [-nu NEWUSERNAME] [-np NEWPASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -a ADD, --add ADD     add a usernamename (requires -p)
  -p PASSWORD, --password PASSWORD
                        the username password
  -d DELETE, --delete DELETE
                        delete a user (requires -p)
  -m MODIFY, --modify MODIFY
                        modify a user's username (requires -p and -nu) or
                        password (requires -p and -np)
  -nu NEWUSERNAME, --newusername NEWUSERNAME
                        new username
  -np NEWPASSWORD, --newpassword NEWPASSWORD
                        new password
```

Usage example:

```[12/15/19]seed@VM:~/.../capitals$ scripts/dbmanager.py -a user -p pass
user user succesfully added
[12/15/19]seed@VM:~/.../capitals$ scripts/dbmanager.py -m user -p pass -nu username
username modified succesfully into username
[12/15/19]seed@VM:~/.../capitals$ scripts/dbmanager.py -m username -p pass -np password
password modified succesfully into password
[12/15/19]seed@VM:~/.../capitals$ scripts/dbmanager.py -d username -p password
user deleted
```

Notice that:
- strigs will be saved as strings;
- if you want to use numbers, please ensure they are within "";
- password argument is always required;
- write your username after arguments -a, -m and -d;
- you cannot add two user with identical username;
- remember to run the command from ```capitals``` repository.

All users and their passowords are saved in ```passw.db``` file, in ```capitals``` repository.
Passwords are stored as digests, computer with a salt (unique for each user) plus hash repetition for improved security.

# ```capitalspackage``` library 

This library is used in ```userapp.py``` but may also used for your personal project.

importing: 
```from capitalspackage import checks```

usage: 
- ```checks.load_csv(filename)``` pass path of .csv file to be loaded
- ```checks.check_capital(checklist, args)``` pass dictionary containing capitals and countries and args from user
- ```checks.check_state(checklist, args)``` pass dictionary containing capitals and countries and args from user
- ```checks.get_country_data(base_url, countryname, args)``` pass base url of API, 
     name of country to fetch data about, and args from user

Refer to ```userapp.py``` section for additional information about the what the functions do.

#```userapp.py```: main application for final user

Start using this app after you set up at least one user with bdmanager.py.

This is the main application, intended for the final user.

Helper:

```[12/15/19]seed@VM:~/.../capitals$ userapp.py -h
usage: userapp.py [-h] [-p PASSWORD] [-u USERNAME] [-v] [-r] [-c CHOOSECSV]
                  [-e]
                  name

positional arguments:
  name                  write name of European country or capital

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        user's password (required)
  -u USERNAME, --username USERNAME
                        username (required)
  -v, --verbosity       incrementally increase output verbosity up to -vv
  -r, --returnr         returns result to store it, instead of printing it
  -c CHOOSECSV, --choosecsv CHOOSECSV
                        specify another csv file to use. make sure the format
                        is CHINA;PECHINO/nGIAPPONE;TOKYO
  -e, --extrainfo       incrementally prints or returns (with -r) extra
                        information about the country: population, area,
                        currencies, languages
```

Notice that:
- a valid username and password is always required;
- the name of a country or capital is required as well;
- you can change the verbosity of the output with ```-v``` for a maximum level of ```-vv```;
- you can ask to have returned the results instead of printing them, in case you'd like to store them for further usage;
- you can choose a different ```.csv``` file from which to load the country/capital information. You need to insert the path of the file. To
  avoid errors, make sure the ```.csv``` file is compliant with the following format: ```CHINA;PECHINO/nGIAPPONE;TOKYO```. No header is
  needed.
  With this option you can potentially expand the usage of the library to include all countries of the world;
- extrainfo calls a functions using an API to retrieve information from the REST Countries databases. The information is available not
  only for european countries but for all REST Countries. Extra information provided:
  - ```'-e'``` population
  - ```'-ee'``` population + area in squared kilometers
  - ```'-eee'``` population + area in squared kilometers + list of curriences used
  - ```'-eeee'``` population + area in squared kilometers + list of curriences used + list of languages spoken


Usage example:
``` [12/15/19]seed@VM:~/.../capitals$ userapp.py -u user -p 123 rome -r -v -eeee
Returning ITALY, the state which capital is ROME
returning list with population, area (km^2),
                           currencies list and languages list of ITALY
[60665551, 301336.0, ['Euro'], ['Italian']]```

# tests

In the folder ```tests``` you may find the ```tests_userapp.py``` used to make test on the right funcitoning of the function ```load_csv```

In the ```setUp```, we have created three temporary files, in a secure manner, using ```tempfile``` library.

We are then running a smoke test using a valid ```.csv``` file, a test using a file with a wrong format, and a test using an empty file.

The function ```load_csv``` handles all the exceptions correctly.

Usage:

```[12/15/19]seed@VM:~/.../capitals$ python3 -m unittest -v -b tests/tests_userapp.py
test_empty_datafile (tests.tests_userapp.TestMain) ... ok
test_right_datafile (tests.tests_userapp.TestMain) ... ok
test_wrong_format_datafile (tests.tests_userapp.TestMain) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK```


This is all you need to know. If you find any bug or issues please report them with a new issue.

This project was done by ENEA groupwork for an exam "Lab of Web Software Development".
Contributors: Dal Monico Massimo, Fontana Leonardo, Malvestio Adalberto, Rogante Elena, Weatherley Sara.
