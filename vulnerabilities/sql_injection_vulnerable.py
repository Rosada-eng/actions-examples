from flask import Flask, request, jsonify
import sqlalchemy

app = Flask(__name__)

# Replace with your actual connection string
connection_string = 'sqlite:///example.db'

@app.route('/example', methods=['GET'])
def get_users():
    # Get the 'user' parameter from the query string
    user = request.args.get("user")
    
    # Create the database connection
    engine = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    
    # Vulnerable SQL query - prone to SQL injection
    result = conn.execute("SELECT user FROM users WHERE user = '" + user + "'")

    # Fetch all results
    users = [row[0] for row in result]

    # Close the connection
    conn.close()

    # Return the results as JSON
    return jsonify(users=users)

if __name__ == "__main__":
    app.run(debug=True)