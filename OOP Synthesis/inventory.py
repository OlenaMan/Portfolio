
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''
    A class representing Shoes.
    Attributes:
        country (str): Shoe origin country.
        code (str): Unique product code.
        product (str): Product name.
        cost (float): Shoe cost
        quantity(int): Product quantity
    '''
    def __init__(self, country, code, product, cost, quantity):
        '''Initialise a Class object.
        Args:
            country (str): Shoe origin country.
            code(str): Unique product code.
            product(str): Product name.
            cost(float): Shoe cost
            quantity(int): Product quantity
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def __str__(self):
        '''
        Returns:
            str: A string representation in the format
                (country, code, product, cost, quantity).
        '''
        return (
            f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")

    def get_cost(self):
        '''
        The code to return the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        The code to return the quantity of the shoes.
        '''
        return self.quantity

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
inventory_file = "/Users/olenamanziuk/Desktop/OOP Synthesis/Tasks/inventory.txt"

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function opens the file inventory.txt
    and reads the data from this file, creates an object and adds the object
    to the the shoe list
    '''
    try:
        with open (inventory_file,"r",encoding="utf-8") as file:

            lines = file.readlines()

        for line in lines[1:]: # Skips the header line
            line = line.strip()
            if line: #ignores empty lines"
                country,code,product,cost,quantity = line.split(",")
                shoe = Shoe(country,code,product,cost,quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File is not found. Please check the path and try again")
    except ValueError as e:
                print(f"Value error. Please check values:{line}\n{e}")

def write_shoes_data():
    with open(inventory_file, "w", encoding="utf-8") as file:
        file.write ("Country,Code,Product,Cost,Quantity, Total Value \n")
        for shoe in shoe_list:
            file.write(str(shoe) + "\n")

def capture_shoes():
    '''
    This function allows a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        country = input("Enter the country of origin: ")
        code = input("Enter the unique product code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the shoe price: "))
        quantity = int(input("Enter the quantity of shoes: "))
        new_shoe = Shoe(country,code,product,cost,quantity)
        shoe_list.append(new_shoe)
        print("---Updated list---:\n")
        view_all()
    except ValueError:
        print(" Entered value is not valid. Please check and repeat. ")

def view_all():
    '''
    This function iterates over the shoe list and
    prints the details of the shoes returned from the __str__
    function. The data is organised in a table format
    by using Python’s tabulate module.
    '''
    table = []

    for shoe in shoe_list:
        table.append([
            shoe.country,
            shoe.code,
            shoe.product,
            shoe.cost,
            shoe.quantity
        ])
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print (tabulate(table, headers = headers, tablefmt="grid"))

def re_stock():
    '''
    This function finds the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. It asks the user if they
    want to add this quantity of shoes and then updates it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("No shoes in stock")
        return

    shoe_low = min(shoe_list, key=lambda shoe:shoe.quantity)
    print("Shoe with the lowest quantity: ")
    print(shoe_low)
    try:
        restock = input("Do you want to add the stock: (yes/no): ").lower()
        if restock == "yes":
            add_quantity = int(input("How many prducts would you like to add? "))
            shoe_low.quantity += add_quantity
            write_shoes_data()
            print("Updated shoe details: \n")
            print(shoe_low)
        else:
            print("No changes made")
    except ValueError:
        print("Invalid input")

def search_shoe(shoe_list):
    '''
     This function searches for a shoe from the list
     using the shoe code and returns this object so that it is printed.
    '''
    shoe_code = input("Enter shoe code you wish to find: ")

    for shoe in shoe_list:
        if shoe.code.lower() == shoe_code.lower():
              print("Shoe was found:")
              print(shoe)
              return shoe
    print("Shoe with provided code was not found")
    return None # If the shoe was not found

def value_per_item():
    '''
    This function calculates the total value for each item.
    The formula is: value = cost * quantity.
    This information is printed on the console for all entries
    '''
    if not shoe_list:
        print("No shoes in stock")
        return

    table = []
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        table.append([
            shoe.country,
            shoe.code,
            shoe.product,
            shoe.cost,
            shoe.quantity,
            f"${value:.2f}"
        ])
    headers = ["Country", "Code", "Product", "Cost", "Quantity", "Total Value"]
    print(tabulate(table, headers=headers,tablefmt="grid" ))

def highest_qty():
    '''
    This code determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''
    if not shoe_list:
        print("No shoes in stock")
        return

    shoe_high = max(shoe_list, key=lambda shoe:shoe.quantity)
    print("Shoe with the higest quantity is for sale: ")
    print(shoe_high)

#==========Main Menu=============
'''
The menu to execute each function above.
'''
def menu():
    read_shoes_data() # loads shoe data from the file
    while True:
        print("\n ----Main Menu----")
        print("1. View all shoes")
        print("2. Capture shoes")
        print("3. Re-stock shoes")
        print("4. Find shoes by code")
        print("5. Display value per item")
        print("6. Find the highest quantity in stock")
        print("7. Exit")
        choice = input("Please enter your choice:1,2,3,4,5,6 or 7 ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
        choice = int(choice)
        if choice == 1:
            view_all()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            re_stock()
        elif choice == 4:
            search_shoe(shoe_list)
        elif choice == 5:
            value_per_item()
        elif choice == 6:
            highest_qty()
        elif choice == 7:
            print("Exit. See you next time!")
            break
        else:
            print("The choice is invalid. Please try again")
menu()
