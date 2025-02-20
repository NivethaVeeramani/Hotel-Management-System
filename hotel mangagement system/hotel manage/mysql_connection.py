import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='Niviveera@123',  
            database='hotel_db'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_customer(connection, name, phone, email):
    """Insert a new customer into the customers table."""
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, phone, email))
        connection.commit()
        print("Customer added successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_customers(connection):
    """Retrieve and display all customers."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        print("Customers:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def book_room(connection, customer_id, room_id, check_in, check_out, total_price):
    """Insert a booking into the bookings table."""
    try:
        cursor = connection.cursor()
        query = """INSERT INTO bookings (customer_id, room_id, check_in, check_out, total_price) 
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (customer_id, room_id, check_in, check_out, total_price))
        connection.commit()
        print("Room booked successfully!")
    except Error as e:
        print(f"Error: {e}")

def view_bookings(connection):
    """Retrieve and display all bookings with customer and room details."""
    try:
        cursor = connection.cursor()
        query = """SELECT 
                       b.booking_id, c.name AS customer_name, r.room_type, 
                       b.check_in, b.check_out, b.total_price
                   FROM bookings b
                   JOIN customers c ON b.customer_id = c.customer_id
                   JOIN rooms r ON b.room_id = r.room_id"""
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Bookings:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def view_rooms(connection):
    """Retrieve and display all room details."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()
        print("Rooms:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def main():
    connection = create_connection()
    if connection:
        # View all rooms
        view_rooms(connection)
        
        # Add a customer
        create_customer(connection, "John Doe", "1234567890", "john.doe@example.com")
        
        # View customers
        view_customers(connection)
        
        # Book a room
        book_room(connection, 1, 2, "2025-01-15", "2025-01-17", 3000.00)
        
        # View bookings
        view_bookings(connection)
        
        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
