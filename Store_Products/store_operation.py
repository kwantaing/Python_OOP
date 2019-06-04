import store
import products

store_A = store.Store("Store_A")
banana = products.Product("Banana",1.99,"Fruits",1)
apple = products.Product("Apple",0.99,"Fruits",2)
burger = products.Product("Burger",5.99,"American",3)

store_A.add_product(banana).add_product(apple).add_product(burger)
store_A.print_info()

store_A.sell_product(1)
store_A.print_info()

store_A.inflation(0.10)
store_A.print_info()

store_A.set_clearance("Fruits",0.5)
store_A.print_info()