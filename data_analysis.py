import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',  # Change if your server is remote
    user='root',  # Your MySQL username
    password='janani',  # Your MySQL password
    database='employee_data'  # Name of your database
)

# Fetch data from the employees table
query = "SELECT * FROM humanresources;"
data = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the data
print(data.head())
# Check for missing values
print(data.isnull().sum())

# Drop rows with any missing values (if necessary)
data.dropna(inplace=True)

# Convert date columns to datetime format
data['Birthdate'] = pd.to_datetime(data['Birthdate'])
data['Hiredate'] = pd.to_datetime(data['Hiredate'])
data['Termdate'] = pd.to_datetime(data['Termdate'], errors='coerce')  # Handle NaT for employees not terminated

# Display the cleaned data
print(data.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

# Visualization 1: Salary Distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['Salary'], bins=30, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# Optional: Export cleaned data to a CSV file
data.to_csv('cleaned_employee_data.csv', index=False)

