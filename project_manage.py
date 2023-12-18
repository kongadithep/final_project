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

table1 = Table('login', login)
table2 = Table('approve', approve)
table3 = Table('name', person2)
student = Table("student", Project)


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities

class Admin:
    # def __init__(self,id,project,request,approve,):
    # elif val[1] = 'student':
    # see and do student related activities
    pass


class Student():
    def addproject(self, project):
        self.projectid = []
        self.projectid.append(project)
        # table1.update_row('Film', 'A Serious Man', 'Year', '2022')

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

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Response', 'no-status')
        input_data.setdefault('Response_date', '-')

        # Append the new data to existing_data
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
    pass


# elif val[1] = 'lead':
# see and do lead related activities
class lead:
    def view_project_status(self, project_id):
        # Implement logic to view project status based on project_id
        pass

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

            # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        new_project_data.setdefault('Status', 'no-status')

    def input_pending_data(self, namelead):

        project_id = input("Project ID: ")
        name = input("Project Name: ")
        group1 = input("What you Group?: ")
        name2 = input("Member1: ")
        name3 = input("Member2: ")
        name4 = input("Advisor: ")

        # แปลงวันที่จากสตริงเป็นวัตถุ datetime
        # try:
        #     date_obj = datetime.strptime(date_str, "%d/%m/%y")
        # except ValueError:
        #     print("รูปแบบวันที่ไม่ถูกต้อง")
        #     return

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
        # Implement logic to view responses for a specific project
        csv_file_path = 'Member_pending_request.csv'
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            # สร้าง list ของ dictionary จากข้อมูลที่มีใน CSV ไฟล์
            existing_data = list(reader)
        rejected_projects = [row for row in existing_data if row["to_be_member"] == group]
        return rejected_projects

    def view_responses_advisor(self, group):
        # Implement logic to view responses for a specific project
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

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')

        # Append the new data to existing_data
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

        # Ensure 'to_be_member' is set to 'reject' if not specified in the new data
        input_data.setdefault('Response', f'Pending From Lead {group}')
        input_data.setdefault('Response_date', '-')

        # Append the new data to existing_data
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


# elif val[1] = 'advisor':
# see and do advisor related activities
class advisor:
    pass


# once everyhthing is done, make a call to the exit function
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
        # Admin activities
        # print(f"Login")
        while True:
            print("Performing admin activities.")
            print("1.Admin can Create Project or Can update all the tables there")
            print("2.Approve or deny")
            print("3.See all project")
            print("4.Delete Project")
            print("5.Quit")
            x = input("What you choice: ")
            if x == 1:
                pass
            elif x == 2:
                print("1.Approve or Deny Student?: ")
                print("2.Approve or Deny faculty?: ")
                ap = int(input("What you choice "))
                pass
            elif x == 3:
                pass
            elif x == 4:
                pass
            elif x == 5:
                break


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

                            y = input("Input role: ")
                            advd.update_role(user_id, y)

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

                    # user_data.table[0]['ID']
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
                    elif modi == 3:
                        break
                    else:
                        print("We have three choice only!!!!")


            elif inputchoice == 3:

                print("Please Add potential members ")
                # group = input("what you group: ")
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
            print("1.See project status you group ")
            print("2.See and modify project information")
            print("3.Send out requests to potential members")
            print("4.Send out requests to a potential advisor")
            print("5.Quit")
            inputchoice1 = int(input("What you choice: "))
            if inputchoice1 == 1:
                pass
            elif inputchoice1 == 2:
                pass
            elif inputchoice1 == 3:
                pass
            elif inputchoice1 == 4:
                pass
            elif inputchoice1 == 5:
                break
    elif user_role == "member":
        while True:
            print("Welcome Member!!!!!!!")
            print("You can")
            print("1.See project status you group ")
            print("2.See and modify project information")
            print("3.See who has responded to the requests sent out")
            print("4.quit")
            inputchoice2 = int(input("What you choice: "))
            if inputchoice2 == 1:
                pass
            elif inputchoice2 == 2:
                pass
            elif inputchoice2 == 3:
                pass
            elif inputchoice2 == 4:
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
