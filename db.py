import sqlite3 as sql

# creating connection to already created SQL db
def set_up_conn(orders_db):
    conn = sql.connect(orders_db)
    return conn

# defining cursor variable to use to navigate through db table
def set_up_cursor():
    cursor = set_up_conn.cursor()
    return cursor

# defining SQL table for the db
def set_up_table():
    sql_file = open("order.sql")
    sql_string = sql_file.read()
    set_up_cursor.executescript(sql_string)

# defining query function to fetch data from table 
def run_query(query):
    data = set_up_cursor.execute(query).fetchall()
    return data

# defining function that allows the user to input new orders into a table
def create_order(first_name, drink_type, drink_size, cream, drink_amount):
    query = f"INSERT INTO orders (first_name, drink_type, drink_size, cream, drink_amount) VALUES ({first_name}, {drink_type}, {drink_size}, {cream}, {drink_amount});"
    run_query(query)
    return True

# defining function that can read all the data from the db table upon request
def check_all_records():
    query = "SELECT * FROM orders_db;"
    data = run_query(query)
    return True

# defining function that allows users to navigate through the table by id
def find_orders_id(id):
    query = "SELECT order_id FROM orders_db WHERE orders_id = {id};"
    data = run_query(query)
    return True

# defining function that allows users to delete entries by id
def del_orders_id(id):
    query = "DELETE FROM orders WHERE order_id = {id};"
    data = run_query(query)
    return True

# defining function that allows users to delete all entries
def del_all_orders():
    query = "DELETE FROM orders WHERE order_id > 0;"
    data = run_query(query)
    return True

# defining function that allows user to update orders by id 
def update_by_id(id):
    query = "UPDATE orders_db SET first_name = {first_name}, drink_type = {drink_types}, drink_size = {drink_size}, cream = {cream}, drink_amount = {drink_amount} WHERE order_id = {id};"
    data = run_query(query)
    return True

# defining function to commit all changes to db when they are made 
def commitChanges():
    set_up_conn.commit()

set_up_conn.commit()