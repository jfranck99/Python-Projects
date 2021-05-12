# Create Employee superclass
class Employee:

    # Initialize attributes of Employee
    def __init__(self, name, number):
        
        self.__name = name

        self.__number = number

    # Modify attribute values
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


    # Display attributes
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    
# Create ProductionWorker subclass by using Employee superclass as a parameter
class ProductionWorker(Employee):

    # Initialize ProductionWorker attributes
    def __init__(self, name, number, shift, pay):

        # Calls superclass __init__ method to initialise first 4 attributes
        Employee.__init__(self, name, number)

        # Initializes specific ProductionWorker attributes
        self.__shift = shift
        self.__pay = pay

    # Modify values of ProductionWorker attributes
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    # Display ProductionWorker attributes
    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay

def main():

    # Get ProductionWorker information

    name = input('What is your name: ')
    number = input('What is your employee number: ')
    shift_num = int(input('Which shift do you work? (1 or 2): '))
    pay = input('What is you hourly pay rate: ')

    # Is shift day or night
    if shift_num == 1:
        shift = 'Day'
    else:
        shift = 'Night'

    # Create instance of ProductionWorker
    my_ProductionWorker = ProductionWorker(name, number, shift, pay)
                          

    # Re-display entered data

    print('')
    print('     ProductionWorker Information     ')
    print('--------------------------------------')
    print('Name:', my_ProductionWorker.get_name())
    print('number:', my_ProductionWorker.get_number())
    print('Shift:', my_ProductionWorker.get_shift())
    print('Pay:', my_ProductionWorker.get_pay())

    
main()
