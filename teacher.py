class Teacher:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.__salary = salary

    def show_details_information(self):
        print("Mr {0}. age {1}. Works under department {2} and got remuneration of {3}".format(self.name, self.age, self.department, self.__salary))

# create a Teacher object and call the show_details_information method
if __name__ == "__main__":
    print("*********Staff Management System**********")
    print("Kathmandu, Nepal")
    name = input("Enter the name of the Teacher:")
    age = input("Enter the Age of the Teacher:")
    department = input("Enter the Department of the Teacher:")
    salary = input("Enter the Salary of the Teacher:")
    teacher = Teacher(name, age, department, salary)
    teacher.show_details_information()
