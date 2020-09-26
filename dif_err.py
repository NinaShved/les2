# Исключения
def discounted(price, discount):
    
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        if discount >= 100:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        print(price_with_discount)     
    except(TypeError, ValueError, SyntaxError):   
        print("Неверные данные")        

discounted(five, 0.5)