class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self,id):
        for index in range(len(self.product_list)):
            if(self.product_list[index].id == id):
                return self.product_list.pop(index)
        return "No product exists with that id"

    def print_info(self):
        print(self.name)
        for product in self.product_list:
            product.print_info()
    
    def inflation(self,percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase,True)

    def set_clearance(self,category,percent_discount):
        for product in self.product_list:
            if(product.category == category):
                product.update_price(percent_discount,False)
