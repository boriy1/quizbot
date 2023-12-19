import sqlite3 as sq

def create_table():
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS foods_list (
        title VARCHAR(255),
        price INT,
        description TEXT,
        categories VARCHAR(255))""")

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS users (
        user_id VARCHAR(255),
        lang VARCHAR(255),
        phone_number VARCHAR(255))""")

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS shopping_cart (
        user_id VARCHAR(255),
        title VARCHAR(255),
        price INT)""")
    
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS locations (
        user_id VARCHAR(255),
        geolocation VARCHAR(255),
        longitude VARCHAR(255),
        latitude VARCHAR(255))""")
    
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS categories (
        title VARCHAR(255))""")
    
    connect.commit()
    connect.close()


def get_user(user_id):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT * FROM users WHERE user_id = {str(user_id)}""").fetchone()

    connect.commit()
    connect.close()

    return user


def get_locations(user_id):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT * FROM locations WHERE user_id = {str(user_id)}""").fetchall()

    connect.commit()
    connect.close()

    return user


def get_products_(user_id):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT * FROM shopping_cart WHERE user_id = {str(user_id)}""").fetchall()

    connect.commit()
    connect.close()

    return user


def get_products(catagory):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT * FROM foods_list WHERE categories = '{str(catagory)}'""").fetchall()

    connect.commit()
    connect.close()

    return user


def get_products_all():
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT * FROM foods_list""").fetchall()

    connect.commit()
    connect.close()

    return user


def get_categories():
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    user = cursor.execute(f"""SELECT title FROM categories""").fetchall()

    connect.commit()
    connect.close()

    return user


def add_location(id, locations, long, lat):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""INSERT INTO locations (user_id, geolocation, longitude, latitude) VALUES (?, ?, ?, ?)""", (str(id), locations, str(long), str(lat)))

    connect.commit()
    connect.close()


def add_user(id, number, lang):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""INSERT INTO users (user_id, lang, phone_number) VALUES (?, ?, ?)""", (str(id), lang, number))

    connect.commit()
    connect.close()
    
    
def add_product_to_cart(id, title, price):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""INSERT INTO shopping_cart (user_id, title, price) VALUES (?, ?, ?)""", (str(id), title, int(price)))

    connect.commit()
    connect.close()
    
    
def update_lang(id, lang):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""UPDATE users SET lang = ? WHERE user_id = ?""", (lang, str(id)))

    connect.commit()
    connect.close()


def delete_cart(id):
    connect = sq.connect('kfc.db')
    cursor = connect.cursor()

    cursor.execute(f"""DELETE FROM shopping_cart WHERE user_id = {str(id)}""")

    connect.commit()
    connect.close()