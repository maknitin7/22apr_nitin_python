"""import qrcode as qr
url = "Hey! this is for you ^^^|^"
img=qr.make(url)
img.save("qrcode.png")"""

"""from pytubefix import YouTube


url=("https://youtu.be/izbydia9jz4?si=MW4Fkdgr1mRx0QDB")
YouTube(url).streams.first().download().get_highest_resolution()
print("Video downloaded successfully!")"""

"""import pywhatkit as kit
kit.show_history()
print("Message sent successfully!")
import pyautogui
pyautogui.alert("Hello, this is a message from PyAutoGUI!")"""

"""import instaloader
instaid= input("Enter the Instagram ID: ")
insta= instaloader.Instaloader()
insta.download_profile(instaid)
print(f"Profile of {instaid} downloaded successfully!")"""

"""import gtuworld
branch="BE"
sub_codes=["3110015"]
gtuworld.download(branch, sub_codes)
"""
import pywhatkit

pywhatkit.sendwhatmsg("+919824641854", """import datetime
import pandas
def billing_system():
    total=0
    items=[]

    while True:
        name=input("Enter your name: ")
        mobile=input("Enter your mobile number: ")
        food=input("Enter food name:")
        qty=int(input("How many items do  u want:"))
        price=float(input("What is the price of your item:"))
        

        item_total= qty * price
        total += item_total
        gst = item_total * 0.18
        
        items.append((name,mobile,food,qty,price, item_total,gst))

        more= input(" Do you want moe items? (1 for yes/2 for no):")
        if more == '1':
            continue
        elif more == '2':
            print("Thank you for your order!")
            break
        

    print("\n ----------------   Bill Summary ------------------- \n ")
    
    DF= pandas.DataFrame(items,columns=[["Name","Mobile No","Food", "Qauntity", "price", "Subtotal", "GST"]])
    print(DF)

    print("\n GRAND TOTAL : ", (total * 0.18) + total) 

    
    x=open("food_bill.txt", "a")
    x.write('Created at:'+str(datetime.datetime.now()))
    x.write("\n -----------------   Bill Summary ------------------ \n ")
    x.write(str(DF))
    x.write("\n GRAND TOTAL : " + str((total * 0.18) + total))



billing_system()""")

