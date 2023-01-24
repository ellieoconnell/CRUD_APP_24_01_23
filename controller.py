from service import service
from db import db

# defining while loop that loops through all menu options
def startApp():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(orderInput())
        if choice == "2":
            print(oneOrder())
        if choice == "3":
            print(allOrders())
        if choice == "4":
            print(orderUpdate())
        if choice == "5":
            print(oneOrderdel())
        if choice == "6":
            print(allOrdersdel())
        else:
            exit = True
            db.commitChanges()

# defining the function called when the user selects option 1 
def orderInput():
    return service.createOrder()

# defining the function called when the user selects option 2
def oneOrder():
    id = input("Please enter id to read: ")
    return service.getOne(id)

# defining the function called when the user selects option 3
def allOrders():
    return service.getAll()

# defining the function called when the user selects option 4
def orderUpdate():
    id = input("Please enter id to update: ")
    return service.updateOne(id)

# defining the function called when the user selects option 5
def oneOrderdel():
    id = input("Please enter id you would like to delete: ")
    return service.delOne(id)

# defining the function called when the user selects option 6
def allOrdersdel():
    service.delAll()

# menu displayed when CRUD app is run
menu = (
    """
    Welcome to the QA Cafe, what would you like to do? 
    1. Create an order
    2. Read an order
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    7. Exit
    """
)

startApp()
