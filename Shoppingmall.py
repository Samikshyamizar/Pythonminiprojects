import datetime

class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.items = []

    def add_item(self, item_name, item_price, item_qty):
        item_total = item_price * item_qty
        self.items.append({
            'item_name': item_name,
            'item_price': item_price,
            'item_qty': item_qty,
            'item_total': item_total
        })

    def get_total(self):
        total = sum([item['item_total'] for item in self.items])
        return total

    def get_discount(self):
        total = self.get_total()
        if total <= 5000:
            discount = total * 0.05
        elif total <= 7000:
            discount = (5000 * 0.05) + (total - 5000) * 0.08
        elif total <= 10000:
            discount = (5000 * 0.05) + (2000 * 0.08) + (total - 7000) * 0.10
        else:
            discount = (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (total - 10000) * 0.15
        return discount

    def get_net_total(self):
        total = self.get_total()
        discount = self.get_discount()
        net_total = total - discount
        return net_total

    def generate_bill(self):
        bill = f'''
        Sunway College Bhatbhateni System
              Maitidevi,Kathmandu    

        Customer Name: {self.name}
        Customer Address: {self.address}
        Customer Email: {self.email}

        {"Item Name":<20} {"Item Price":>10} {"Item Quantity":>15} {"Total Price":>15}
        '''
        for item in self.items:
            bill += f"{item['item_name']:<20} {item['item_price']:>10} {item['item_qty']:>15} {item['item_total']:>15}\n"
            bill += f"\nDiscount: {self.get_discount()}"
            bill += f"\nNet Total: {self.get_net_total()}"

        filename = f"bill_{self.name}_{datetime.datetime.now().date()}.txt"
        with open(filename, 'w') as bill_file:
            bill_file.write(bill)
        print(f"Bill for {self.name} generated and saved successfully.")

def main():
    n = int(input("Enter the number of customers: "))
    for i in range(n):
        name = input(f"Enter the name of customer [{i+1}]: ")
        address = input(f"Enter the address of customer [{i+1}]: ")
        email = input(f"Enter the email of customer [{i+1}]: ")
        itemno = int(input(f"Enter the number of items for {name}: "))

        customer = Customer(name, address, email)

        for j in range(itemno):
            item_name = input(f"Enter the name of item [{j+1}]: ")
            item_price = int(input(f"Enter the price of item [{j+1}]: "))
            item_qty = int(input(f"Enter the quantity of item [{j+1}]: "))
            customer.add_item(item_name, item_price, item_qty)

        customer.generate_bill()

if __name__ == "__main__":
    main()
