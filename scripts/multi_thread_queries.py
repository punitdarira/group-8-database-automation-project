import threading
import mysql.connector

def insert_data():
    conn = mysql.connector.connect(host='group-8-automated-mysql-server.mysql.database.azure.com', user='group8', password='Secret55', database='project_db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('Vancouver', '2024-02-01', 7.1, 12, 80.3)")
    conn.commit()
    conn.close()

def select_data():
    conn = mysql.connector.connect(host='group-8-automated-mysql-server.mysql.database.azure.com', user='group8', password='Secret55', database='project_db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
    for row in cursor.fetchall():
        print(row)
    conn.close()

threads = []
for _ in range(3):
    t1 = threading.Thread(target=insert_data)
    t2 = threading.Thread(target=select_data)
    threads.extend([t1, t2])

for t in threads:
    t.start()

for t in threads:
    t.join()
