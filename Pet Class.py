class Pet:

    # Initialize the 3 attributes
    def __init__(self, name, animal_type, age):

        self.__name = name

        self.__animal_type = animal_type

        self.__age = age

    # Sets the name of the pet
    def set_name(self, name):
        self.__name = name

    # Sets the animal_type of the pet
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Sets the age of the pet
    def set_age(self, age):
        self.__age = age

    # Returns the name of the pet
    def get_name(self):
        return self.__name

    # Returns the animal_type of the pet
    def get_type(self):
        return self.__animal_type

    # Returns the age of the pet
    def get_age(self):
        return self.__age



def main():
    
    # Get pet info from user
    name = input("What is the name of your pet? ")

    animal_type = input("What kind of animal is your pet? ")

    age = input("How old is your pet? ")
    
    # Create an instance of the Pet class
    my_pet = Pet(name, animal_type, age)

    # Re-display information
    print("------- Pet Info -------")
    print("Name:", my_pet.get_name())
    print("Animal type:", my_pet.get_type())
    print("Age:", my_pet.get_age())

main()
