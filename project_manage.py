# import database module
import os, csv
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
    return login, person


login, person = initializing()

table1 = Table('login', login)


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
                return [user_data.table[0]['ID'], user_data.table[0]['role'], user_data.table[0]['username']]
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
with open(os.path.join(__location__, 'login.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        Project.append(dict(r))
approve = []
with open(os.path.join(__location__, 'Member_pending_request.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        approve.append(dict(r))
person2 = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        person2.append(dict(r))
project2 = []
with open(os.path.join(__location__, 'Project.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        project2.append(dict(r))
advisor = []
with open(os.path.join(__location__, 'Project.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        advisor.append(dict(r))

table1 = Table('login', login)
table2 = Table('approve', approve)
table3 = Table('name', person2)
student = Table("student", Project)
member_table = Table("member", project2)
advisor1 = Table("advisor",advisor)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities

class Admin:

    def admin_input_pending_data(self):
        project_id = input("Project ID: ")
        name = input("Project Name: ")
        group1 = input("What you Group?: ")
        name2 = input("Member1: ")
        name3 = input("Member2: ")
        name4 = input("Advisor: ")
        Lead = input("Lead:")
        Status = input("Approve only: ")


        # สร้าง dictionary จากข้อมูลที่รับมา
        input_data = {
            "ProjectID": project_id,
            "Project": name,
            "Group": group1,
            "Lead": Lead,
            "Member1": name2,
            "Member2": name3,
            "Advisor": name4,
            "Status": Status


            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_pending_data(input_data)

    def update_pending_data(self, input_data):
        csv_file_path = 'Project.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Status', '-')

        # Append the new data to existing_data
        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def update_student_approve(self, target_Group, new_role):
        with open('Member_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ProjectID'] == target_Group:
                row['Response'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Member_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_student_date(self, target_Group, new_role):
        with open('Member_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ProjectID'] == target_Group:
                row['Response_date'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Member_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_advisor_approve(self, target_Group, new_role):
        with open('Member_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ProjectID'] == target_Group:
                row['Response'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Advisor_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_advisor_date(self, target_Group, new_role):
        with open('Advisor_pending_request.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ProjectID'] == target_Group:
                row['Response_date'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Member_pending_request.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def delete_by_id(self, target_id):
        with open("Project.csv", mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # กรองข้อมูลเพื่อลบแถวที่มี ID เท่ากับ target_id
        updated_data = [row for row in existing_data if row['ProjectID'] != target_id]

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open("Project.csv", mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID","Project","Group","Lead","Member1","Member2","Advisor","Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(updated_data)
    def update_Project_name(self, target_id, new_projectid,new_Project,new_Group,new_lead,member1,member2,Advisor,status):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["ProjectID"] == target_id:
                row['ProjectID'] = new_projectid
                row['Project'] = new_Project
                row['Group'] = new_Group
                row['Lead'] = new_lead
                row['Member1'] = member1
                row['Member2'] = member2
                row['Advisor'] = Advisor
                row['Status'] = status

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)
    def student_exists(self, student_name):
        with open("login.csv", mode='r') as file:
            reader = csv.reader(file)

            return any(student_name == row[1] for row in reader)
class Student():
    def addproject(self, project):
        self.projectid = []
        self.projectid.append(project)


    def input_pending_data(self, id):

        date_str = input("to be member Group?: ")

        input_data = {
            "ProjectID": id,
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


        input_data.setdefault('Response', 'no-status')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
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

    def check_approve(self, id_project):
        csv_file_path = 'Member_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row['ProjectID'] == id_project]
        return rejected_projects

    def student_exists(self, student_name):
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

    def update_role2(self, target_id, new_role):
        with open('persons.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ID'] == target_id:
                row['type'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('persons.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ID", "fist", "last", "type"]
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
    def check_member(self, id, group):
        cc = member_table.filter(lambda x: x['ProjectID'] == id and x['Group'] == group)
        return cc

    def update_Project_name(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Project'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Project_status(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Group"] == target_id:
                row['Status'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
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
    def update_Project_member1(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["ProjectID"] == target_id:
                row['Member1'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)
    def update_Project_member2(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["ProjectID"] == target_id:
                row['Member1'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

# elif val[1] = 'lead':
# see and do lead related activities
class lead:

    def update_student_deny(self, target_ID, new_status):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["ProjectID"] == target_ID:
                row['Status'] = new_status

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_project_table(self, new_project_data):

        csv_file_path = 'Project.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        new_project_data.setdefault('Status', 'no-status')

    def input_pending_data(self, namelead):

        project_id = input("Project ID: ")
        name = input("Project Name: ")
        group1 = input("What you Group?: ")
        name2 = input("Member1: ")
        name3 = input("Member2: ")
        name4 = input("Advisor: ")



        # สร้าง dictionary จากข้อมูลที่รับมา
        input_data = {
            "ProjectID": project_id,
            "Project": name,
            "Group": group1,
            "Lead": namelead,
            "Member1": name2,
            "Member2": name3,
            "Advisor": name4,

            # "Lead" :
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_pending_data(input_data)

    def update_pending_data(self, input_data):
        csv_file_path = 'Project.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Status', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def view_responses_member(self, group):
        # Implement logic to view responses for a specific project
        csv_file_path = 'Member_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row["to_be_member"] == group]
        return rejected_projects

    def view_responses_advisor(self, group):

        csv_file_path = 'Advisor_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row["to_be_advisor"] == group]
        return rejected_projects

    def delete_by_id(self, target_id):
        with open("Project.csv", mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # กรองข้อมูลเพื่อลบแถวที่มี ID เท่ากับ target_id
        updated_data = [row for row in existing_data if row['Lead'] != target_id]

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(updated_data)

    def update_member1(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['Lead'] == target_id:
                row["ProjectID"] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_member2(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Member2'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Advisor(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Advisor'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Project_name(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Project'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Project_status(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Status'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def member_input_pending_data(self, id):
        name = input("Pending student id: ")
        date_str = input("to be a member Group?: ")

        input_data = {
            "ProjectID": name,
            "to_be_member": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_member_pending_data(input_data, date_str)

    def update_member_pending_data(self, input_data, group):
        csv_file_path = 'Member_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def advisor_input_pending_data(self, id):
        name = input("Pending faculty id: ")
        date_str = input("to be member Group?: ")

        input_data = {
            "ProjectID": id,
            "to_be_member": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.advisor_update_pending_data(input_data, date_str)

    def advisor_update_pending_data(self, input_data, group):
        csv_file_path = 'Advisor_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))



class faculty:
    def input_pending_data(self):
        project_id = input("ID: ")
        print("example if you want to join Group 5 You input Group5")
        date_str = input("to be advisor Group?: ")

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


        input_data.setdefault('Response', 'no-status')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_advisor", "Response", "Response_date"]
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

    def update_role2(self, target_id, new_role):
        with open('persons.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['ID'] == target_id:
                row['type'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('persons.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ID", "fist", "last", "type"]
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
            fieldnames = ["ProjectID", "to_be_advisor", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)



class advisor:
    def update_student_adivisor(self, target_ID, new_status):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Group"] == target_ID:
                row['Advisor'] = new_status

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_project_table(self, new_project_data):

        csv_file_path = 'Project.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        new_project_data.setdefault('Status', 'no-status')

    def input_pending_data(self, namelead):

        project_id = input("Project ID: ")
        name = input("Project Name: ")
        group1 = input("What you Group?: ")
        name2 = input("Member1: ")
        name3 = input("Member2: ")
        name4 = input("Advisor: ")



        # สร้าง dictionary จากข้อมูลที่รับมา
        input_data = {
            "ProjectID": project_id,
            "Project": name,
            "Group": group1,
            "Lead": namelead,
            "Member1": name2,
            "Member2": name3,
            "Advisor": name4,

            # "Lead" :
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_pending_data(input_data)

    def update_pending_data(self, input_data):
        csv_file_path = 'Project.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Status', '-')

        # Append the new data to existing_data
        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def view_responses_member(self, group):

        csv_file_path = 'Member_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row["to_be_member"] == group]
        return rejected_projects

    def view_responses_advisor(self, group):

        csv_file_path = 'Advisor_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row["to_be_advisor"] == group]
        return rejected_projects

    def delete_by_id(self, target_id):
        with open("Project.csv", mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # กรองข้อมูลเพื่อลบแถวที่มี ID เท่ากับ target_id
        updated_data = [row for row in existing_data if row['Lead'] != target_id]

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(updated_data)

    def update_member1(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row['Lead'] == target_id:
                row["ProjectID"] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_member2(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Member2'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Advisor(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Advisor'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Project_name(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Project'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def update_Project_status(self, target_id, new_role):
        with open('Project.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)

        # วนลูปใน existing_data เพื่ออัปเดต role เมื่อพบ ID ที่ตรงกับ target_id
        for row in existing_data:
            if row["Lead"] == target_id:
                row['Status'] = new_role

        # เขียนข้อมูลทั้งหมดลงใน CSV ไฟล์
        with open('Project.csv', mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "Project", 'Group', "Lead", "Member1", "Member2", "Advisor", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

    def member_input_pending_data(self, id):
        name = input("Pending student id: ")
        date_str = input("to be a member Group?: ")

        input_data = {
            "ProjectID": name,
            "to_be_member": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.update_member_pending_data(input_data, date_str)

    def update_member_pending_data(self, input_data, group):
        csv_file_path = 'Member_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def advisor_input_pending_data(self, id):
        name = input("Pending faculty id: ")
        date_str = input("to be member Group?: ")

        input_data = {
            "ProjectID": id,
            "to_be_member": date_str
            # เพิ่มค่าอื่นๆ ที่ต้องการรับอินพุต
        }

        # เรียกใช้เมทอดที่ต้องการในต่อไป
        self.advisor_update_pending_data(input_data, date_str)

    def advisor_update_pending_data(self, input_data, group):
        csv_file_path = 'Advisor_pending_request.csv'

        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)


        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')


        existing_data.append(input_data)

        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ["ProjectID", "to_be_member", "Response", "Response_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # เขียน header
            writer.writeheader()

            # เขียนข้อมูลในแต่ละแถว
            writer.writerows(existing_data)

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))



movie = []
with open(os.path.join(__location__, 'Member_pending_request.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        movie.append(dict(r))
table1 = Table('movies', movie)

if val and len(val) == 3:
    user_id, user_role, user_name = val
    print(user_role)
    if user_role == 'admin':
        while True:
            print("Performing admin activities.")
            print("1.Admin can Create Project or Can update all the tables there")
            print("2.Approve or deny")
            print("3.See all project")
            print("4.Delete Project")
            print("5.Quit")
            admin = Admin()
            isa = int(input("What you choice: "))
            if isa == 1:
                print(project2)
                s = int(input("1.Create Project / 2.update project: "))
                if s == 1:
                    admin.admin_input_pending_data()
                elif s == 2:
                    print(project2)
                    ID = input("ProjectID: ")
                    name_Project = input("Nameproject: ")
                    Lead = input("New lead: ")
                    if admin.student_exists(Lead):
                        print(f"{Lead} add in Project.")
                    else:
                        print("Can't find name.")
                    Group = input("New Group: ")
                    Member1 = input("New member1: ")
                    if admin.student_exists(Member1):
                        print(f"{Member1} add in Project.")
                    else:
                        print("Can't find name.")
                    Member2 = input("New member2: ")
                    if admin.student_exists(Member2):
                        print(f"{Member2} add in Project.")
                    else:
                        print("Can't find name.")
                    Advisor = input("New Advisor: ")
                    if admin.student_exists(Advisor):
                        print(f"{Advisor} add in Project.")
                    else:
                        print("Can't find name.")
                    Status = input("New Status: ")
                    admin.update_Project_name(ID,name_Project,Lead,Group,Member1,Member2,Advisor,Status)


            elif isa == 2:
                print("1.Approve or Deny Student?: ")
                print("2.Approve or Deny faculty?: ")
                ap = int(input("What you choice: "))

                if ap == 1:
                    print(approve)
                    student_id = input("student ID:")
                    Respond = input("Accept/deny: ")
                    Respond_date = input("Respond date: ")
                    admin.update_student_approve(student_id,Respond)
                    admin.update_student_date(student_id,Respond_date)
                if ap ==2:
                    print(advisor)
                    faculty = input("faculty ID")
                    Respond_f = input("Accept/deny")
                    Respond_date_f = input("Respond date")
                    admin.update_advisor_approve(faculty,Respond_f)
                    admin.update_student_date(faculty,Respond_date_f)

            elif isa == 3:
                print(project2)
            elif isa == 4:
                print(project2)
                delete = input("Project ID: ")
                admin.delete_by_id(delete)

            elif isa == 5:
                break




    elif user_role == 'student':
        # Student activities
        while True:
            print("Performing student activities.")
            print("What do you want to request ")
            print("1.Check status(***You should add information before check***)")
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
                        if respond == "Approve":
                            print("Status Approve.")
                            print("You can choose to be a leader or 2.member.")
                            y = input("You can type Lead or member: ")
                            pending.update_role(user_id, y)
                            pending.update_role2(user_id, y)
                            list_member.append(respond)
                        elif respond == "Reject":
                            print("Project not Approve Please Add new Project.")
                            list_member.append(respond)
                        elif respond == "no-status":
                            print("Waiting Admin Apporve")
                            list_member.append(respond)
                else:
                    if (len(projects)) == 0:
                        print("-----No data Please Add Information.-----")


            elif select == 2:
                pending.input_pending_data(user_id)
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
                    ku = f"deny to join {group}"
                    pending.update_student_deny(group, ku)
            elif select == 4:
                break


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
                projects = advd.check_approve_advisor(user_id)
                if projects:
                    for project in projects:
                        print(project)
                        respond = list(project.values())[2]

                        if respond == "Approve":
                            print("Status Approve.")

                            y = input("Input role: ")
                            advd.update_role(user_id, y)
                            advd.update_role2(user_id, y)

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
                    advd.update_faculty_deny(group, ky)
            elif select == 4:
                break
    elif user_role == 'Lead':
        while True:
            print("Welcome Lead!!!!!!!")
            print("You can")
            print("1.See project status ")
            print("2.See and modify project information")
            print("3.Send out requests to potential members")
            print("4.Send out requests to a potential advisor")
            print("5.Quit")
            lead1 = lead()
            inputchoice = int(input("What you choice: "))
            if inputchoice == 1:
                print("1.check pending member")
                print("2.check pending advisor")
                pm = int(input("1 or 2:"))
                if pm == 1:
                    group = input("what you group: ")
                    projects = lead1.view_responses_member(group)
                    if projects:
                        for project in projects:
                            print(project)
                elif pm == 2:
                    group = input("what you group: ")
                    projects = lead1.view_responses_advisor(group)
                    if projects:
                        for project in projects:
                            print(project)

            elif inputchoice == 2:
                print("1.add project and information")
                print("2.delete Group project")
                print("3.modify project information")
                print("Quit")
                modify_ = int(input("What you choice: "))
                if modify_ == 1:
                    Gro = input("What you Group?: ")
                    table = table1.filter(lambda x: x['to_be_member'] == Gro and x['Response'] == "Approve")

                    print(table)


                    lead1.input_pending_data(user_name)
                elif modify_ == 2:
                    lead1.delete_by_id(user_name)
                elif modify_ == 3:
                    print("1.modify Project name")
                    print("2.update Project")
                    print("3.Quit")
                    modi = int(input("what number you choice: "))
                    if modi == 1:
                        new_nameProject = input("New Projectname: ")
                        lead1.update_Project_name(user_name, new_nameProject)
                    elif modi == 2:
                        new_status_project = input("Status Project: ")
                        lead1.update_Project_status(user_name, new_status_project)
                    elif modi == 3:
                        break
                    else:
                        print("We have three choice only!!!!")


            elif inputchoice == 3:

                print("Please Add potential members ")

                names_member = table3.filter(lambda x: x["type"] == "student")
                print(names_member)
                lead1.member_input_pending_data(user_id)

            elif inputchoice == 4:
                print("Please Add potential Advisor ")
                names_faculty = table3.filter(lambda x: x["type"] == "faculty")
                print(names_faculty)
                lead1.advisor_input_pending_data(user_id)
            elif inputchoice == 5:
                break

    elif user_role == 'advisor':
        while True:
            print("Welcome Advisor!!!!!!!")
            print("You can")
            print("1.See project status you group")
            print("2,update advisor")
            print("3.Quit")

            inputchoice1 = int(input("What you choice: "))
            ad = advisor()
            if inputchoice1 == 1:
                status = member_table.filter(lambda x: x["Advisor"] == user_name)
                print(status)
            elif inputchoice1 ==2:
                group = input("What you Group request: ")
                ad.update_student_adivisor(group,user_name)
            elif inputchoice1 == 3:
                break
    elif user_role == "member":
        while True:
            print("Welcome Member!!!!!!!")
            print("You can")
            print("1.See project status you group ")
            print("2.See and modify project information")
            print("3.See who has responded to the requests sent out")
            print("4.Pleas Add you name If you select 1 and don't have you name ")
            print("5.quit")
            inputchoice2 = int(input("What you choice: "))
            c_member = Member()
            if inputchoice2 == 1:
                project_id = input("Project ID: ")
                group_member = input("Group Member: ")
                addname = advisor1.filter(lambda x:x["Group"] == group_member)
                print(addname)
                print("if you don't have a name in your group Please Member1 or Member2 in Choice 4")
                cc = c_member.check_member(project_id, group_member)
                print(cc)

            elif inputchoice2 == 2:
                print("1.modify Project name")
                print("2.update Project")
                print("3.Quit")
                modi = int(input("what number you choice: "))
                if modi == 1:
                    new_nameProject = input("New Projectname: ")
                    c_member.update_Project_name(user_name, new_nameProject)
                elif modi == 2:
                    new_status_project = input("Status Project: ")
                    group = input("Group: ")
                    c_member.update_Project_status(group, new_status_project)
                elif modi == 3:
                    break
            elif inputchoice2 == 3:
                x = int(input("1.accept or 2.deny?: "))
                if x == 1:
                    group = input("Group?: ")
                    ky = f"waiting to join{group}"
                    kz = table2.filter(lambda x: x["Response"] == ky)
                    print(kz)
                if x == 2:
                    group = input("Group?: ")
                    ku = f"deny to join Group{group}"
                    kz = table2.filter(lambda x: x["Response"] == ku)
                    print(kz)
            elif inputchoice2 == 4:
                name = int(input("1.Name1 / 2.Name2 "))
                if name == 1:
                    project_ID = input("project_ID: ")
                    c_member.update_Project_member1(project_ID,user_name)
                if name == 2:
                    project_ID2 = input("Group: ")
                    c_member.update_Project_member2(project_ID2,user_name)
            elif inputchoice2 == 5:
                break



exit()
