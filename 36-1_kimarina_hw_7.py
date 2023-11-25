import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn



def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)



def insert_product(conn, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)



def update_quantity_by_id(conn, product_id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)



def update_price_by_id(conn, product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_price, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)



def delete_product_by_id(conn, product_id):
    sql = '''DELETE from products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



def select_cheap_and_abundant_products(conn):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



def search_products_by_title(conn, search_term):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{search_term}%',))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)




sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''



connection = create_connection('hw.db')

if connection is not None:
    print('Successfully connected to DB!')
    create_table(connection, sql_to_create_products_table)

    create_table(connection, sql_to_create_products_table)

    insert_product(connection, ('Мыло', 15.99, 50)),
    insert_product(connection, ('Детское мыло', 12.50, 30)),
    insert_product(connection, ('Шампунь', 24.99, 25)),
    insert_product(connection, ('Детский шампунь', 18.75, 40)),
    insert_product(connection, ('Зубная щетка', 22.49, 15)),
    insert_product(connection, ('Зубная паста', 28.99, 20)),
    insert_product(connection, ('Крем', 14.95, 35)),
    insert_product(connection, ('Умывашка', 19.99, 28)),
    insert_product(connection, ('Мочалка', 16.50, 32)),
    insert_product(connection, ('Гель', 17.25, 27)),
    insert_product(connection, ('Порошок', 23.75, 18)),
    insert_product(connection, ('Бальзам', 26.50, 22)),
    insert_product(connection, ('Кондиционер', 21.99, 23)),
    insert_product(connection, ('Губка', 13.49, 38)),
    insert_product(connection, ('Пена для ванны', 20.75, 33)),
    
    
    update_quantity_by_id(connection, 3, 10)
    
    update_price_by_id(connection, 5, 15.99)
    
    delete_product_by_id(connection, 8)
    
    select_all_products(connection)
    
    select_cheap_and_abundant_products(connection)
    
    search_products_by_title(connection, "Product 1")
    
    connection.close()