import os
import sqlite3
import pandas as pd

#Set the working directory here
os.chdir(r'C:\Users\audre\OneDrive\Desktop\IBM Python Project\Python Initialized Database')

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'First_Name', 'Last_Name', 'City', 'City_Code']

file_path = r'C:\Users\audre\OneDrive\Desktop\IBM Python Project\Python Initialized Database\INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index = False)
print('Table is ready')