from db import get_connection


# to add expense
def add_expense():
    farmer_id = input("Enter Farmer ID : ")
    crop_id = input("Enter Crop ID : ")
    expense_type = input("Enter Expense Type : ")
    amount = input("Enter Expense Amount : ")

    connection = get_connection()
    query = """insert into expenses
               (farmer_id, crop_id, expense_type, amount)
               values (%s, %s, %s, %s)"""

    cursor = connection.cursor()
    cursor.execute(query, (farmer_id, crop_id, expense_type, amount))
    connection.commit()

    print("Expense added Successfully !!!")

    cursor.close()
    connection.close()


# To Print All Expenses
def print_all_expenses(expenses):
    for expense in expenses:
        print(f"===== Expense {expense[0]} Details ===== ")
        print(f"Farmer ID : {expense[1]}")
        print(f"Crop ID : {expense[2]}")
        print(f"Expense Type : {expense[3]}")
        print(f"Expense Amount : {expense[4]}")
        print("===================================")


def get_all_expenses():
    connection = get_connection()
    query = "select * from expenses;"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print_all_expenses(res)

    cursor.close()
    connection.close()


# To get expense by id
def print_expense_by_id(expense):
    print(f"===== Expense {expense[0]} Details ===== ")
    print(f"Farmer ID : {expense[1]}")
    print(f"Crop ID : {expense[2]}")
    print(f"Expense Type : {expense[3]}")
    print(f"Expense Amount : {expense[4]}")
    print("===================================")


def get_expense_by_id():
    id = input("Enter Expense Id : ")

    connection = get_connection()
    query = "select * from expenses where id = %s;"
    cursor = connection.cursor()
    cursor.execute(query, (id,))
    res = cursor.fetchone()

    if res:
        print_expense_by_id(res)
    else:
        print("Expense ID not found!")

    cursor.close()
    connection.close()


# to update expense type by id
def update_expense_type():
    id = input("Enter Expense Id for Update : ")
    expense_type = input("Enter New Expense Type : ")

    connection = get_connection()
    query = "update expenses set expense_type=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (expense_type, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Expense Type Updated Successfully!!!")
    else:
        print("Expense ID not found!")

    cursor.close()
    connection.close()


# to update expense amount by id
def update_expense_amount():
    id = input("Enter Expense Id for Update : ")
    amount = input("Enter New Expense Amount : ")

    connection = get_connection()
    query = "update expenses set amount=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (amount, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Expense Amount Updated Successfully!!!")
    else:
        print("Expense ID not found!")

    cursor.close()
    connection.close()


# to update all expense details
def update_expense_details():
    id = input("Enter Expense Id for Update : ")
    farmer_id = input("Enter Farmer ID : ")
    crop_id = input("Enter Crop ID : ")
    expense_type = input("Enter New Expense Type : ")
    amount = input("Enter New Expense Amount : ")

    connection = get_connection()

    query = """update expenses set farmer_id=%s, crop_id=%s, expense_type=%s, amount=%s where id=%s;"""

    cursor = connection.cursor()
    cursor.execute(query,(farmer_id, crop_id, expense_type, amount, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Expense Details Updated Successfully!!!")
    else:
        print("Expense ID not found!")

    cursor.close()
    connection.close()


# to delete expense by id
def delete_expense_by_id():
    id = input("Enter Expense Id for Delete : ")
    
    connection = get_connection()
    query = "delete from expenses where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Expense Deleted Successfully!!!")
    else:
        print("Expense ID not found!")

    cursor.close()
    connection.close()