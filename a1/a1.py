class DeviceItem:
    def __init__(self, model_name):
        self.model_name = model_name

class Laptop(DeviceItem):
    def __init__(self, laptop_id, brand, model_name):
        super().__init__(model_name)
        self.laptop_id = laptop_id
        self.brand = brand
        self.available = True

    def __str__(self):
        if self.available == True:
            availability = "Available"
        elif self.available == False:
            availability = "Not Available"

        laptop_name = f"{self.brand} {self.model_name}"
        
        return f"{self.laptop_id:<4} {laptop_name:<21} {availability}"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_laptops = []

    def __str__(self):
        return f"{self.student_id} - {self.name}"

class LaptopLoanDesk:
    def __init__(self):
        self.laptops = [
            Laptop(1, "Lenovo", "ThinkPad"),
            Laptop(2, "Dell", "Latitude"),
            Laptop(3, "HP", "EliteBook"),
            Laptop(4, "Apple", "MacBook Air"),
            Laptop(5, "Asus", "Vivobook")
        ]
        
        self.students = [
            Student(1001, "Alice"),
            Student(1002, "Bob"),
            Student(1003, "Charlie"),
            Student(1004, "Diana"),
            Student(1005, "Ethan")
        ]

    def show_laptops(self):
        return self.laptops

    def add_laptop(self, brand, model_name):
        laptop = Laptop(len(self.laptops) + 1, brand, model_name)
        self.laptops.append(laptop)
        return laptop

    def search_laptop_by_model(self, model_name):
        for laptop in self.laptops:
            if laptop.model_name == model_name:
                result_laptop = laptop
                return result_laptop
        result_laptop = 0
        return result_laptop

    def show_students(self):
        return self.students

    def add_student(self, name):
        student = Student(len(self.students) + 1, name)
        self.students.append(student)
        return student

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def loan_laptop(self, student_id, laptop_id):
        return None

    def return_laptop(self, student_id, laptop_id):
        return None

# Print menu and return selection from menu
def main_menu():
    print("Student Laptop Loan Management System")
    print("1. Show Laptops\
        \n2. Add laptop\
        \n3. Search laptop by model name\
        \n4. Show list of registered students\
        \n5. Add new student\
        \n6. Search Student by ID\
        \n7. Loan a laptop\
        \n8. Return a laptop\
        \n9. Exit")
    selection = int(input("Input desired function number: "))
    return selection

# Main

desk = LaptopLoanDesk()

while True:
    selection = main_menu()
    
    match selection:
        # Show laptops
        case 1:
            print("ID   Laptop Model          Availability")
            laptops = desk.show_laptops()
            for laptop in laptops:
                print(laptop)
        
        #Add laptop
        case 2:
            brand = input("Enter brand: ")
            model_name = input("Enter model name: ")
            desk.add_laptop(brand, model_name)
            print("Laptop has been added!")
        
        # Search laptop by model name
        case 3:
            model_name = input("Enter model name: ")
            result_laptop = desk.search_laptop_by_model(model_name)
            if result_laptop == 0:
                print("Model does not exist or is not available.")
            else:
                print(result_laptop)
        
        # Show list of registered students
        case 4:
            print("ID  Name")
            students = desk.show_students()
            for student in students:
                print(student)
        
        # Add a new student
        case 5:
            name = input("Enter student name: ")
            student = desk.add_student(name)
            print("Student has been added!")
            print(f"New student: {student}")
        
        # Search student by ID
        case 6:
            desk.search_student_by_id()
        
        # Loan a laptop
        case 7:
            LaptopLoanDesk.loan_laptop()
        
        # Return a laptop
        case 8:
            LaptopLoanDesk.return_laptop()
        
        # Exit
        case 9:
            print("Running option 9")
        
