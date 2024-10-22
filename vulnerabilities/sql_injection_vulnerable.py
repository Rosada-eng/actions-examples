from flask import Flask, request, jsonify
import sqlalchemy

app = Flask(__name__)

connection_string = 'sqlite:///example.db'

@app.route('/example', methods=['GET'])
def get_users():
    # Get the 'user' parameter from the query string
    user = request.args.get("user")
    
    # Create the database connection
    engine = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    
    # Vulnerable SQL query - prone to SQL injection
    result = conn.execute("SELECT * FROM users WHERE user = '" + user + "'")

    # Fetch all results
    users = [row[0] for row in result]
    
    # Close the connection
    conn.close()
    
    # Return the results as JSON
    return jsonify(users=users)

if __name__ == "__main__":
    app.run(debug=True)

"""
    Attack example 1 - retrieve all users data: 
        username_input = "admin' OR '1'='1"

    Attack example 2 - drop table:
        username_input = "'; DROP TABLE users; --"

"""
