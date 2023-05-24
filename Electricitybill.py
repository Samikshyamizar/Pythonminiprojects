class ElectricityBill:
    def __init__(self):
        self.customer_name = input("Enter customer name: ")
        self.customer_address = input("Enter customer address: ")
        self.customer_unit = int(input("Enter consumed unit: "))
    
    def calculate_bill(self):
        if self.customer_unit <= 100:
            total_amount = self.customer_unit * 4 
        elif self.customer_unit <= 150:
            total_amount = 100 * 4 + (self.customer_unit - 100) * 8 
        elif self.customer_unit <= 250: 
            total_amount = 100 * 4 + 50 * 8 + (self.customer_unit - 150) * 10  
        elif self.customer_unit <= 500: 
            total_amount = 100 * 4 + 50 * 8 + 100 * 10 + (self.customer_unit - 250) * 12 
        else: 
            total_amount = 100 * 4 + 50 * 8 + 100 * 10 + 250 * 12 + (self.customer_unit - 500) * 15

        if self.customer_unit > 500:
            total_amount *= 0.95  
        if total_amount > 10000:
            total_amount *= 0.9  

        return total_amount
    
    def display_bill(self, total_amount):
        print("Sunway College Electricity Bill")
        print("-----------------------------------")
        print(f"Name: {self.customer_name}")
        print(f"Address: {self.customer_address}")
        print(f"Units Consumed: {self.customer_unit}")
        print(f"Total Amount: Rs. {total_amount:.2f}")

def main():
    electricity_bill = ElectricityBill()
    total_amount = electricity_bill.calculate_bill()
    electricity_bill.display_bill(total_amount)

if __name__ == '__main__':
    main()
