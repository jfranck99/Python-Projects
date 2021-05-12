# Create Person superclass
class Person:

    # Initialize attributes of Person
    def __init__(self, name, address, phone):
        
        self.__name = name

        self.__address = address

        self.__phone = phone

    # Modify attribute values
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # Display attributes
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
# Create Customer subclass by using Person superclass as a parameter
class Customer(Person):

    # Initialize Customer attributes
    def __init__(self, name, address, phone, customer_num, mail_list):

        # Calls superclass __init__ method to initialise first 4 attributes
        Person.__init__(self, name, address, phone)

        # Initializes specific Customer attributes
        self.__customer_num = customer_num
        self.__mail_list = mail_list

    # Modify values of Customer attributes
    def set_customer_num(self, customer_num):
        self.__customer_num = customer_num

    def set_mail_list(self, mail_list):
        self.__mail_list = mail_list

    # Display Customer attributes
    def get_num(self):
        return self.__customer_num

    def get_mail_list(self):
        return self.__mail_list

def main():

    # Get customer information

    name = input('Name: ')
    address = input('Address: ')
    phone = input('Phone: ')
    customer_num = input('Customer number: ')
    mail = input('Include in mailing list? (y/n): ')

    # True or false for mailing list

    if mail.lower() == 'y':
        mail_list = True
    else:
        mail_list = False

    # Create instance of Customer

    my_customer = Customer(name, address, phone,
                           customer_num, mail_list)

    # Re-display entered data

    print('     Customer Information     ')
    print('------------------------------')
    print('Name:', my_customer.get_name())
    print('Address:', my_customer.get_address())
    print('Phone:', my_customer.get_phone())
    print('Customer number:', my_customer.get_num())
    print('Mailing List:', my_customer.get_mail_list())

    
main()
