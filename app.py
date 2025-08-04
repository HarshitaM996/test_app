# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# import mysql.connector # Uncomment this line if you have mysql.connector installed and configured

app = Flask(__name__)
CORS(app) # Enable CORS for all routes, useful for frontend-backend communication

# --- MySQL Database Configuration (Placeholder) ---
# You'll need to replace these with your actual MySQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'your_database_name'
}

# Function to establish database connection
def get_db_connection():
    try:
        # conn = mysql.connector.connect(**DB_CONFIG) # Uncomment this line
        # return conn # Uncomment this line
        print("Database connection (simulated): Connected successfully!") # Placeholder
        return None # Placeholder: In a real app, this would return the connection object
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# --- Routes ---

@app.route('/')
def index():
    """
    Renders the login page from the 'templates' folder.
    """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login requests.
    Expects JSON data with 'username' and 'password'.
    """
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # --- Database Interaction (Simulated for now) ---
    conn = get_db_connection()
    if conn:
        try:
            # In a real application, you would query your 'users' table
            # to verify the username and hashed password.
            # Example (conceptual, do not use directly for production without proper hashing):
            # cursor = conn.cursor(dictionary=True)
            # cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            # user = cursor.fetchone()
            # if user and user['password'] == password: # Replace with password hashing verification
            #     return jsonify({"message": "Login successful!", "user": user['username']}), 200
            # else:
            #     return jsonify({"message": "Invalid credentials"}), 401
            print(f"Simulating login for user: {username}")
            if username == "testuser" and password == "testpass":
                return jsonify({"message": "Login successful!", "user": username}), 200
            else:
                return jsonify({"message": "Invalid credentials (simulated)"}), 401

        except Exception as e:
            print(f"Error during login process: {e}")
            return jsonify({"message": "An internal server error occurred"}), 500
        finally:
            # if conn:
            #     conn.close() # Uncomment this line
            pass # Placeholder
    else:
        # If database connection fails, still provide a simulated response
        print("Could not connect to database, simulating login.")
        if username == "testuser" and password == "testpass":
            return jsonify({"message": "Login successful (simulated)!", "user": username}), 200
        else:
            return jsonify({"message": "Invalid credentials (simulated)"}), 401


# --- Run the Flask Application ---
if __name__ == '__main__':
    # For development, you can run with debug=True
    # In production, use a production-ready WSGI server like Gunicorn or uWSGI
    app.run(debug=True, port=5000)
