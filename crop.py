from db import get_connection

#too add farmer to table
def add_crop():
    farmer_id=input("Enter Farmer ID : ")
    crop_name=input("Enter Crop Name (Rice/Black Gram) : ")
    area=input("Enter Crop Area : ")
    season=input("Enter Season (Kharif/Rabi) : ")
    production=input("Enter Production of the Crop : ")
    
    connection=get_connection()
    query="insert into crops (farmer_id,crop_name,area,season,production) values (%s,%s,%s,%s,%s)"
    cursor=connection.cursor()
    cursor.execute(query,(farmer_id,crop_name,area,season,production))
    connection.commit()
    print("Crop added Successfully !!!")
    cursor.close()
    connection.close()

# To Print All Crops
def print_all_crops(crops):
    for crop in crops:
        print(f"===== Crop {crop[0]} Details ===== ")
        print(f"Farmer ID : {crop[1]}")
        print(f"Crop Name : {crop[2]}")
        print(f"Crop Area : {crop[3]}")
        print(f"Crop Season : {crop[4]}")
        print(f"Crop Production : {crop[5]}")
        print("===================================")

def get_all_crops():
    connection=get_connection()
    query="select * from crops;"
    cursor=connection.cursor()
    cursor.execute(query)
    res=cursor.fetchall()
    print_all_crops(res)
    cursor.close()
    connection.close()

#to get crop by id
def print_crop_by_id(crop):
    print(f"===== Crop {crop[0]} Details ===== ")
    print(f"Farmer ID : {crop[1]}")
    print(f"Crop Name : {crop[2]}")
    print(f"Crop Area : {crop[3]}")
    print(f"Crop Season : {crop[4]}")
    print(f"Crop Production : {crop[5]}")
    print("===================================")


def get_crop_by_id():
    id=input("Enter Crop Id : ")
    connection=get_connection()
    query="select * from crops where id = %s;"
    cursor=connection.cursor()
    cursor.execute(query,(id,))
    res=cursor.fetchone()

    if res:
        print_crop_by_id(res)
    else:
        print("Crop ID not found!")
    
    cursor.close()
    connection.close()

# to update crop name by id
def update_crop_name():
    id = input("Enter Crop Id for Update : ")
    crop_name = input("Enter New Crop Name : ")

    connection = get_connection()
    query = "update crops set crop_name=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (crop_name, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Name Updated Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()


# to update crop area by id
def update_crop_area():
    id = input("Enter Crop Id for Update : ")
    area = input("Enter New Crop Area : ")

    connection = get_connection()
    query = "update crops set area=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (area, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Area Updated Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()


# to update crop season by id
def update_crop_season():
    id = input("Enter Crop Id for Update : ")
    season = input("Enter New Season : ")

    connection = get_connection()
    query = "update crops set season=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (season, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Season Updated Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()


# to update crop production by id
def update_crop_production():
    id = input("Enter Crop Id for Update : ")
    production = input("Enter New Production : ")

    connection = get_connection()
    query = "update crops set production=%s where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (production, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Production Updated Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()


# to update all crop details
def update_crop_details():
    id = input("Enter Crop Id for Update : ")
    farmer_id = input("Enter Farmer ID : ")
    crop_name = input("Enter New Crop Name : ")
    area = input("Enter New Crop Area : ")
    season = input("Enter New Season : ")
    production = input("Enter New Production : ")

    connection = get_connection()
    query = """update crops 
               set farmer_id=%s, crop_name=%s, area=%s, season=%s, production=%s 
               where id=%s;"""

    cursor = connection.cursor()
    cursor.execute(query, (farmer_id, crop_name, area, season, production, id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Details Updated Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()


# to delete crop by id
def delete_crop_by_id():
    id = input("Enter Crop Id for Delete : ")

    connection = get_connection()
    query = "delete from crops where id=%s;"
    cursor = connection.cursor()
    cursor.execute(query, (id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Crop Deleted Successfully!!!")
    else:
        print("Crop ID not found!")

    cursor.close()
    connection.close()