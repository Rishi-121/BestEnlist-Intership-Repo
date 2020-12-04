import mysql.connector as mysql

pythonDataTypes = [
    ("int", 1),
    ("float", "1.5"),
    ("complex", "1 + 2j"),
    ("str", "BestEnlist Python Development"),
    ("list", "[1, 2, 3, 4, 5]"),
    ("tuple", "(1, 2, 3, 4, 5)"),
    ("bool", "True"),
    ("set", "{1, 2, 3, 4, 5}"),
    ("dict", "{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}")
]

conn = mysql.connect(host="localhost", user="root",
                     password="", database="bepythondb", port="3308")

cursor = conn.cursor()

insert_query = "INSERT INTO datatypes(datatype,example) VALUES(%s, %s)"

cursor.executemany(insert_query, pythonDataTypes)

conn.commit()

if cursor:
    print("Data inserted successfully")
    select_query = "SELECT * FROM datatypes"
    cursor.execute(select_query)
    for data in cursor:
        print(data)
else:
    print("Error")

conn.close()
