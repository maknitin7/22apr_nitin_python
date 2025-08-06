import tkinter as tk
from tkinter import messagebox, ttk

# ----------- Functions -----------
def calculate_total():
    try:
        # Cosmetics prices
        total_cosmetics = (
            int(bath_soap.get() or 0) * 40 +
            int(face_cream.get() or 0) * 120 +
            int(face_wash.get() or 0) * 140 +
            int(hair_spray.get() or 0) * 180 +
            int(body_lotion.get() or 0) * 200
        )
        cosmetics_tax = total_cosmetics * 0.05

        # Grocery prices
        total_grocery = (
            int(rice.get() or 0) * 80 +
            int(food_oil.get() or 0) * 150 +
            int(daal.get() or 0) * 100 +
            int(wheat.get() or 0) * 90 +
            int(sugar.get() or 0) * 60
        )
        grocery_tax = total_grocery * 0.05

        # Others prices
        total_others = (
            int(maza.get() or 0) * 40 +
            int(coke.get() or 0) * 45 +
            int(frooti.get() or 0) * 50 +
            int(nimkos.get() or 0) * 35 +
            int(biscuits.get() or 0) * 20
        )
        others_tax = total_others * 0.05

        total_price.set(f"Rs. {total_cosmetics + total_grocery + total_others:.2f}")
        cosmetics_total.set(f"Rs. {total_cosmetics}")
        grocery_total.set(f"Rs. {total_grocery}")
        others_total.set(f"Rs. {total_others}")
        tax_cosmetics.set(f"Rs. {cosmetics_tax:.2f}")
        tax_grocery.set(f"Rs. {grocery_tax:.2f}")
        tax_others.set(f"Rs. {others_tax:.2f}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_bill():
    if not cust_name.get() or not phone.get() or not bill_no.get():
        messagebox.showwarning("Missing Info", "Customer details are required!")
        return

    bill_text.delete("1.0", tk.END)
    bill_text.insert(tk.END, "\tWelcome to Nitin's SmartBazar\n")
    bill_text.insert(tk.END, f"\nBill No. : {bill_no.get()}")
    bill_text.insert(tk.END, f"\nCustomer Name : {cust_name.get()}")
    bill_text.insert(tk.END, f"\nPhone No. : {phone.get()}\n")
    bill_text.insert(tk.END, "\n=====================================")
    bill_text.insert(tk.END, "\nProduct\t\tQty\tPrice")
    bill_text.insert(tk.END, "\n=====================================")

    total_amount = 0
    items = {
        "Bath Soap": (bath_soap, 40),
        "Face Cream": (face_cream, 120),
        "Face Wash": (face_wash, 140),
        "Hair Spray": (hair_spray, 180),
        "Body Lotion": (body_lotion, 200),
        "Rice": (rice, 80),
        "Food Oil": (food_oil, 150),
        "Daal": (daal, 100),
        "Wheat": (wheat, 90),
        "Sugar": (sugar, 60),
        "Maza": (maza, 40),
        "Coke": (coke, 45),
        "Frooti": (frooti, 50),
        "Nimkos": (nimkos, 35),
        "Biscuits": (biscuits, 20),
    }

    for item, (entry, price) in items.items():
        qty = int(entry.get() or 0)
        if qty > 0:
            line = f"\n{item}\t\t{qty}\t{qty * price}"
            bill_text.insert(tk.END, line)
            total_amount += qty * price

    bill_text.insert(tk.END, "\n=====================================")
    bill_text.insert(tk.END, f"\nTotal Amount:\t\tRs. {total_amount:.2f}")
    bill_text.insert(tk.END, "\n=====================================")

    # Save to file
    filename = f"Bill-{bill_no.get()}.txt"
    try:
        with open(filename, "w") as f:
            f.write(bill_text.get("1.0", tk.END))
        messagebox.showinfo("Saved", f"Bill saved successfully as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save bill\n{str(e)}")


# ----------- Main GUI -----------
root = tk.Tk()
root.title("Billing Software")
root.geometry("1000x650")
root.config(bg="lightblue")

# Customer details
cust_name = tk.StringVar()
phone = tk.StringVar()
bill_no = tk.StringVar()

tk.Label(root, text="Customer Name").place(x=20, y=10)
tk.Entry(root, textvariable=cust_name).place(x=140, y=10)
tk.Label(root, text="Phone No").place(x=350, y=10)
tk.Entry(root, textvariable=phone).place(x=420, y=10)
tk.Label(root, text="Bill No").place(x=600, y=10)
tk.Entry(root, textvariable=bill_no).place(x=670, y=10)

# Product variables
bath_soap = tk.StringVar(); face_cream = tk.StringVar(); face_wash = tk.StringVar()
hair_spray = tk.StringVar(); body_lotion = tk.StringVar()
rice = tk.StringVar(); food_oil = tk.StringVar(); daal = tk.StringVar()
wheat = tk.StringVar(); sugar = tk.StringVar()
maza = tk.StringVar(); coke = tk.StringVar(); frooti = tk.StringVar()
nimkos = tk.StringVar(); biscuits = tk.StringVar()

# Totals and tax
total_price = tk.StringVar()
cosmetics_total = tk.StringVar(); grocery_total = tk.StringVar(); others_total = tk.StringVar()
tax_cosmetics = tk.StringVar(); tax_grocery = tk.StringVar(); tax_others = tk.StringVar()

all_entries = [bath_soap, face_cream, face_wash, hair_spray, body_lotion,
               rice, food_oil, daal, wheat, sugar,
               maza, coke, frooti, nimkos, biscuits]

# Cosmetics Frame
tk.Label(root, text="Cosmetics", font=('Arial', 12, 'bold')).place(x=20, y=50)
tk.Label(root, text="Bath Soap").place(x=20, y=80)
tk.Entry(root, textvariable=bath_soap, width=5).place(x=100, y=80)
tk.Label(root, text="Face Cream").place(x=20, y=110)
tk.Entry(root, textvariable=face_cream, width=5).place(x=100, y=110)
tk.Label(root, text="Face Wash").place(x=20, y=140)
tk.Entry(root, textvariable=face_wash, width=5).place(x=100, y=140)
tk.Label(root, text="Hair Spray").place(x=20, y=170)
tk.Entry(root, textvariable=hair_spray, width=5).place(x=100, y=170)
tk.Label(root, text="Body Lotion").place(x=20, y=200)
tk.Entry(root, textvariable=body_lotion, width=5).place(x=100, y=200)

# Grocery Frame
tk.Label(root, text="Grocery", font=('Arial', 12, 'bold')).place(x=250, y=50)
tk.Label(root, text="Rice").place(x=250, y=80)
tk.Entry(root, textvariable=rice, width=5).place(x=320, y=80)
tk.Label(root, text="Food Oil").place(x=250, y=110)
tk.Entry(root, textvariable=food_oil, width=5).place(x=320, y=110)
tk.Label(root, text="Daal").place(x=250, y=140)
tk.Entry(root, textvariable=daal, width=5).place(x=320, y=140)
tk.Label(root, text="Wheat").place(x=250, y=170)
tk.Entry(root, textvariable=wheat, width=5).place(x=320, y=170)
tk.Label(root, text="Sugar").place(x=250, y=200)
tk.Entry(root, textvariable=sugar, width=5).place(x=320, y=200)

# Others Frame
tk.Label(root, text="Others", font=('Arial', 12, 'bold')).place(x=450, y=50)
tk.Label(root, text="Maza").place(x=450, y=80)
tk.Entry(root, textvariable=maza, width=5).place(x=520, y=80)
tk.Label(root, text="Coke").place(x=450, y=110)
tk.Entry(root, textvariable=coke, width=5).place(x=520, y=110)
tk.Label(root, text="Frooti").place(x=450, y=140)
tk.Entry(root, textvariable=frooti, width=5).place(x=520, y=140)
tk.Label(root, text="Nimkos").place(x=450, y=170)
tk.Entry(root, textvariable=nimkos, width=5).place(x=520, y=170)
tk.Label(root, text="Biscuits").place(x=450, y=200)
tk.Entry(root, textvariable=biscuits, width=5).place(x=520, y=200)

# Totals Frame
tk.Label(root, text="Bill Menu", font=('Arial', 12, 'bold')).place(x=650, y=50)
tk.Label(root, text="Total Cosmetics").place(x=650, y=80)
tk.Entry(root, textvariable=cosmetics_total, width=12).place(x=770, y=80)
tk.Label(root, text="Total Grocery").place(x=650, y=110)
tk.Entry(root, textvariable=grocery_total, width=12).place(x=770, y=110)
tk.Label(root, text="Total Others").place(x=650, y=140)
tk.Entry(root, textvariable=others_total, width=12).place(x=770, y=140)

tk.Label(root, text="Cosmetics Tax").place(x=650, y=180)
tk.Entry(root, textvariable=tax_cosmetics, width=12).place(x=770, y=180)
tk.Label(root, text="Grocery Tax").place(x=650, y=210)
tk.Entry(root, textvariable=tax_grocery, width=12).place(x=770, y=210)
tk.Label(root, text="Others Tax").place(x=650, y=240)
tk.Entry(root, textvariable=tax_others, width=12).place(x=770, y=240)

# Buttons
tk.Button(root, text="Total", command=calculate_total, width=10).place(x=650, y=280)
tk.Button(root, text="Generate Bill", command=generate_bill, width=15).place(x=740, y=280)


# Bill Area
bill_text = tk.Text(root, width=50, height=20)
bill_text.place(x=650, y=370)

root.mainloop()
