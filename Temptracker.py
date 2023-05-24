class TemperatureTracker:
    def __init__(self):
        self.company_name = ''
        self.company_address = ''
        self.num_days = 0
        self.temperature_readings = []
        self.temperature_categories = {'very_hot': 0, 'pleasant': 0, 'very_cold': 0}
        self.temperature_range = {'very_hot': range(85, 101), 'pleasant': range(60, 85), 'very_cold': range(0, 60)}

    def initialDisplay(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address
        print(f'{self.company_name}\n----------Temperature Record Management System-----------\n{self.company_address}\n')

    def InputInformation(self):
        self.num_days = int(input('How many days to record? '))
        print('\nPlease enter temperature readings for each day:')
        for i in range(self.num_days):
            temperature = int(input(f'Temperature day [{i+1}] = '))
            self.temperature_readings.append(temperature)

    def calculateTemperature(self):
        total_temperature = sum(self.temperature_readings)
        average_temperature = round(total_temperature / self.num_days)
        for temp in self.temperature_readings:
            for category, temp_range in self.temperature_range.items():
                if temp in temp_range:
                    self.temperature_categories[category] += 1
                    break
        return average_temperature

    def CategoryCheck(self, temp):
        if temp in self.temperature_range['very_hot']:
            return 'very_hot'
        elif temp in self.temperature_range['pleasant']:
            return 'pleasant'
        else:
            return 'very_cold'

    def displayInformation(self):   
        print(f'Daily Temperatures Report')
        for i, temp in enumerate(self.temperature_readings):
            category = self.CategoryCheck(temp)
            print(f'Temperature day [{i+1}] = {temp} Celsius {category} ')
        print(f'The average Temp for {self.num_days} days = {self.calculateTemperature()} Celsius')

    def finalDisplay(self):
        
        print(f'\nNumber of hot days = {self.temperature_categories["very_hot"]} day/s')
        print(f'Number of pleasant days = {self.temperature_categories["pleasant"]} day/s')
        print(f'Number of cold days = {self.temperature_categories["very_cold"]} day/s')
# Example usage:
tt = TemperatureTracker()
tt.initialDisplay('UniCampus', 'Kathmandu Nepal')
tt.InputInformation()
tt.displayInformation()
tt.finalDisplay()
