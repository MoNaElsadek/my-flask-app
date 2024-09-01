from flask import Flask
import mysql.connector

app = Flask(__name__)

# Replace these with your actual database connection details
db_host = 'db'  # This should match the service name in docker-compose.yml
db_user = 'root'
db_password = 'password'
db_name = 'testdb'

@app.route('/')
def index():
    return "Hello, Ansible and Docker Compose!"

@app.route('/db')
def check_db():
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db = cursor.fetchone()
        conn.close()
        return f"Connected to database: {db}"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/add/<data>', methods=['GET'])
def add_data(data):
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO my_table (column_name) VALUES (%s)", (data,))
        conn.commit()
        conn.close()
        return f"Added data: {data}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

