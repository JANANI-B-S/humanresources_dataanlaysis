import pandas as pd
import mysql.connector

# Load CSV file
data = pd.read_csv('E:\\data anlysis\\HumanResources.csv', delimiter=';')

# Convert Employee_ID to numeric, forcing errors to NaN
data['Employee_ID'] = pd.to_numeric(data['Employee_ID'], errors='coerce')

# Drop rows with NaN values in Employee_ID
data.dropna(subset=['Employee_ID'], inplace=True)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',  # Change if your server is remote
    user='root',
    password='janani',
    database='employee_data'
)

cursor = conn.cursor()

# Insert data into the table
for index, row in data.iterrows():
    try:
        cursor.execute("""
        INSERT INTO employees (Employee_ID, First_Name, Last_Name, Gender, State, City, 
        Education_Level, Birthdate, Hiredate, Termdate, Department, Job_Title, Salary, Performance_Rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    except mysql.connector.Error as err:
        print(f"Error at row {index}: {err}")

conn.commit()
cursor.close()
conn.close()

print("Data loading complete.")


