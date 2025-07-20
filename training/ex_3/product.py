class Product:

    def __init__(self, name, price):
        print("конструктор")
        self.product_name = name
        self.product_price = price

    def getProductName(self):
        return self.product_name

    def getProductPrice(self):
        return self.product_price

    def getProductNamePrice(self):
        return f"Product: {self.product_name}, Price: {self.product_price}"
