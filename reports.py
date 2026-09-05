from db import get_connection


def get_farmer_report():

    farmer_id = input("Enter Farmer ID : ")

    connection = get_connection()
    cursor = connection.cursor()

    # Farmer and Crop Details
    query = """
    SELECT f.name, f.village, f.phone, c.crop_name, c.area, c.season, c.production FROM farmers f JOIN crops c ON f.id = c.farmer_id WHERE f.id = %s ORDER BY c.crop_name; """

    cursor.execute(query, (farmer_id,))
    farmer = cursor.fetchone()

    if farmer:

        print("\n========== FARMER REPORT ===========")
        print(f"Farmer Name    : {farmer[0]}")
        print(f"Village        : {farmer[1]}")
        print(f"Phone          : {farmer[2]}")
        print(f"Crop Name      : {farmer[3]}")
        print(f"Crop Area      : {farmer[4]}")
        print(f"Season         : {farmer[5]}")
        print(f"Production     : {farmer[6]} kg")

        # Total Expenses
        query = """
        SELECT SUM(amount) FROM expenses WHERE farmer_id = %s GROUP BY farmer_id;"""

        cursor.execute(query, (farmer_id,))
        expense = cursor.fetchone()

        if expense:
            total_expense = expense[0]
        else:
            total_expense = 0

        # Total Sales
        query = """SELECT SUM(total_amount) FROM sales WHERE farmer_id = %s GROUP BY farmer_id; """

        cursor.execute(query, (farmer_id,))
        sale = cursor.fetchone()

        if sale:
            total_sales = sale[0]
        else:
            total_sales = 0

        profit = total_sales - total_expense

        print(f"Total Expenses : ₹{total_expense}")
        print(f"Total Sales    : ₹{total_sales}")
        print(f"Profit         : ₹{profit}")
        print("===================================")

    else:
        print("Farmer ID not found!")

    cursor.close()
    connection.close()