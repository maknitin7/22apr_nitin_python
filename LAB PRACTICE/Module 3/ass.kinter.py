import tkinter

window = tkinter.Tk()
window.title("Assessment 2")
window.geometry("1000x1500")
window.config(bg="lightblue")

# Center the "BILLING SOFTWARE" text
tkinter.Label(text="BILLING SOFTWARE", font="elephant 20", fg="white", bg="navyblue").grid(row=0, column=5, columnspan=2, sticky="n")

# Place "Customer Name" below
tkinter.Label(text="Customer Name:", font="dubai 14 bold",bg="lightblue", fg="black").grid(row=1, column=0, sticky="w")

# Add an entry field for the customer name
cn=tkinter.Entry()
cn.grid(row=1, column=1, sticky="w")

tkinter.Label(text="Phone No    ", font="dubai 14 bold",bg="lightblue", fg="black").grid(row=1, column=2, sticky="w")
ph=tkinter.Entry()
ph.grid(row=1, column=3, sticky="w")

tkinter.Label(text="Bill No.    ", font="dubai 14 bold",bg="lightblue", fg="black").grid(row=1, column=4, sticky="w")
bill=tkinter.Entry()
bill.grid(row=1, column=5, sticky="w")


def bill_details():
    print("Customer name:",cn.get())
    print("Phonne No:",ph.get())
    print("Bill No:",bill.get())

    with open("Billing_Software.txt","w") as bl:
        bl.write(f"Customer Name:{cn.get()} \nPhone NO: {ph.get()} \nBill No: {bill.get()} ")


tkinter.Button(text="Enter",font="elephant 12",command=bill_details).grid(row=1,column=7)

window.mainloop()