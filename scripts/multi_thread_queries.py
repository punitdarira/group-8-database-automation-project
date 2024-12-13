import os
import pymysql
import threading

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': 3306 
}

def insert_query():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO ClimateData (location, date, temperature, humidity) VALUES ('Paris', '2023-01-02', 10.0, 75)")
            connection.commit()
            print("Insert Query Executed Successfully!")
    finally:
        connection.close()

def select_query():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
            results = cursor.fetchall()
            for row in results:
                print(row)
    finally:
        connection.close()

def update_query():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE ClimateData SET humidity = 60 WHERE location = 'Toronto'")
            connection.commit()
            print("Update Query Executed Successfully!")
    finally:
        connection.close()

def main():
    insert_thread = threading.Thread(target=insert_query)
    select_thread = threading.Thread(target=select_query)
    update_thread = threading.Thread(target=update_query)

    insert_thread.start()
    select_thread.start()
    update_thread.start()

    insert_thread.join()
    select_thread.join()
    update_thread.join()

if __name__ == "__main__":
    main()