import mysql.connector
# 3306
host = "127.0.0.1"
user = "local_shreyash"
password = "@Cj695123"
database = "class2_db"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def create_connection():
    conn = None;
    try:
        conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
        print("You have a connection with SQL Buddy !!!")
    except Error as e:
        print(e)
    return conn

def get_schema_representation():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    # for row in tables:
    #     print(row[0])

    db_schema = {}

    for table in tables:
        table_name = table[0]

        cursor.execute(f"DESCRIBE `{table_name}`;")
        columns = cursor.fetchall()

        column_details = {}

        for column in columns:
            column_name = column[1]
            column_type = column[2]
            column_details[column_name] = column_type

        db_schema[table_name] = column_details

    conn.close()
    return db_schema

# if __name__ == "__main__":
#     print(get_schema_representation())

# if connection.is_connected():
#     print("Connected to MYSQL database")
# else:
#     print("Failed to connect to MYSQL database")


# cursor = connection.cursor()

# query = "SELECT * FROM employees"
# cursor.execute(query)

# results = cursor.fetchall()

# for row in results:
#     print(row)

# cursor.close()