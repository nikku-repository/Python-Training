# Q1. Product Search System (Static Polymorphism)
class ProductSearch:
    def search(self, name = None, category = None, pricerange = None):
        if name is not None and category is not None and pricerange is not None:
            print(f"Searching by {name}, {category} and {pricerange}")
        elif name is not None and category is not None:
            print(f"Searching by {name} and {category}")
        elif name is not None:
            print(f"Searching by {name}")
        else:
            print(f"Invalid search item")

pdt = ProductSearch()
pdt.search("Shyam", "Electronics", "300-400")
pdt.search("Gaurav", "Grocieries")
pdt.search("Nikku")
pdt.search()
print("=" *50)

# ==================================================================================

# Q2. Cart System with Quantity Variations (Static Polymorphism)
class Cart:
    def addproduct(self, product1 = None, quantity1 = None, product2 = None, quantity2 = None):
        if product1 is not  None and  quantity1 is not  None and product2 is not None and  quantity2 is not None:
            print(f"Adding Product: {product1} with Quantity: {quantity1} and Product: {product2} with Quantity: {quantity2}")
        elif product1 is not  None and  quantity1 is not  None:
            print(f"Adding Product: {product1} with Quantity: {quantity1}")
        else:
            print("No product to add")


cart = Cart()
cart.addproduct("TV", 100, "Washing Machine", 300)
cart.addproduct("Shorts", 900)
cart.addproduct()
print("=" *50)

# ==================================================================================

# Q3. Discount Application (Static Polymorphism)
class Discount:
    def applydiscount(self, flatdiscount = None,  percentagediscount = None,  oneonone = None):
        if flatdiscount is not None:
            print(f"Applying flat discount Rs. {flatdiscount}")
        elif percentagediscount is not None:
            print(f"Applying percentage discount {percentagediscount}%")
        elif oneonone is True:
            print(f"Applying buy one get one discount")
        else:
            print(f"No discount")

discount = Discount()
discount.applydiscount(2500)
discount.applydiscount(None, 65)
discount.applydiscount(None, None, True)
discount.applydiscount()
print("=" *50)

# ==================================================================================

# Q4. Payment System (Dynamic Polymorphism)
class Payment:
    def payment(self):
        print("No payment method selected")


class CreditCardPayment(Payment):
    def payment(self):
        print("Credit Card payment method selected")
    
    
class UPIPayment(Payment):
    def payment(self):
        print("UPI payment method selected")
    
    
class CODPayment(Payment):
    def payment(self):
        print("COD payment method selected")

payments = [CreditCardPayment(), UPIPayment(), CODPayment(), Payment()]

for pmnt in payments:
    pmnt.payment()

