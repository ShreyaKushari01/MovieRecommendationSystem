import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",  # Update with your MySQL password
        database="movie_recommendation"
    )

# Route to home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to get movie recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['genre']
    db = connect_db()
    cursor = db.cursor()

    # Simple recommendation query (You can modify logic to be more complex)
    query = f"SELECT * FROM movies WHERE genre = '{user_input}'"
    cursor.execute(query)
    movies = cursor.fetchall()

    db.close()

    return render_template('index.html', movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
