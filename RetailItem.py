class RetailItem:

    # Initialize the attributes
    def __init__(self, desc, units, price):

        self.__desc = desc

        self.__units = units

        self.__price = price


    # Sets the desc of the RetailItem
    def set_desc(self, desc):
        self.__desc = desc

    # Sets the units of the RetailItem
    def set_units(self, units):
        self.__units = units

    # Sets the price of the RetailItem
    def set_price(self, price):
        self.__price = price

    # Returns the desc of the RetailItem
    def get_desc(self):
        return self.__desc

    # Returns the units of the RetailItem
    def get_units(self):
        return self.__units

    # Returns the price of the RetailItem
    def get_price(self):
        return self.__price



def main():

        # Item #1 attributes
        desc = "Jacket        "
        units = 12
        price = 59.95

        # Create first instance of the retailItem class
        item1 = RetailItem(desc, units, price)
        
        # Item #2 attributes
        desc = "Designer Jeans"
        units = 40
        price = 34.95

        # Create second instance of the retailItem class
        item2 = RetailItem(desc, units, price)
        
        # Item #3 attributes
        desc = "Shirt         "
        units = 20
        price = 24.95
        
        # Create third instance of the retailItem class
        item3 = RetailItem(desc, units, price)

        # Re-display information
        print("------- Retail Item Info -------")
        print("Item #1 |", item1.get_desc(), "|", item1.get_units(), "|", item1.get_price())
        print("Item #2 |", item2.get_desc(), "|", item2.get_units(), "|", item2.get_price())
        print("Item #3 |", item3.get_desc(), "|", item3.get_units(), "|", item3.get_price())

main()
