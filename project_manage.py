# import database module
import os,csv
from database import Table
from database import DB
import sys
# define a funcion called initializing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
def initializing():
    login = []
    with open(os.path.join(__location__, 'login.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            login.append(dict(r))
    person = []
    with open(os.path.join(__location__, 'persons.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            person.append(dict(r))
    return login,person
login,person = initializing()
table1 = Table('login',login)
# define a funcion called login
def login():
    # here are things to do in this function:
    # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None
    while True:
        print("1: Login")
        print("2: Quit")
        choice = input("What is your choice? ")

        if choice == '1':
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            user_data = table1.filter(
                lambda entry: entry['username'] == username and entry['password'] == password)

            if user_data.table:
                print("Login successful.")
                print(f"ID: {user_data.table[0]['ID']}, Role: {user_data.table[0]['role']}")
                return [user_data.table[0]['ID'], user_data.table[0]['role']]
            else:
                print("Invalid username or password. Try again.")

        elif choice == '2':
            break
        else:
            print("Invalid choice. Try again.")



# define a function called exit
def exit():
    sys.exit()

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
if val and len(val) == 2:
    user_id, user_role = val
    # print(user_role)
    if user_role == 'admin':
        # Admin activities
        # print(f"Login")
        print("Performing admin activities.")
        print("Admin can Create Project or Can update all the tables there")

    elif user_role == 'student':
        # Student activities
        print("Performing student activities.")

    elif user_role == 'faculty':
        print("Performing faculty activities.")
        print("faclty Role ")
        print("See request to be a supervisor")
        print("Send accept response (for projects eventually serving as an advisor)")
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
