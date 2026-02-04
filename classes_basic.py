#make a class called restaurant with name and couisine type and also make two methods (1)discribe restaurant (2)open_restaurant


class restaurant():
    def __init__(self ,restaurant_name ,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cusine_type=cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} And cuisine are {self.cusine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open now")
    
karachi=restaurant('coconut groove','Angolan cuisine')
karachi.describe_restaurant()
karachi.open_restaurant()


#make a class called user.create two attributes called first name and last name 
#and then create several other attributes that are typically stored in a usre profile 
#make a method called describe_user() that print a summary of the user information
#make another method called greet user()that print a personalized greeting to the user

class user():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"The first name of the user is {self.first_name} and the last name of the user is {self.last_name}")
    def greet_user(self):
        print(f"Hello {self.first_name.title().strip()+self.last_name} wellcome!")

fahad=user('shah','fahad')
fahad.describe_user()
fahad.greet_user()


#Add number of served as instance and then write a method to print it
#then change initial value and print it again

class restaurant():
    def __init__(self ,restaurant_name ,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cusine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} And cuisine are {self.cusine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open now")
    def set_number_served(self):
        print(f"This restaurant serve {self.number_served} People Today")
    
karachi=restaurant('coconut groove','Angolan cuisine')
karachi.describe_restaurant()
karachi.open_restaurant()
karachi.set_number_served()
karachi.number_served=10
karachi.set_number_served()

#Add atribute login attempt
#write a method called increament login attempt that increase login attempt by 1
#another method called reset login attempt to reset login attempt to 0

class user():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempt=0
    def describe_user(self):
        print(f"The first name of the user is {self.first_name} and the last name of the user is {self.last_name}")
    def greet_user(self):
        print(f"Hello {self.first_name.title().strip()+self.last_name} wellcome!")
    def reset_login_attempt(self):
        print(f"The login attempt are back to zero")
    def increament_login_attempt(self,per_attempt):
        self.login_attempt+=per_attempt
        print(self.login_attempt)

fahad=user('shah','fahad')
fahad.describe_user()
fahad.greet_user()
fahad.increament_login_attempt(4)
fahad.reset_login_attempt()
fahad.increament_login_attempt(4)


# use instance as an attribute 
# make parent class car 
# make child class which inherit from car 
# make a sperate class for battery 
# called spererate calss method in electric car
class car():
    def __init__(self ,name ,model ,year):
        self.name=name
        self.model=model
        self.year=year

    def condition(self):
        print(f"Car name {self.name} is Running")

    def gas(self):
        print(f"Car name {self.name} need gas tu run")
class battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"The size of the battery is {self.battery_size}")
        
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message=f"this car can go {str(range)}"
        message+="Miles on full charge"
        print(message)
class electric_car(car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery=battery()
    def condition(self):
        return super().condition()
    def gas(self):
        print(f"This i electric car and it donot need gas to run")


car1=electric_car('tesla','l288','2009')

car1.condition()
car1.gas()
car1.battery.describe_battery()
car1.battery.get_range()

# An ice cream stand is a specific kind of resturant
# Write a class called Ice creamStand that inherts form the restaurant class (We already wrote)
# Add an attribute called flavour that store a list of ice cream flavour
# Write a method that displays these flavour
# Creat an instance of ice cream stand
# and call this method

class restaurant():
    def __init__(self ,restaurant_name ,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cusine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} And cuisine are {self.cusine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open now")
    def set_number_served(self):
        print(f"This restaurant serve {self.number_served} People Today")

class Ice_cream_stand(restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavour):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour=flavour
    def display_flavour(self):
        for i in self.flavour:
            print(f"The flavours {self.restaurant_name} Offers if {i}")
        
    
karachi=restaurant('coconut groove','Angolan cuisine')
karachi.describe_restaurant()
karachi.open_restaurant()
karachi.set_number_served()
karachi.number_served=10
karachi.set_number_served()
ice=Ice_cream_stand('coconut groove','angolo',['apple','mango','pineapple'])
ice.display_flavour()

