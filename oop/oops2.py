"""product :
    id 
    name
    price 
    total_quantity 
    offer
    
    add_product 
    delete_prod
    change_price 
    update_stock 
    
Cust :
    cust_id
    name
    contact_no  
    
    add_to_cart(product,q)
    remove_from_kart()
    request_bill(cart,mode_payment)
    
Supermarket
    
    CGST = 5%
    SGST = 5% 
    cal_bill(cart) => Total Bill 

Offers
    id 
    product 
    quantity 
    offer price 
    valid_till 
    
    add_offer()
    remove_offer()
    update_offer()"""


class Product:
    def __init__(self,p_id,p_name,u_price,total_quantity):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = u_price
        self.p_quantity = total_quantity
        
    def remove_product(self):
        id = self.p_id
        del self
        return id
    
    def change_price(self,new_price):
        self.p_price = new_price
        
    def update_stock(self,current_quantity):
        self.p_quantity = current_quantity
        
    def __str__(self):
        return "{} {}".format(self.p_id,self.p_name)


    

class SuperMarket:
    
    @classmethod
    def cal_bill(cls,cart):
        total_ammount = 0
       
        for prod,quantity in cart.items():
#             print(prod.p_price,quantity,total_ammount)
            total_ammount += prod.p_price * quantity
            
        
        total_ammount += total_ammount * 0.05
        return total_ammount





class Customer:
    def __init__(self,c_id,c_name,c_contact,c_cart = {}):
        self.c_id = c_id
        self.c_name = c_name
        self.c_contact = c_contact
        self.c_cart = c_cart
        
    def add_to_cart(self,prod,quantity):
        if prod in self.c_cart:
            self.c_cart[prod]= self.c_cart[prod] + quantity
        else:
            self.c_cart.setdefault(prod,quantity)
            
    def remove_from_kart(self,prod):
        if prod in self.c_cart:
            id = prod.p_id
            self.c_cart.pop(prod)
            return id
        
    def req_bill(self):
        return SuperMarket.cal_bill(self.c_cart)




p1 = Product(101,"A",50,500)
p2 = Product(102,"B",30,50)
p3 = Product(103,"C",20,500)

print(p1)
print(p2)
print(p3)    



