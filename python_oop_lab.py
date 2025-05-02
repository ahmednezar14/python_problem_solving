# Person Class
class Person:
    def __init__(self, name, money=100, mood="neutral", health_rate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate
    
    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        return self.mood
    
    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50
        else:
            self.health_rate = 0
        return self.health_rate
    
    def buy(self, items):
        self.money -= (10 * items)
        return self.money

# Car Class
class Car:
    def __init__(self, name, velocity=0, fuel_rate=100):
        self.name = name
        self._fuel_rate = fuel_rate
        self._velocity = velocity
    
    @property
    def fuel_rate(self):
        return self._fuel_rate
    
    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            print("Fuel rate must be between 0 and 100")
            self._fuel_rate = min(max(value, 0), 100)
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("Velocity must be between 0 and 200")
            self._velocity = min(max(value, 0), 200)
    
    def run(self, velocity, distance):
        self.velocity = velocity
        remaining_distance = distance
        
        while remaining_distance > 0 and self.fuel_rate > 0:
            # For every 10 km, fuel rate decreases by 10%
            km_to_travel = min(10, remaining_distance)
            fuel_needed = km_to_travel * 0.1  # 10% per 10km
            
            if self.fuel_rate >= fuel_needed:
                self.fuel_rate -= fuel_needed
                remaining_distance -= km_to_travel
                print(f"Traveled {km_to_travel} km. Remaining distance: {remaining_distance} km")
            else:
                print("Not enough fuel to continue!")
                break
        
        self.stop(remaining_distance)
        return remaining_distance
    
    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance <= 0:
            print("You have arrived at your destination!")
        else:
            print(f"Car stopped. Remaining distance: {remaining_distance} km")

# Employee Class
class Employee(Person):
    employees_num = 0
    
    def __init__(self, name, id, email, salary, distance_to_work, car=None):
        super().__init__(name)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work
        Employee.employees_num += 1
    
    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        return self.mood
    
    def drive(self, distance, velocity):
        if self.car:
            print(f"{self.name} is driving {self.car.name} at {velocity} km/h")
            return self.car.run(velocity, distance)
        else:
            print(f"{self.name} doesn't have a car")
            return distance
    
    def refuel(self, gas_amount=100):
        if self.car:
            self.car.fuel_rate = gas_amount
            print(f"Car refueled. Fuel rate: {self.car.fuel_rate}")
        else:
            print(f"{self.name} doesn't have a car")
    
    def send_mail(self, to, subject, body):
        print(f"Email sent from {self.email} to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        
        
    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num
        print(f"Number of employees changed to {num}")

# Office Class
class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None
    
    def hire(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is hired at {self.name}")
    
    def fire(self, emp_id):
        employee = self.get_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            Employee.employees_num -= 1
            print(f"{employee.name} fired from {self.name}")
        else:
            print(f"No employee with ID {emp_id}")
    
    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
       # Check if velocity is zero to avoid division by zero
        if velocity == 0:
            # If velocity is zero, employee can't reach the office
            return True
            
        # Calculate expected arrival time
        expected_time = distance / velocity  # Time in hours
        expected_arrival = move_hour + expected_time
        
        return expected_arrival > target_hour
    
    def check_lateness(self, emp_id, move_hour):
        employee = self.get_employee(emp_id)
        if employee and employee.car:
            is_late = self.calculate_lateness(9, move_hour, employee.distance_to_work, employee.car.velocity)
            if is_late:
                self.deduct(emp_id, 10)
                print(f"{employee.name} is late. Deducted 10 from salary. New salary: {employee.salary}")
                return True
            else:
                self.reward(emp_id, 10)
                print(f"{employee.name} is on time. Rewarded 10 to salary.New salary: {employee.salary}")
                return False
        return None
    
    def deduct(self, emp_id, deduction):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary -= deduction
        
    
    def reward(self, emp_id, reward_amount):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary += reward_amount

    


# creating object sami who works in iti and has car fiat 128 
if __name__ == "__main__":
    # Create Samy's car
    fiat_128 = Car("Fiat 128")
    
    # Create Samy as an employee
    samy = Employee("Samy", 1, "samy@iti.gov", 5000,20,car=fiat_128)
    
    # Create ITI office
    iti = Office("ITI Smart Village")
    
    # Hire Samy
    iti.hire(samy)
    
    # Demonstrate some functionality
    print(f"\nSamy's initial mood: {samy.mood}")
    samy.sleep(7)
    print(f"After sleeping 7 hours, Samy's mood: {samy.mood}")
    
    print(f"\nSamy's initial health: {samy.health_rate}")
    samy.eat(2)
    print(f"After eating 2 meals, Samy's health: {samy.health_rate}")
    
    print(f"\nSamy's initial money: {samy.money}")
    samy.buy(3)
    print(f"After buying 3 items, Samy's money: {samy.money}")
    
    print("\nSamy is going to work:")
    samy.car.velocity = 60  # Set velocity to 60 km/h
    samy.drive(samy.distance_to_work, samy.car.velocity)
    
    # Check if Samy is late (starting at 8:30)
    print("\nChecking if Samy is late:")
    iti.check_lateness(samy.id, 8.5)  
    
    # Demonstrate refueling
    print("\nRefueling Samy's car:")
    samy.refuel()
    
    ahmed = Employee("ahmed", 1, "ahmed@iti.gov", 5000,20)
    
    # Show employee count
    print(f"\nTotal employees: {Employee.employees_num}")
    
    # Demonstrate class method to change employees number
    print("\nChanging total employees count:")
    Employee.change_emps_num(10)
   
    
    # Send an email
    print("\nSamy sends an email:")
    samy.send_mail("manager@iti.gov", "Daily Report", "Today's work is completed successfully.")
