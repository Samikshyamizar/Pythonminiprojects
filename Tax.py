class StaffManagement:
    def __init__(self):
        self.staff_data = {}

    def display_static_info(self):
        heading = ("""
                   Sunway College Account Department
                        Maitidevi ,Kathmandu
                          Welcome to
                  Salary & Tax Calculate System(STCS)""")
        print(heading)

    def collect_staff_info(self):
        n = int(input("Enter the number of Staff: "))
        for i in range(n):
            self.staff_data[i] = {}
            self.staff_data[i]['name'] = input(f"Enter the name of Staff [{i+1}]: ")
            self.staff_data[i]['address'] = input(f"Enter the address of staff [{i+1}]: ")
            self.staff_data[i]['email'] = input(f"Enter the email of staff [{i+1}]: ")
            self.staff_data[i]['pan'] = input(f"Enter the pan of staff [{i+1}]: ")
            self.staff_data[i]['married_status'] = input(f"Enter the married status of staff [{i+1}]: ")
            self.staff_data[i]['FY'] = input(f"Enter the FY of staff [{i+1}]: ")
            montly_income = int(input(f"Enter the monthly income of staff: "))
            self.staff_data[i]['annual_income'] = montly_income * 12

    def calculate_tax(self):
        for i in range(len(self.staff_data)):
            annual_income = self.staff_data[i]['annual_income']
            tax = 0
            if annual_income <= 400000:
                tax = tax + annual_income * 0.01
            elif annual_income <= 500000:
                tax = tax + (annual_income - 400000) * 0.1
            elif annual_income <= 700000:
                tax = tax + 400000 * 0.01 + 100000 * 0.1 + (annual_income - 500000) * 0.2
            elif annual_income <= 1300000:
                tax = tax + 400000 * 0.01 + 100000 * 0.1 + 200000 * 0.2 + (annual_income - 700000) * 0.3
            else:
                tax = tax + 400000 * 0.01 + 100000 * 0.1 + 200000 * 0.2 + 600000 * 0.3 + (annual_income - 1300000) * 0.36
            self.staff_data[i]['tax'] = tax

    def display_staff_info(self):
        for i in range(len(self.staff_data)):
            print(f"\nStaff {i+1} details:")
            print(f"Name: {self.staff_data[i]['name']}")
            print(f"Address: {self.staff_data[i]['address']}")
            print(f"Email: {self.staff_data[i]['email']}")
            print(f"PAN: {self.staff_data[i]['pan']}")
            print(f"Marital Status: {self.staff_data[i]['married_status']}")
            print(f"FY: {self.staff_data[i]['FY']}")
            print(f"Monthly Income: {self.staff_data[i]['annual_income'] / 12}")
            print(f"Annual Income: {self.staff_data[i]['annual_income']}")
            print(f"Tax: {self.staff_data[i]['tax']}")

# Main program
staff = StaffManagement()
staff.display_static_info()
staff.collect_staff_info()
staff.calculate_tax()
staff.display_staff_info()
