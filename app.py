from farmers import get_all_farmers,add_farmer,get_farmer_by_id,update_farmer_name,update_farmer_village,update_farmer_phone,update_farmer_details,delete_farmer_by_id
from crop import add_crop,get_all_crops,get_crop_by_id,update_crop_details,update_crop_name,update_crop_area,update_crop_season, update_crop_production,delete_crop_by_id
from expenses import add_expense, get_all_expenses, get_expense_by_id, update_expense_details, update_expense_type, update_expense_amount, delete_expense_by_id
from sales import add_sale,get_all_sales,get_sale_by_id,update_sale_details,update_sale_quantity,update_sale_price,delete_sale_by_id
from reports import get_farmer_report
while True:
    print("Select 1 for farmers table")
    print("Select 2 for crops table")
    print("Select 3 for expenses table")
    print("Select 4 for sales table")
    print("Select 5 for Farmer Report")
    print("Select 6 For Exit")
    table=input("Which table details you want to see : ")
    
    if(table=="1"):
        while True:
            print(" ====== For Farmer Details Choose Follwing Options ======")
            print("Choose 1 : To Print All Farmers Details")
            print("Choose 2 : To Print a single Farmer Details")
            print("Choose 3 : To add New Farmer ")
            print("Choose 4 : To Make Updations of Farmer Details")
            print("Choose 5 : To Make deletion of Farmer Details")
            print("Choose 6: For Exit")
            print("==================================================")
            choice=input("Enter Your Choice : ")
            if(choice=="1"):
                get_all_farmers()

            if(choice=="2"):
                get_farmer_by_id()
            if(choice=="3"):
                add_farmer()
            if(choice=="4"):
                print("Click 1 : for Update All Values ")
                print("Click 2 : for Update Name ")
                print("Click 3 : for Update Village Name ")
                print("Click 4 : for Update Village Phone Number ")
                option=input("Choose What You Want To Update : ")
                if(option=="1"):
                    update_farmer_details()
                if(option=="2"):
                    update_farmer_name()
                if(option=="3"):
                    update_farmer_village()
                if(option=="4"):
                    update_farmer_phone()
            if(choice=="5"):
                    delete_farmer_by_id()
            if(choice=="6"): 
                    break
    if(table=="2"):
        while True:
            print(" ====== For Crop Details Choose Following Options ======")
            print("Choose 1 : To Print All Crops Details")
            print("Choose 2 : To Print a Single Crop Details")
            print("Choose 3 : To Add New Crop")
            print("Choose 4 : To Make Updations of Crop Details")
            print("Choose 5 : To Make Deletion of Crop Details")
            print("Choose 6 : For Exit")
            print("========================================================")
            choice=input("Enter Your Choice : ")
            if(choice=="1"):
                get_all_crops()
            if(choice=="2"):
                get_crop_by_id()
            if(choice=="3"):
                add_crop()
            if(choice=="4"):
                print("Click 1 : for Update All Values ")
                print("Click 2 : for Update Crop Name ")
                print("Click 3 : for Update Crop Area ")
                print("Click 4 : for Update Crop Season ")
                print("Click 5 : for Update Crop Production ")
                option=input("Choose What You Want To Update : ")
                if(option=="1"):
                    update_crop_details()
                if(option=="2"):
                    update_crop_name()
                if(option=="3"):
                    update_crop_area()
                if(option=="4"):
                    update_crop_season()
                if(option=="5"):
                    update_crop_production()
            if(choice=="5"):
                    delete_crop_by_id()
            if(choice=="6"):
                    break
    if(table=="3"):
        while True:
            print(" ====== For Expense Details Choose Following Options ======")
            print("Choose 1 : To Print All Expenses Details")
            print("Choose 2 : To Print a Single Expense Details")
            print("Choose 3 : To Add New Expense")
            print("Choose 4 : To Make Updations of Expense Details")
            print("Choose 5 : To Make Deletion of Expense Details")
            print("Choose 6 : For Exit")
            print("===========================================================")

            choice=input("Enter Your Choice : ")
            if(choice=="1"):
                get_all_expenses()
            if(choice=="2"):
                get_expense_by_id()
            if(choice=="3"):
                add_expense()
            if(choice=="4"):
                print("Click 1 : for Update All Values ")
                print("Click 2 : for Update Expense Type ")
                print("Click 3 : for Update Expense Amount ")
                option=input("Choose What You Want To Update : ")
                if(option=="1"):
                    update_expense_details()
                if(option=="2"):
                    update_expense_type()
                if(option=="3"):
                    update_expense_amount()
            if(choice=="5"):
                delete_expense_by_id()
            if(choice=="6"):
                break
    if(table=="4"):
        while True:
            print(" ====== For Sales Details Choose Following Options ======")
            print("Choose 1 : To Print All Sales Details")
            print("Choose 2 : To Print a Single Sale Details")
            print("Choose 3 : To Add New Sale")
            print("Choose 4 : To Make Updations of Sale Details")
            print("Choose 5 : To Make Deletion of Sale Details")
            print("Choose 6 : For Exit")
            print("==========================================================")
            choice=input("Enter Your Choice : ")
            if(choice=="1"):
                get_all_sales()
            if(choice=="2"):
                get_sale_by_id()
            if(choice=="3"):
                add_sale()
            if(choice=="4"):
                print("Click 1 : for Update All Values ")
                print("Click 2 : for Update Sale Quantity ")
                print("Click 3 : for Update Price Per Kg ")
                option=input("Choose What You Want To Update : ")
                if(option=="1"):
                    update_sale_details()
                if(option=="2"):
                    update_sale_quantity()
                if(option=="3"):
                    update_sale_price()
            if(choice=="5"):
                delete_sale_by_id()
            if(choice=="6"):
                break
    if(table=="5"):
        get_farmer_report()
    if(table=="6"):
        break