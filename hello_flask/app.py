from flask import Flask
import MySQLdb
import time

app = Flask(__name__)

def connect_to_db():
    while True:
        try:
            db = MySQLdb.connect(
                host="mydb",    # Hostname of the MySQL container (service name)
                user="root",    # Username
                passwd="my-secret-pw",  # Password
                db="mysql"      # Database name
            )
            return db
        except MySQLdb.OperationalError as e:
            print(f"Database not ready, retrying in 2 sec... ({e})")
            time.sleep(2)

@app.route('/')
def hello_world():
    db = connect_to_db()
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

