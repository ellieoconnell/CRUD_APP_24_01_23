import db

# defining the create order function by pulling the function from the db file
def createOrder(first_name, drink_types, drink_size, cream, drink_amount):
    print(first_name)
    data = db.create_order(first_name, drink_types, drink_size, cream, drink_amount)
    return data

# defining the get all function by pulling the function from the db file
def getAll():
    data = db.check_all_records()
    return data

# defining the find order by id function by pulling the function from the db file
def getOne(id):
    data = db.find_orders_id(id)
    return data

# defining the delete order by id function by pulling the function from the db file
def delOne(id):
    data = db.del_orders_id(id)
    return data

# defining the delete all orders function by pulling the function from the db file
def delAll():
    data = db.del_all_orders()
    return data

# defining the update orders by id function by pulling the function from the db file
def updateOne(id,first_name, drink_types, drink_size, cream, drink_amount):
    data = db.update_by_id(id, first_name, drink_types, drink_size, cream, drink_amount)
    return data 
  