import sqlite3

def get_user_data(username):
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)  # This allows SQL injection!
    result = cursor.fetchall()
    
    conn.close()
    return result

# Example of potential SQL injection attempt
username_input = input("Enter your username: ")
print(get_user_data(username_input))