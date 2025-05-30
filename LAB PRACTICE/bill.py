def billing():
    items=[]
    total=0
    while True:
     
        food=input("enter food name:")
        qty=int(input(" how many items:"))
        price=float(input("enter the price of item:"))
     
        item_total=qty*price
        total += item_total

        items.append((food,qty,price ,item_total))

        new=input( "do u need more:")
        if new != "yes":
            break
     
    print("grandtotal", total) 

billing()