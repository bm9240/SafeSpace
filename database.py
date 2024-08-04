import sqlite3

# Function to create the messages table if it doesn't exist
def create_table():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a username column to the messages table
def add_username_column():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            ALTER TABLE messages
            ADD COLUMN username TEXT
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        print("Username column already exists")
    conn.close()

# Function to add a new message to the database
def add_message(topic, username, message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (topic, username, message) VALUES (?, ?, ?)", (topic, username, message))
    conn.commit()
    conn.close()

# Function to retrieve messages from the database
def get_messages(topic=None):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    if topic:
        cursor.execute("SELECT * FROM messages WHERE topic = ?", (topic,))
    else:
        cursor.execute("SELECT * FROM messages")
    results = cursor.fetchall()
    conn.close()
    return results

# Function to run any SQL query (for admin or special purposes)
def run_sql_query(query):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Initialize the database table
create_table()
add_username_column()