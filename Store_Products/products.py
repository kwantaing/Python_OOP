class Product:
    def __init__(self, name, price, category,id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id

    def price_to_string(self):
        return '%.2f' %self.price

    def update_price(self, percent_change, is_increased):
        if (is_increased):
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
        return self
        
    def print_info(self):
        print(f"Product Name: {self.name} , id: {self.id}Category: {self.category}, Price: ${self.price_to_string()}")