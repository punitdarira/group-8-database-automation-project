import pymysql

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': 3306 
}

def insert_query(cursor):
    cursor.execute("INSERT INTO ClimateData (location, date, temperature, humidity) VALUES ('Paris', '2023-01-02', 10.0, 75)")
    print("Insert Query Executed Successfully!")

def select_query(cursor):
    cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
    results = cursor.fetchall()  # Fetch all results
    for row in results:
        print(row)

def update_query(cursor):
    cursor.execute("UPDATE ClimateData SET humidity = 60 WHERE location = 'Toronto'")
    print("Update Query Executed Successfully!")

def main():
    # Create the connection and cursor once, and pass the cursor to each query
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            insert_query(cursor)
            select_query(cursor)
            update_query(cursor)
            connection.commit()  # Save any changes after the queries
    finally:
        connection.close()  # Always close the connection

if __name__ == "__main__":
    main()
