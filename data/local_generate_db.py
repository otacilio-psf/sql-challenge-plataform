import requests
import zipfile
import sqlite3
import io

def download_chinook_db():
    url = "https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip"

    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall("data")
        print("DB downloaded successfully")
    else:
        print("Failed to download DB")

def solution_table_1():
    solution_table_query = r"""
    CREATE TABLE solution_1 AS
    SELECT
    	c.Country,
    	CAST(ROUND(SUM(i.Total), 2) AS REAL) AS Total
    FROM customers c
    JOIN invoices i
    	ON c.CustomerId = i.CustomerId
    WHERE c.Country like '%u%'
    GROUP BY c.Country
    HAVING SUM(i.Total) > 100
    """
    cursor = conn.cursor()
    cursor.execute(solution_table_query)
    cursor.close()
    print("Solution table 1 created sucessfuly")

if __name__ == "__main__":
    download_chinook_db()

    conn = sqlite3.connect('data/chinook.db')
    
    solution_table_1()

    conn.commit()
    conn.close()