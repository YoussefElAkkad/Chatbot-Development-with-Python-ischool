# class Dog:
#   def __init__(self,breed):
#     self.breed=breed
#   def make_sound(self):
#     return "Woof!"

# class Cat:
#   def __init__(self,breed):
#     self.breed=breed

#   def make_sound(self):
#     return "Meow!"

# class AnimalShelter:
#   def __init__(self):
#     self.animals=[]
#   def add_animal(self,animal):
#     self.animals.append(animal)
#   def make_sounds(self):
#     for animal in self.animals:
#       print(animal.make_sound())


# shelter=AnimalShelter()
# shelter.add_animal(Dog("Golden Retriever"))
# shelter.add_animal(Cat("Persian"))
# shelter.add_animal(Dog("Poodle"))
# shelter.make_sounds()



# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def drive(self):
#         return f"Driving {self.brand} {self.model}"

# class ElectricCar:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def drive(self):
#         return f"Driving {self.brand} {self.model} silently"
    
# car=Car("Toyota","Camry")
# ECar=ElectricCar("Tesla","Model S")
# print(car.drive())
# print(ECar.drive())





# class Employee:
#     def __init__(self,name,salary):
#       self.name=name
#       self.salary=salary

#     def get_info(self):
#        return f"Name: {self.name}, Salary: {self.salary}"
    
# class Manager(Employee):
#    def __init__(self,name,salary,department):
#       super().__init__(name,salary)
#       self.department=department

#    def get_info(self):
#       return f"{super().get_info()}, Department: {self.department}"
   

# class Director(Manager):
#    def __init__(self,name,salary,department,num_of_reports):
#       super().__init__(name,salary,department)
#       self.num_of_reports=num_of_reports
#    def get_info(self):
#       return f"{super().get_info()}, Reports: {self.num_of_reports}"
   
# d=Director("Alice",100000,"Finance",5)
# print(d.get_info())





# class Library:
#     def __init__(self):
#         self.books = []
    
#     def add_book(self, title, author):
#         book = {'title': title, 'author': author, 'available': True}
#         self.books.append(book)
    
#     def remove_book(self, title):
#         for book in self.books:
#             if book['title'] == title:
#                 self.books.remove(book)
#                 break
    
#     def display_available_books(self):
#         for book in self.books:
#             if book['available']:
#                 print("Title:", book['title'])
#                 print("Author:", book['author'])
#                 print()

# library=Library()
# library.add_book("The Great Gatspy","F. Scott Fitzgerald")
# library.add_book("To Kill a Mockingbird","Harper Lee")
# library.display_available_books()
# library.remove_book("To Kill a Mockingbird")
# library.display_available_books()




# class GradeTracker:
#     def __init__(self, student_name):
#         self.student_name = student_name
#         self.grades = {}
    
#     def add_grade(self, subject, grade):
#         self.grades[subject] = grade
    
#     def calculate_average_grade(self):
#         total_grades = 0
#         for grade in self.grades.values():
#             total_grades += grade
#         average_grade = total_grades / len(self.grades)
#         return average_grade
    
#     def display_student_info(self):
#         print("Student Name:", self.student_name)
#         print()
#         for subject, grade in self.grades.items():
#             print("Subject:", subject)
#             print("Grade:", grade)
#             print()


# grade_tracker=GradeTracker("Youssef Tamer")
# grade_tracker.add_grade("Math",98)
# grade_tracker.add_grade("Physics",100)
# grade_tracker.add_grade("English",95)
# grade_tracker.display_student_info()