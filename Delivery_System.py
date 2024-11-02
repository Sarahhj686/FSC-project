class Delivery_System:
    def __init__(self):
        
        self.drivers = {
             "driver 1":{"id":"ID001","name": "Max Verstappen", "start_city": "Akkar"},
             "driver 2":{"id":"ID002", "name": "Charles Leclerc", "start_city": "Saida"},
             "driver 3":{"id":"ID003", "name": "Lando Norris", "start_city": "Jbeil"},
             "driver 4":{"id":"ID004", "name": "jalal", "start_city": "Jbeil"}
        }
        self.cities = {
            "Beirut": ["Jbeil"],
            "Jbeil": ["Beirut", "Akkar"],
            "Akkar": ["Jbeil"],
            "Saida": ["Zahle"],
            "Zahle": ["Saida"]
        }

    def main_menu(self):
        print("Hello! Please enter:") 
        print("(1) To go to the drivers menu")
        print("(2) To go to the cities menu")
        print("(3) To exit the system")
        user_input=int(input("enter your choice:"))
        
        if user_input== 1:
            self.drivers_menu()
           
        elif user_input==2:
            self.cities_menu()
        
        elif user_input==3:
            return
        else:
            print("invalid input, try again")
            self.main_menu()
            
    def drivers_menu(self):
        print("Enter:")
        print("(1) To view all the drivers")
        print("(2) To add a driver")
        print("(3) Check similar drivers")
        print("(4) To go back to the main menu")
        user_choice= int(input("enter your choice:"))
        
        if user_choice== 1:
            self.view_drivers()
        elif user_choice== 2:
            self.add_driver()
        elif user_choice== 3:
            self.check_similar_drivers()
        elif user_choice== 4:
            self.main_menu()
        else: 
            print("invalid input, try again")
            self.drivers_menu()
        
    def view_drivers(self):
        for driver_details in self.drivers.values():
            print(f"{driver_details['id']}, {driver_details['name']}, {driver_details['start_city']}")
            
    def add_driver(self):
        key="ID00"
        Id= len(self.drivers)+ 1 
        self.drivers["id"]=(key)+str(Id)
        name1= str(input("enter the name of the driver you want to add: ")).capitalize()
        start_city1=str(input("enter the start city of the driver:")).capitalize()
        if start_city1 not in self.cities:
            choice=str(input("start city not available would you like to add it?"))
            if choice=="yes":
                self.drivers["start_city"]=start_city1
            else: 
                return
        self.drivers["name"] = name1
        print("driver added successfully!")
        print(self.drivers)
        
ds= Delivery_System()
ds.main_menu()
