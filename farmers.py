from db import get_connection

#too add farmer to table
def add_farmer():
    name=input("Enter Farmer Name : ")
    village=input("Enter Farmer Village : ")
    phone=input("Enter Farmer Phone Number :  ")
    
    connection=get_connection()
    query="insert into farmers (name,village,phone) values (%s,%s,%s)"
    cursor=connection.cursor()
    cursor.execute(query,(name,village,phone))
    connection.commit()
    print("Farmer added Successfully !!!")
    cursor.close()
    connection.close()

#to print all farmers from the table
def print_all_farmers(farmers):
    for farmer in farmers:
        print(f"===== Farmer {farmer[0]} Details ===== ")
        print(f"Farmer Name : {farmer[1]}")
        print(f"Farmer village : {farmer[2]}")
        print(f"Farmer Phone Number : {farmer[3]}")
        print("===================================")

def get_all_farmers():
    connection=get_connection()
    query="select * from farmers;"
    cursor=connection.cursor()
    cursor.execute(query)
    res=cursor.fetchall()
    print_all_farmers(res)
    cursor.close()
    connection.close()

#to print single farmer by id

def print_farmer_by_id(farmer):
    print(f"====== Farmer {farmer[0]} Details ====== ")
    print(f"Farmer Name : {farmer[1]}")
    print(f"Farmer village : {farmer[2]}")
    print(f"Farmer Phone Number : {farmer[3]}")
    print("===================================")


def get_farmer_by_id():
    id=input("Enter Farmer Id : ")
    connection=get_connection()
    query="select * from farmers where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,id)
    res=cursor.fetchone()

    if res:
        print_farmer_by_id(res)
    else:
        print("Farmer ID not found!")
    
    cursor.close()
    connection.close()

#to updated farmer name by id
def update_farmer_name():
    id=input("Enter Farmer Id for Update : ")
    name=input("Enter new name : ")
    connection=get_connection()
    query="update farmers set name=%s where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,(name,id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Name Updated Successfully!!!")
    else:
        print("Farmer ID not found!")
    cursor.close()
    connection.close()

#to updated farmer village by id 
def update_farmer_village():
    id=input("Enter Farmer Id for Update : ")
    village=input("Enter New Village Name : ")
    connection=get_connection()
    query="update farmers set village=%s where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,(village,id))
    connection.commit()
    if cursor.rowcount > 0:
        print(" Village Name Updated Succesfully!!!")
    else:
        print("Farmer ID not found!")
    
    cursor.close()
    connection.close()

#to updated farmer Phone Number by id 
def update_farmer_phone():
    id=input("Enter Farmer Id for Update : ")
    number=input("Enter New Phone Number : ")
    connection=get_connection()
    query="update farmers set phone=%s where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,(number,id))
    connection.commit()
    if cursor.rowcount > 0:
        print(" Phone Number Updated Succesfully!!!")
    else:
        print("Farmer ID not found!")
    
    cursor.close()
    connection.close()
    
# to update all the fields
def update_farmer_details():
    id=input("Enter Farmer Id for Update : ")
    name=input("Enter new name : ")
    village=input("Enter New Village Name : ")
    number=input("Enter New Phone Number : ")
    
    connection=get_connection()
    query="update farmers set name=%s, village=%s, phone=%s where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,(name,village,number,id))
    connection.commit()
    if cursor.rowcount > 0:
        print(" Updated Succesfully!!!")
    else:
        print("Farmer ID not found!")
    
    cursor.close()
    connection.close()


#to Delete farmer Details by id
def delete_farmer_by_id():
    id=input("Enter Farmer Id for Delete : ")
    connection=get_connection()
    query="delete from farmers where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,id)
    connection.commit()
    if cursor.rowcount > 0:
        print("Deleted Successfully!!!")
    else:
        print("Farmer ID not found!")
    cursor.close()
    connection.close()
