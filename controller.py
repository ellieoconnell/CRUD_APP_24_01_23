import service
import db

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
    name = input("Please enter name of customer: ")
    drink = input("Please enter the type of drink the customer wants: ")
    size = input("Please enter the size of the drink the customer wants: ")
    extra = input("Did the customer want cream? True or False: ")
    amount = input("How many drinks did the customer order?: ")
    return service.createOrder(name, drink, size, extra, amount)

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
    name = input("Please enter new name of customer: ")
    drink = input("Please enter the new type of drink the customer wants: ")
    size = input("Please enter the new size of the drink the customer wants: ")
    extra = input("Did the customer want cream? True or False: ")
    amount = input("How many drinks did the customer order?: ")
    return service.updateOne(id, name, drink, size, extra, amount)

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
    3. Read all orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    7. Exit
    """
)

startApp()
