# 🌾 Smart Farmer Management System

## 📌 Project Overview

The **Smart Farmer Management System** is a beginner-friendly Python and MySQL project designed to manage farmer and agriculture-related information in an organized way.

The system allows users to manage:

* 👨‍🌾 Farmer details
* 🌱 Crop details
* 💰 Farming expenses
* 🛒 Crop sales
* 📊 Farmer reports

The main purpose of this project is to store agricultural information in a database and easily perform **Create, Read, Update, and Delete (CRUD)** operations.

---

## 🎯 Main Purpose

The main purpose of this project is to digitally manage farmer information, crop production, farming expenses, and crop sales.

The system also provides a **Farmer Report** that displays important information such as:

* Farmer details
* Crop details
* Production
* Total expenses
* Total sales
* Profit

### Profit Calculation

```text
Profit = Total Sales - Total Expenses
```

---

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **PyMySQL**
* **SQL**

### SQL Concepts Used

* DDL
* DML
* Constraints
* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* JOIN
* GROUP BY
* ORDER BY
* Aggregate Functions such as `SUM()`

---

## 📂 Project Structure

```text
Smart-Farmer-Management-System/
│
├── main.py
├── db.py
├── farmers.py
├── crop.py
├── expenses.py
├── sales.py
├── reports.py
└── README.md
```

---

## 👨‍🌾 Farmer Management

The farmer module allows the user to:

* Add a new farmer
* View all farmers
* View a farmer by ID
* Update farmer name
* Update village
* Update phone number
* Update all farmer details
* Delete a farmer

---

## 🌱 Crop Management

The crop module allows the user to:

* Add a new crop
* View all crops
* View crop by ID
* Update crop name
* Update crop area
* Update crop season
* Update crop production
* Update all crop details
* Delete a crop

---

## 💰 Expense Management

The expense module allows the user to:

* Add an expense
* View all expenses
* View expense by ID
* Update expense type
* Update expense amount
* Update all expense details
* Delete an expense

Example expenses:

```text
Seeds
Fertilizer
Labour
Pesticides
```

---

## 🛒 Sales Management

The sales module allows the user to:

* Add a new sale
* View all sales
* View sale by ID
* Update quantity
* Update price per kg
* Update all sale details
* Delete a sale

The total sale amount is calculated using:

```text
Total Amount = Quantity × Price Per Kg
```

---

## 📊 Farmer Report

The report module provides a summary of a farmer's agricultural information.

The report displays:

```text
Farmer Name
Village
Phone
Crop Name
Crop Area
Season
Production
Total Expenses
Total Sales
Profit
```

Example:

```text
========== FARMER REPORT ==========

Farmer Name     : Gopi
Village         : Urivi
Phone           : XXXXXXXXXX
Crop Name       : Black Gram
Crop Area       : 2 Acres
Season          : Rabi
Production      : 1600 kg
Total Expenses  : ₹10000
Total Sales     : ₹120000
Profit          : ₹110000

===================================
```

---

## 🗄️ Database

The project uses MySQL to store the information.

Main tables:

```text
farmers
crops
expenses
sales
```

The tables are connected using farmer IDs and crop IDs.

---

## ▶️ How to Run the Project

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install PyMySQL

Open the terminal and run:

```bash
pip install pymysql
```

### 3. Create the MySQL Database

Create your database and required tables in MySQL.

### 4. Configure Database Connection

Update the database username, password and database name in:

```text
db.py
```

### 5. Run the Project

Open the project folder in the terminal and run:

```bash
python main.py
```

---

## 📋 Main Menu

The application provides the following options:

```text
Select 1 for farmers table
Select 2 for crops table
Select 3 for expenses table
Select 4 for sales table
Select 5 for Farmer Report
Select 6 For Exit
```

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Python functions
* Python modules
* MySQL database connectivity
* CRUD operations
* SQL queries
* DDL and DML
* SQL constraints
* JOIN
* GROUP BY
* ORDER BY
* Aggregate functions
* Database relationships
* Basic project structure
* Menu-driven Python applications

---

## 🚀 Future Improvements

Some possible future improvements are:

* Add login functionality
* Add input validation
* Add multiple crop reports
* Add monthly expense reports
* Add graphical reports
* Create a web interface
* Add farmer search functionality
* Generate PDF reports

---

## 👨‍💻 Author

**Gopi**

### 📌 Project Type

**Python + MySQL Database Project**

---

⭐ If you find this project useful, feel free to explore the code and give feedback.
