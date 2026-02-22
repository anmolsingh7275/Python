# import mysql.connector
import mysql.connector 

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chauhan@2002",
          database="student_db"
)

print("Connected Successfully!")

cursor = conn.cursor()

# sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
# values = ("Anmol", 21, "BCA")

# cursor.execute(sql, values)

# conn.commit()

cursor.execute("SELECT * FROM students")

result = cursor.fetchall()

for row in result:
    print(row)
#Update The  Data

    

sql = "UPDATE students SET age = %s WHERE name = %s"
values = (22, "Anmol")

cursor.execute(sql, values)

conn.commit()

print("Data Updated Successfully!")

#DELETE DATA

sql = "DELETE FROM students WHERE name = %s"
values = ("Anmol",)

cursor.execute(sql, values)

conn.commit()

print("Data Deleted Successfully!")

conn.close()