import sqlite3


class Database():
  def __init__(self):
    self.connection = sqlite3.connect('insert path to database'+'name of your database')
    self.cursor = self.connection.cursor()

  
  def test_connection(self):
    sqlite_select_Query = "SELECT sqlite_version();"
    self.cursor.execute(sqlite_select_Query)
    record = self.cursor.fetchall()
    print(f"Connected successfully. SQLite Database Version is: {record}")

  def get_all_users(self):
    query = "SELECT name, adress, city FROM customers"
    self.cursor.execute(query)
    record = self.cursor.fetchall()
    return record
    
  def get_user_adress_by_name(self, name):
    query = f"SELECT adress, city, postalCode, country FROM customers WHERE name = 'name'"
    self.cursor.execute(query)
    record = self.cursor.fetchall()
    return record

  def update_product_qnt_by_id(self, product_id, qnt):
    query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
    self.cursor.execute(query)
    seelf.connection.commit()

  def select_product_qnt_by_id(self, product_id):
    query = f"SELECT quantity FROM products WHERE id = {product_id}"
    self.cursor.execute(query)
    record = self.cursor.fetchall()
    return record

  def insert_product(self, product_id, name, description, qnt):
    query = f"INSERT INTO products (id, name, description, quantity) \
        VALUES ({product_id}, '{name}', '{description}', {qnt})"
      self.cursor.execute(query)
      seelf.connection.commit()
  
