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

            user_data = table1.filter(lambda x: x['username'] == username and x['password'] == password)

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
Project = []
with open(os.path.join(__location__,'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        Project.append(dict(r))

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities

class Admin:
    # def __init__(self,id,project,request,approve,):
# elif val[1] = 'student':
    # see and do student related activities
    pass
class Student():
    def addproject(self,project):
        self.projectid = []
        self.projectid.append(project)
        # table1.update_row('Film', 'A Serious Man', 'Year', '2022')
    def input_pending_data(self):
        project_id = input("ID: ")
        date_str = input("to be member Group?: ")

        # แปลงวันที่จากสตริงเป็นวัตถุ datetime
        # try:
        #     date_obj = datetime.strptime(date_str, "%d/%m/%y")
        # except ValueError:
        #     print("รูปแบบวันที่ไม่ถูกต้อง")
        #     return

        # สร้าง dictionary จากข้อมูลที่รับมา
        input_data = {
            "ProjectID": project_id,
            "to_be_member": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_pending_data(input_data)
    def update_pending_data(self, input_data):
        csv_file_path = 'Member_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Response', 'no-status')
        input_data.setdefault('Response_date', '-')

        # Append the new data to existing_data
        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID","to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))


    def updateProject(self, myss):
        csv_file_path = 'Project.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        existing_data.append(myss)
        with open(csv_file_path, mode='w', newline='') as csv_file:
            # fieldnames = ["Name", "Age", "Grade"]
            fieldnames = ["ProjectID", "Project", "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def check_approve(self,id_project):
        csv_file_path = 'Member_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row['ProjectID'] == id_project]
        return rejected_projects

    def student_exists(self,student_name):
        with open("persons.csv", mode='r') as file:
            reader = csv.reader(file)
            # Check if the student name exists in the first column of the CSV file
            return any(student_name == row[1] for row in reader)
    def update_role(self, target_id, new_role):
        with open('login.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ID'] == target_id:
                row['role'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('login.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ID", "username", "password", "role"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)
    def update_student_deny(self, target_Group, new_role):
        with open('Member_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['to_be_member'] == target_Group:
                row['Response'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Member_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)
# elif val[1] = 'member':
    # see and do member related activities
fieldnames = ["ProjectID", 'Project', "Lead", "Member1", "Member2", "Advisor", 'Status']
class Member:
    pass
# elif val[1] = 'lead':
    # see and do lead related activities
class lead:
    pass
# elif val[1] = 'faculty':
    # see and do faculty related activities
class faculty:
    def input_pending_data(self):
        project_id = input("ID: ")
        print("example if you want to join Group 5 You input Group5")
        date_str = input("to be advisor Group?: ")

        # แปลงวันที่จากสตริงเป็นวัตถุ datetime
        # try:
        #     date_obj = datetime.strptime(date_str, "%d/%m/%y")
        # except ValueError:
        #     print("รูปแบบวันที่ไม่ถูกต้อง")
        #     return

        # สร้าง dictionary จากข้อมูลที่รับมา
        input_data = {
            "ProjectID": project_id,
            "to_be_advisor": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_pending_data(input_data)
    def update_pending_data(self, input_data):
        csv_file_path = 'Advisor_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Response', 'no-status')
        input_data.setdefault('Response_date', '-')

        # Append the new data to existing_data
        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID","to_be_advisor", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def check_approve_advisor(self, id_project):
        csv_file_path = 'Advisor_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

                # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row['ProjectID'] == id_project]
        return rejected_projects

    def update_role(self, target_id, new_role):
        with open('login.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ID'] == target_id:
                row['role'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('login.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ID", "username", "password", "role"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_faculty_deny(self, target_Group, new_role):
        with open('Member_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['to_be_member'] == target_Group:
                row['Response'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Member_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID","to_be_advisor", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

# elif val[1] = 'advisor':
    # see and do advisor related activities
class advisor:
    pass

# once everyhthing is done, make a call to the exit function
movie = []
with open(os.path.join(__location__,'Member_pending_request.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        movie.append(dict(r))
table1 = Table('movies', movie)

if val and len(val) == 2:
    user_id, user_role = val
    print(user_role)
    if user_role == 'admin':
        # Admin activities
        # print(f"Login")
        print("Performing admin activities.")
        print("Admin can Create Project or Can update all the tables there")
        x = input("you can update:")
    # ProjectID
    # Title
    # Lead
    # Member1
    # Member2
    # Advisor
    # Status

    elif user_role == 'student':
        # Student activities
        while True:
            print("Performing student activities.")
            print("What do you want to request ")
            print("1.Check status")
            print("2.requests Member")
            print("3.check request?")
            print("4.Quit")
            select = int(input("Please Select: "))
            pending = Student()
            list_member = []
            if select == 1:

                projects = pending.check_approve(user_id)

                if projects:
                    for project in projects:
                        print(project)
                        respond = list(project.values())[2]
                    # list_member.append(respond)
                        if respond == "Approve":
                            print("Status Approve.")
                            print("You can choose to be a leader or member.")
                            x = input("Your id: ")
                            y = input("Input role: ")
                            pending.update_role(x,y)


                        elif respond == "Reject":
                            print("Project not Approve Please Add new Project.")
                        elif respond == "no-status":
                            print("Waiting Admin Apporve")

            elif select == 2:
                pending.input_pending_data()
            elif select == 3:
                my_table_3_request = table1.filter(lambda x: x["ProjectID"] == user_id)
                print(my_table_3_request)
                x = int(input("1.accept or 2.deny?: "))
                if x == 1:
                    group = input("Group?: ")
                    ky = f"waiting to join {group}"
                    pending.update_student_deny(group, ky)
                if x == 2:
                    group = input("Group?: ")
                    ky = f"deny to join {group}"
                    pending.update_student_deny(group, ky)
            elif select == 4:
                break


            # "ProjectID", "to_be_member", "Response", "Response_date"


        # ID_project = input("ID Project: ")
        # print("1.Lead: ")
        # print("2.Member: ")
        # lead_or_member = input("What you choice: ")
        # if lead_or_member == 1:
        #     pass
        # elif lead_or_member == 2:
        #     pass
        # else:
        #     print("We have 2 choice 1 or 2 :")
        # student = Student()
        # id = input("Project ID: ")
        # title = input("Title Project: ")
        #
        # Lead = input("Lead name: ")
        # # if student.student_exists(Lead):
        # #     print(f"{Lead} add in Project.")
        # # else:
        # #     print("Can't find name.")
        # Member1 = input("Member1 name: ")
        # # if student.student_exists(Lead):
        # #     print(f"{Member1} add in Project.")
        # # else:
        # #     print("Can't find name.")
        # Member2 = input("Member2 name: ")
        # # if student.student_exists(Lead):
        # #     print(f"{Member2} add in Project.")
        # # else:
        # #     print("Can't find name.")
        # Advisor = input("Advisor name: ")
        # # if student.student_exists(Lead):
        # #     print(f"{Advisor} add in Project.")
        # # else:
        # #     print("Can't find name.")
        # status = input("Status: ")
        # new_data = {"ProjectID":id,'Project': title,"Lead":Lead,"Member1":Member1,"Member2":Member2,"Advisor":Advisor, 'Status': status}
        #
        # student.update(new_data)

        # Lionel.M 2977

    elif user_role == 'faculty':
        print("Performing faculty activities.")
        print("faclty Role ")
        print("See request to be a supervisor")
        print("Send accept response (for projects eventually serving as an advisor)")
        while True:
            print("1.Check status")
            print("2.requests Member")
            print("3.check request?")
            print("4.Quit")
            select = int(input("Please Select: "))
            advd = faculty()
            list_member = []
            if select == 1:
                x = input("Input ID: ")
                projects = advd.check_approve_advisor(x)
                if projects:
                    for project in projects:
                        print(project)
                        respond = list(project.values())[2]
                        # list_member.append(respond)
                        if respond == "Approve":
                            print("Status Approve.")
                            print("You can choose to be a leader or a member.")
                            x = input("Your id: ")
                            y = input("Input role: ")
                            advd.update_role(x, y)

                        elif respond == "Reject":
                            print("Project not Approve Please Add new Project.")
                        elif respond == "no-status":
                            print("Waiting Admin Apporve")

            elif select == 2:
                advd.input_pending_data()
            elif select == 3:
                my_table_3_request = table1.filter(lambda x: x["ProjectID"] == user_id)
                print(my_table_3_request)
                x = int(input("1.accept or 2.deny?: "))
                if x == 1:
                    group = input("Group?: ")
                    ky = f"waiting to join {group}"
                    advd.update_faculty_deny(group,ky)
            elif select ==4:
                break

# table3 = Table('movies',movie )
# my_table_3_survive_m = table3.filter(lambda x:x["Status"] == "On hold")
# print(my_table_3_survive_m.table)
# print("average value of ‘Worldwide Gross",my_table_3_survive_m.aggregate(lambda x: sum(x)/len(x),'Worldwide Gross'))

# sdroject = []
# with open(os.path.join(__location__,'Project.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         sdroject.append(dict(r))
# print(sdroject)

exit()
