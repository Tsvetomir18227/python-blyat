class NumericList:
    def __init__(self, input_list):
        self.numeric_list = [num for num in input_list if isinstance(num, (int, float))]

    def show_list(self):
        return self.numeric_list

    def calculate_average(self):
        if not self.numeric_list:
            return "No numeric elements to calculate average."
        return sum(self.numeric_list) / len(self.numeric_list)

# Пример на използване:
input_data = [1, 2, 'a', 3.5, 'b', 4]
numeric_obj = NumericList(input_data)

print("Съдържание на списъка:", numeric_obj.show_list())
print("Средна стойност:", numeric_obj.calculate_average())
