import os
import pymysql

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': 3306 
}

def validate_table_structure():
    expected_columns = {'id', 'location', 'date', 'temperature', 'precipitation', 'humidity'}
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("DESCRIBE ClimateData")
            columns = cursor.fetchall()
            actual_columns = {column[0] for column in columns}
            if expected_columns.issubset(actual_columns):
                print("Table structure is correct.")
            else:
                print("Table structure is incorrect. Missing columns:", expected_columns - actual_columns)
    finally:
        connection.close()

def validate_humidity_column():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM ClimateData LIKE 'humidity'")
            result = cursor.fetchone()
            if result:
                print("Humidity column exists.")
            else:
                print("Humidity column does not exist.")
    finally:
        connection.close()

def validate_insert_query():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ClimateData WHERE location = 'Paris' AND date = '2023-01-02' AND temperature = 10.0 AND humidity = 75 AND precipitation = 65")
            result = cursor.fetchone()
            if result:
                print("Insert query validation passed.")
            else:
                print("Insert query validation failed.")
    finally:
        connection.close()

def validate_concurrent_queries():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ClimateData WHERE location = 'Paris'")
            insert_result = cursor.fetchone()
            cursor.execute("SELECT * FROM ClimateData WHERE location = 'Toronto' AND humidity = 60")
            update_result = cursor.fetchone()
            if insert_result:
                print("Insert query executed successfully.")
            else:
                print("Insert query failed.")
            if update_result:
                print("Update query executed successfully.")
            else:
                print("Update query failed.")
    finally:
        connection.close()

def main():
    validate_table_structure()
    validate_humidity_column()
    validate_insert_query()
    validate_concurrent_queries()

if __name__ == "__main__":
    main()