import pandas
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
    
    DF= pandas.DataFrame(items,columns=[["Food", "Qauntity", "price", "Subtotal"]])
    print(DF)

    print("\n GRAND TOTAL: ", total)


billing_system()