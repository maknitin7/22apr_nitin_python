def billing_system():
    total=0
    items=[]

    while True:

        food=input(" Enter food name:")
        qty=int(input(" How many items do  u want:"))
        price=float(input(" What is the price of your item:"))

        item_total= qty * price
        total += item_total
        
        items.append((food,qty,price, item_total))

        more= input(" Do you want moe items? (1 for yes/2 for no):")
        if more == '1':
            continue
        elif more == '2':
            print("Thank you for your order!")
            break
        

    print("\n -----   Bill Summary ----- \n ")
    
    for item in items:
        food, qty, price, item_total = item
        print(f" items: {food}, quantity: {qty}, price: {price}, subtotal: {item_total}")

    print("\n GRAND TOTAL: ", total)
    

billing_system()