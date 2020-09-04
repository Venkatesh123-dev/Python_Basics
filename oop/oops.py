"""Problem 1:
In a normal supermarket, things are identified using Stock Keeping Units. In our store, we’ll use individual letters of the alphabet (A, B, C, and so on). Our goods are priced individually. In addition, some items are multipriced: buy n of them, and they’ll cost you y Rs. For example, item ‘A’ might cost 50 Rs individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you 120Rs. In fact this week’s prices are:

Item Unit Special

    Price Price

    A 50 3 for 120 
    B 30 2 for 45 
    C 20 
    D 15

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 . Because the pricing changes frequently, we need to be able to pass in a set of pricing rules each time we start handling a checkout transaction


Product :
    id
    title
    unit_price
    
Admin:
    add_product()
    
    
Billing_Sytem:
    cal_billing_amount(cart)
    
Customer:
    add_cart()
    check_out()
    
Cart:
    items[(Product,quantity),(Product,quantity),(Product,quantity)]
    
    
cust 1 => 1 cart        prod_name
                        price
                        quantity
        
          A  5 
            
          B  10    """

class Product:
    def __init__(self,p_id,title,unit_price):
        self.p_id =p_id
        self.p_title = title
        self.p_unit_price = unit_price
        self.offer = False

    def set_offer(self):
        self.offer = True

class Admin:

    def add_product(self,p_id,title,unit_price):
        p1 = Product(p_id,title,unit_price)
        return p1

    def add_offers(self,product,quantity,offer_price):
        o1 = Offer(product,quantity,offer_price)
        product.set_offer()
        return o1

class Customer:

    def __init__(self):
        self.cart = []

    def add_to_cart(self,product,quantity):
        self.cart.append((product,quantity))

    def checkout(self):
        return Billing.calculate_bill(self.cart)

class Billing:

    @classmethod
    def calculate_bill(cls,cart):
        bill_amount = 0
        final_cart = {}
        for product,quantity in cart:
            if product in final_cart:
                final_cart[product] += quantity
            else:
                final_cart[product] = quantity

        ## Calculate the bill by checking the offer

#         for product,quantity in cart:
#             bill_amount += product.p_unit_price * quantity

#         return bill_amount


class Offer:
    def __init__(self,product,quantity,offer_price):
        self.product = product
        self.quantity = quantity
        self.offer_price = offer_price

admin = Admin()
print(admin)

a = admin.add_product(1001,"A",50)
b = admin.add_product(1001,"B",30)
c = admin.add_product(1001,"C",20)
d = admin.add_product(1001,"D",15)


cust1 = Customer()
cust2 = Customer()

cust1.add_to_cart(a,6)
cust1.add_to_cart(b,2)
cust1.add_to_cart(a,3)

amount = cust1.checkout()
print(amount)
