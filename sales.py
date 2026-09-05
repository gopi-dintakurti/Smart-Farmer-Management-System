from db import get_connection


# To Add Sale
def add_sale():
    farmer_id = input("Enter Farmer ID : ")
    crop_id = input("Enter Crop ID : ")
    quantity = input("Enter Quantity Sold : ")
    price_per_kg = input("Enter Price Per Kg : ")
    total_amount = float(quantity) * float(price_per_kg)

    connection = get_connection()
    query = """insert into sales (farmer_id, crop_id, quantity, price_per_kg, total_amount) values (%s, %s, %s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(query, (farmer_id, crop_id, quantity, price_per_kg, total_amount))
    connection.commit()
    print("Sale added Successfully !!!")
    print(f"Total Sale Amount : ₹{total_amount}")
    cursor.close()
    connection.close()


# To Print All Sales
def print_all_sales(sales):
    for sale in sales:
        print(f"===== Sale {sale[0]} Details ===== ")
        print(f"Farmer ID : {sale[1]}")
        print(f"Crop ID : {sale[2]}")
        print(f"Quantity Sold : {sale[3]}")
        print(f"Price Per Kg : {sale[4]}")
        print(f"Total Amount : ₹{sale[5]}")
        print("===================================")


def get_all_sales():
    connection = get_connection()
    query = "select * from sales;"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print_all_sales(res)
    cursor.close()
    connection.close()


# To Print Sale By ID
def print_sale_by_id(sale):
    print(f"===== Sale {sale[0]} Details ===== ")
    print(f"Farmer ID : {sale[1]}")
    print(f"Crop ID : {sale[2]}")
    print(f"Quantity Sold : {sale[3]}")
    print(f"Price Per Kg : {sale[4]}")
    print(f"Total Amount : ₹{sale[5]}")
    print("===================================")


def get_sale_by_id():
    id = input("Enter Sale Id : ")
    connection = get_connection()
    query = "select * from sales where id = %s;"
    cursor = connection.cursor()
    cursor.execute(query, (id,))
    res = cursor.fetchone()

    if res:
        print_sale_by_id(res)
    else:
        print("Sale ID not found!")

    cursor.close()
    connection.close()


# To Update Quantity
# To Update Quantity
def update_sale_quantity():
    id = input("Enter Sale Id for Update : ")
    quantity = input("Enter New Quantity : ")

    connection = get_connection()
    cursor = connection.cursor()

    # Get existing price
    query = "select price_per_kg from sales where id=%s;"
    cursor.execute(query, (id,))
    res = cursor.fetchone()

    if res:
        price_per_kg = res[0]
        total_amount = float(quantity) * float(price_per_kg)

        query = """update sales
                   set quantity=%s, total_amount=%s
                   where id=%s;"""

        cursor.execute(query, (quantity, total_amount, id))
        connection.commit()

        print("Sale Quantity Updated Successfully!!!")
        print(f"New Total Amount : ₹{total_amount}")

    else:
        print("Sale ID not found!")

    cursor.close()
    connection.close()


# To Update Price Per Kg
# To Update Price Per Kg
def update_sale_price():
    id = input("Enter Sale Id for Update : ")
    price_per_kg = input("Enter New Price Per Kg : ")

    connection = get_connection()
    cursor = connection.cursor()

    # Get existing quantity
    query = "select quantity from sales where id=%s;"
    cursor.execute(query, (id,))
    res = cursor.fetchone()

    if res:
        quantity = res[0]
        total_amount = float(quantity) * float(price_per_kg)

        query = """update sales
                   set price_per_kg=%s, total_amount=%s
                   where id=%s;"""

        cursor.execute(query, (price_per_kg, total_amount, id))
        connection.commit()

        print("Sale Price Updated Successfully!!!")
        print(f"New Total Amount : ₹{total_amount}")

    else:
        print("Sale ID not found!")

    cursor.close()
    connection.close()


# To Update All Sale Details
def update_sale_details():
    id = input("Enter Sale Id for Update : ")

    farmer_id = input("Enter Farmer ID : ")
    crop_id = input("Enter Crop ID : ")
    quantity = input("Enter New Quantity : ")
    price_per_kg = input("Enter New Price Per Kg : ")
    total_amount = float(quantity) * float(price_per_kg)
    connection = get_connection()
    query = """update sales set farmer_id=%s, crop_id=%s, quantity=%s, price_per_kg=%s, total_amount=%s where id=%s;"""
    cursor = connection.cursor()
    cursor.execute(query,(farmer_id,crop_id,quantity,price_per_kg,total_amount,id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Sale Details Updated Successfully!!!")
    else:
        print("Sale ID not found!")

    cursor.close()
    connection.close()


# To Delete Sale
def delete_sale_by_id():
    id = input("Enter Sale Id for Delete : ")
    connection = get_connection()
    query = "delete from sales where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Sale Deleted Successfully!!!")
    else:
        print("Sale ID not found!")

    cursor.close()
    connection.close()