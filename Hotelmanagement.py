import mysql.connector as m
print("---------------***********************************-------------")
print('---------------|             WELCOME             |-------------')
print('---------------|                To               |-------------')
print('---------------|            Gold  Rise           |-------------')
print("---------------***********************************-------------")

# Checking MySQL Connection
def connect():
    c = m.connect(host='localhost', user='root', password='power', database='hotelm')
    if c.is_connected():
        print("\n ")
    else:
        print('Not connected')
    return c

c = connect()

# Creating a cursor
x = c.cursor()

# Creating a database if it doesn't exist
x.execute('CREATE DATABASE IF NOT EXISTS hotelm')

# CREATE TABLE statements

x.execute('''CREATE TABLE IF NOT EXISTS room_details (
                rtype VARCHAR(50),
                rno INT PRIMARY KEY,
                rent INT,
                status VARCHAR(50)
            )''')

x.execute('''CREATE TABLE IF NOT EXISTS employee (
                E_id INT PRIMARY KEY,
                E_name VARCHAR(50),
                E_salary INT,
                E_addr VARCHAR(100),
                DOJ DATE,
                E_work VARCHAR(100)
            )''')

x.execute('''CREATE TABLE IF NOT EXISTS customer (
                C_id INT PRIMARY KEY,
                C_name VARCHAR(50),
                email VARCHAR(50)
            )''')

x.execute('''CREATE TABLE IF NOT EXISTS booking (
                rno INT,
                C_id INT,
                rtype VARCHAR(50),
                C_name VARCHAR(50),
                DOO DATE,
                checkout DATE,
                advanced DECIMAL(10, 2)
            )''')

# ADD FOREIGN KEYS
t = 'ALTER TABLE booking ADD FOREIGN KEY (rno) REFERENCES room_details(rno)on delete cascade'
x.execute(t)

# Modify the foreign key constraints in your database schema to cascade deletes
w = 'ALTER TABLE booking ADD FOREIGN KEY (C_id) REFERENCES customer(C_id) ON DELETE CASCADE'
x.execute(w)


# Committing the changes

c.commit()

'''-----------------------------Employee----------------------------------'''

# ===================================ADD EMPLOYEE================================
def employee():
    c = connect()
    x = c.cursor()
    print("-------------ADD NEW EMPLOYEE---------------")
    E_id = int(input("Enter Employee ID: "))
    E_name = input("Enter Employee NAME: ")
    E_salary = int(input("Enter Employee Salary: "))
    addr = input("Enter Employee Address: ")
    DOJ = input("Enter Employee DOJ (Date of Joining) (YYYY-MM-DD): ")
    E_work = input("Enter Employee Work: ")
    q = "INSERT INTO employee VALUES({}, '{}', {}, '{}', '{}', '{}')".format(E_id, E_name, E_salary, addr, DOJ, E_work)
    x.execute(q)
    print("--------Added Successfully--------")
    c.commit()
    userlog()

#====================================VIEW EMPLOYEE===============================
def view_emp():
    c = connect()
    x = c.cursor()
    x.execute("SELECT * FROM employee")
    r = x.fetchall()
    for i in r:
        print(i)
    login_emp()

#====================================UPDATE EMPLOYEE=============================
def update_emp(emp_id):
    c = connect()
    x = c.cursor()
    print("+----------------------------------------------------+")
    print("|              UPDATE EMPLOYEE RECORD                |")
    print("+----------------------------------------------------+")
    print("|1.  Update Employee Name                            |")
    print("|2.  Update Employee Salary                          |")
    print("|3.  Update Employee Address                         |")
    print("|4.  Update Employee DOJ (Date of Joining)           |")
    print("|5.  Update Employee Work                            |")
    print("|0.  Go to previous menu                             |")
    print("+----------------------------------------------------+")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        new_name = input("Enter new Employee Name: ")
        query = "UPDATE employee SET E_name = '{}' WHERE E_id = {}".format(new_name, emp_id)
    elif choice == 2:
        new_salary = int(input("Enter new Employee Salary: "))
        query = "UPDATE employee SET E_salary = {} WHERE E_id = {}".format(new_salary, emp_id)
    elif choice == 3:
        new_addr = input("Enter new Employee Address: ")
        query = "UPDATE employee SET E_addr = '{}' WHERE E_id = {}".format(new_addr, emp_id)
    elif choice == 4:
        new_doj = input("Enter new Employee DOJ (Date of Joining) (YYYY-MM-DD): ")
        query = "UPDATE employee SET DOJ = '{}' WHERE E_id = {}".format(new_doj, emp_id)
    elif choice == 5:
        new_work = input("Enter new Employee Work: ")
        query = "UPDATE employee SET E_work = '{}' WHERE E_id = {}".format(new_work, emp_id)
    elif choice == 0:
        login_emp()
    else:
        print("Invalid choice")
        userlog()

    x.execute(query)
    c.commit()
    print("Employee record updated successfully!")

#=====================================DELETE EMPLOYEE============================
def delete_emp():
    c = connect()
    x = c.cursor()
    emp_id = int(input("Enter the Employee ID to delete: "))
    query = "DELETE FROM employee WHERE E_id = {}".format(emp_id)
    x.execute(query)
    c.commit()
    print("Employee record deleted successfully!")
    login_emp()

#=====================================LOGIN EMPLOYEE=============================
def login_emp():
    c = connect()
    x = c.cursor()
    print("-------------EMPLOYEE LOGIN---------------")
    entered_id = int(input("Enter Employee ID: "))
    entered_name = input("Enter Employee Name: ")
    query = "SELECT * FROM employee WHERE E_id = {} AND E_name = '{}'".format(entered_id, entered_name)
    x.execute(query)
    result = x.fetchall()

    if result:
        print("Login successful!\n")
        print("+---------------------------------+")
        print("| 1. Update Record                |")
        print("| 2. Add Employee                 |")
        print("| 3. Delete Employee Account      |")
        print("| 4. Show Employees               |")
        print("| 0. main menu                    |")
        print("+---------------------------------+")
        c = int(input("Enter Choice: "))

        if c == 1:
            update_emp(entered_id)
        elif c == 2:
            employee()
        elif c == 3:
            delete_emp()
        elif c == 4:
            view_emp()
        elif c == 0:
            manager()
        else:
            login_emp()
    else:
        print("Login failed. Invalid credentials.")
        userlog()

"""------------------------------Customer--------------------------------------"""

#=====================================ADD CUSTOMER===============================
def cust_signup():
    # For Customer signup
    c = connect()
    x = c.cursor()
    print("-----<ADD NEW CUSTOMER>-----")
    C_id = int(input("Enter CUSTOMER ID: "))
    C_name = input("Enter CUSTOMER NAME: ")
    email = input("Enter email of CUSTOMER: ")
    q = input("Do You Want To Continue (y/n) ")
    if q.lower() == 'y':
        x.execute("INSERT INTO customer VALUES({}, '{}', '{}')".format(C_id, C_name, email))
        print("Added")
    elif q.lower() == 'n':
        cust()
    else:
        cust_signup()
    c.commit()
    cust()

#====================================CHECK CUSTOMER EXISTENCE====================
def customer_exist(C_id):
    c = connect()
    x = c.cursor()
    x.execute("SELECT * FROM customer WHERE C_id = '{}'".format(C_id))
    record1 = x.fetchone()
    return record1
    c.commit()

#====================================VIEW CUSTOMER===============================
def view_cust():
    c = connect()
    x = c.cursor()
    print("-----<VIEW CUSTOMERS>-----\n")
    x.execute("SELECT * FROM customer")
    r = x.fetchall()
    for row in r:
        print(row)
    c.commit()

#====================================UPDATE CUSTOMER=============================
def update_cust(C_id):
    c = connect()
    x = c.cursor()
    print("+-------------------------------+")
    print("|    UPDATE Customer RECORD     |")
    print("+--+----------------------------+")
    print("|1.| Update Customer C_id       |")
    print("|2.| Update Customer Name       |")
    print("|3.| Update Customer Email      |")
    print("+--+----------------------------+")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        new_CID = int(input("Enter new Customer C_id (Customer ID): "))
        q = "UPDATE Customer SET C_id = {} WHERE C_id = {}".format(new_CID, C_id)
    elif choice == 2:
        new_name = input("Enter new Customer Name: ")
        q = "UPDATE Customer SET C_name = '{}' WHERE C_id = {}".format(new_name, C_id)
    elif choice == 3:
        new_email = input("Enter new Customer Email: ")
        q = "UPDATE Customer SET email = '{}' WHERE C_id = {}".format(new_email, C_id)
    else:
        print("Invalid choice")
        return

    x.execute(q)
    c.commit()
    print("Customer record updated successfully!")
    cust_login()

#====================================DELETE CUSTOMER=============================
def delete_cust():
    c = connect()
    x = c.cursor()
    C_id = int(input("Enter the Customer ID to delete: "))
    
    # Delete associated booking records first
    x.execute("DELETE FROM booking WHERE C_id = {}".format(C_id))
    
    # Then delete the customer record
    x.execute("DELETE FROM customer WHERE C_id = {}".format(C_id))
    
    c.commit()
    print("Customer record and associated bookings deleted successfully!")

    # Ask the user if they want to perform additional actions
    choice = input("Do you want to perform another action? (y/n): ").lower()
    if choice == 'y':
        cust_login()
    else:
        userlog()


'''-----------------------------------Room------------------------------------'''

def room_exist(rno):
    c = connect()
    x = c.cursor()
    x.execute("SELECT * FROM room_details WHERE rno = {}".format(rno))
    record = x.fetchone()
    return record
    c.commit()


def book_room():
    c = connect()
    x = c.cursor()
    print("-----<BOOKING A NEW ROOM>-----")
    C_id = int(input("Enter CUSTOMER ID: "))
    C_name = input("Enter CUSTOMER NAME:")
    print("We have the rooms ")
    print("0. Main Menu\n")
    print("+---------------------------+")
    print("|   Rooms Type   |  Price($)|")
    print("+---------------------------+")
    print("|1. Ultra Delux  |  $100000 |")
    print("|2. Delux        |  $70000  |")
    print("|3. Standard     |  $50000  |")
    print("|4. Basic        |  $20000  |")
    print("+---------------------------+")
    q = int(input("Enter Type of room (1-4): "))

    # Define room types and corresponding prices
    rtypes = ['Ultra Delux', 'Delux', 'Standard', 'Basic']
    prices = [100000, 70000, 50000, 20000]

    available_rooms = []

    if 0 < q <= len(rtypes):
        rtype = rtypes[q - 1]
        print(f"Room Price = {prices[q - 1]}")

        # Available room numbers for the selected room type
        x.execute("SELECT rno FROM room_details WHERE rtype = %s AND status = 'available'", (rtype,))
        available_rooms = x.fetchall()
        

        if available_rooms:
            print(f"Available Room Numbers for {rtype}:")
            for room in available_rooms[:4]:
                print(room[0])
        else:
            print(f"No available {rtype} rooms.")
            print(" Please Login Again ( Time-Out )")
            return
    elif q == 0:
        userlog()
    else:
        print("Invalid room type selected.")
        return

    # The user to select a room number
    rno = int(input("Enter Room Number to book: "))

    # Check if the selected room is available
    if (rno,) in available_rooms:
        DOO = input("Enter DATE OF OCCUPANCY (YYYY-MM-DD): ")
        checkout = input("Enter CHECK OUT DATE  (YYYY-MM-DD): ")
        advanced = float(input("Enter advanced amount: "))

        # Check if the room is available
        room_record = room_exist(rno)

        if room_record and room_record[3] == "available":
            # Insert booking record
            sql = "INSERT INTO booking (rno, C_id, rtype, C_name, DOO, checkout, advanced) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (rno, C_id, rtype, C_name, DOO, checkout, advanced)
            x.execute(sql, values)

            # Update room status to occupied
            x.execute("UPDATE room_details SET status = 'occupied' WHERE rno = %s", (rno,))

            c.commit()
            print(f"Room {rno} booked for Customer ID {C_id} - {C_name}")
        else:
            print("Room is not available for booking.")
    else:
        print("Invalid room number selected.")


# =============================== TO GENERATE BILL ==============================


def generate_bill(C_id):
    c = connect()
    x = c.cursor()

    # Fetch booking data
    x.execute("SELECT DOO, checkout, C_id, C_name, rno, advanced FROM booking where c_id={}".format(C_id))
    booking_data = x.fetchall()

    if booking_data:
        for row in booking_data:
            DOO, checkout, C_id, C_name, rno, advanced = row
            num_nights = int(checkout[-2:]) - int(DOO[-2:])

            # Fetch room rent for the specified room number
            x.execute("SELECT rent FROM room_details WHERE rno = {}".format(rno))
            room_rent_data = x.fetchone()
            if room_rent_data:
                room_rent = room_rent_data[0]

                # Calculate the total cost
                total_cost = room_rent * num_nights

                # Calculate the balance amount
                balance = total_cost - float(advanced)
                print("           ___________________")
                print("")
                print("+---------|     *  Bill  *    |------------+")
                print("           ___________________")
                print('')
                print(f"| Room Number            :   {rno}            |")
                print(f"| Customer ID            :   {C_id}          |")
                print(f"| Customer Name          :   {C_name}         |")
                print(f"| Date of Occupancy      :   {DOO}    |")
                print(f"| Check Out Date         :   {checkout}    |")
                print(f"| Room Rent per Night    : $ {room_rent}         |")
                print(f"| Number of Nights Stayed:   {num_nights}             |")
                print(f"| Total Room Rent        : $ {total_cost}             |")
                print(f"| Advanced Payment       : $ {advanced}       |")
                print(f"| Balance Amount         : $ {balance}      |")
                print("+------------------------------------------+")
                print('                   :)                     ')

                c.commit()
            else:
                print("Error fetching room rent data.")
    else:
        print("No booking data found.")

def add_room_details():
    c = connect()
    x = c.cursor()
    print("-----<ADD NEW ROOM DETAILS>-----")
    rtype = input("Enter TYPE of ROOM: ")
    rno = int(input("Enter ROOM NUMBER: "))
    rent = int(input("Enter ROOM RENT: "))
    status = input("Enter status: ")

    # Check if the room number already exists
    if room_exist(rno):
        print("Room with the same number already exists.")
        return

    x.execute("INSERT INTO room_details (rtype, rno, rent, status) VALUES (%s, %s, %s, %s)", (rtype, rno, rent, status))
    c.commit()
    print("Room details added successfully.")

def update_room_details():
    c = connect()
    x = c.cursor()
    print("-----<UPDATE ROOM DETAILS>-----")
    rno = int(input("Enter ROOM NUMBER to update: "))
    new_status = input("Enter new status: ")
    room_record = room_exist(rno)

    if room_record:
        x.execute("UPDATE room_details SET status = %s WHERE rno = %s", (new_status, rno))
        c.commit()
        print(f"Room {rno} details updated successfully.")
    else:
        print("Room not found.")

def check_room_details():
    c = connect()
    x = c.cursor()
    print("-----<CHECK ROOM DETAILS>-----")
    rno = int(input("Enter ROOM NUMBER to check: "))

    room_record = room_exist(rno)

    if room_record:
        print("Room Details:")
        print("Room Type:", room_record[0])
        print("Room Number:", room_record[1])
        print("Room Rent:", room_record[2])
        print("Status:", room_record[3])
    else:
        print("Room not found.")

def cust_login():
    c = connect()
    x = c.cursor()
    print("-------------USER LOGIN---------------")
    entered_id = int(input("Enter USER ID: "))
    entered_name = input("Enter USER Name: ")
    query = "SELECT * FROM customer WHERE C_id = {} and C_name = '{}'".format(entered_id, entered_name)
    x.execute(query)
    result = x.fetchall()

    if result:
        print("Login successful!\n")
        print("+---------------------------------+")
        print("| 1. Book Rooms                   |")
        print("| 2. Update Account               |")
        print("| 3. Delete Account               |")
        print("| 4. Get bill                     |")
        print("| 5. Main Menu                    |")
        print("+---------------------------------+")
        c = int(input("Enter Choice :"))
        if c == 1:
            book_room()
        elif c == 2:
            update_cust(entered_id)
        elif c == 3:
            delete_cust()
        elif c == 4:
            generate_bill(entered_id)
        elif c == 5:
            userlog()
        else:
            cust_login()
    else:
        print("Login failed. Invalid credentials.")
    userlog()

def cust():
    c = connect()
    print("1. Sign Up (customer) ")
    print("2. Login ")
    c = int(input("Enter Your Option :"))
    if c == 1:
        cust_signup()
    elif c == 2:
        cust_login()
    else:
        cust()


def manager():
    print("+----+-------------------+")
    print("| 1. |  Employee Login   |")
    print("| 2. |  Main Menu        |")
    print("+----+-------------------+")
    c = int(input("Enter Your Choice : "))
    if c == 1:
        login_emp()
    elif c == 2:
        userlog()
    else:
        manager()

def userlog():
    c = connect()
    print("=========| Welcome, TO Hotel |==========")
    print("+----+----------------+")
    print("| 1. |  Customer      |")
    print("| 2. |  Employee      |")
    print("+----+----------------+")
    
    login = int(input("Enter Option :"))
    if login == 1:
        cust()
    elif login == 2:
        manager()
    elif login == None:
        print("something went wrong try again")
        userlog()



         
userlog()
