import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess

class MenuBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MenuBar Application")
        self.root.geometry("600x400")
        self.root.config(bg="lightyellow")  # Set background color

        # Create styled menubar
        self.menubar = tk.Menu(self.root, bg="skyblue", fg="black", activebackground="orange", font=("Arial", 20, "bold"))
        self.root.config(menu=self.menubar)
        self.icon_image = tk.PhotoImage(file="logo.jpg")
        self.root.iconphoto(False, self.icon_image)


        # File menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0, font=("Arial", 12))
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Apps menu
        self.apps_menu = tk.Menu(self.menubar, tearoff=0, font=("Arial", 10))
        self.menubar.add_cascade(label="Apps", menu=self.apps_menu)
        self.apps_menu.add_command(label="Calculator", command=self.open_calculator)
        self.apps_menu.add_command(label="Notepad", command=self.open_notepad)
        self.apps_menu.add_command(label="Google Chrome", command=self.open_chrome)

        # About & Contact
        self.menubar.add_command(label="About", command=self.show_about)
        self.menubar.add_command(label="Contact", command=self.show_contact)

        # Welcome message in center
        self.welcome_label = tk.Label(
            self.root,
            text="Welcome.\nThis is a tkinter application\nWork with  the above Menu Bar to use this app. \ncreated by Nitin Makadiya.",
            font=("Helvetica", 16, "bold"),
            bg="lightyellow",
            justify="center"
        )
        self.welcome_label.place(relx=0.5, rely=0.5, anchor="center")

    def new_file(self):
        self.welcome_label.config(text="New file created.")
        self.root.title("MenuBar Application - New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.welcome_label.config(text=content)
                self.root.title(f"MenuBar Application - {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.welcome_label.cget("text"))
                self.root.title(f"MenuBar Application - {os.path.basename(file_path)}")
                messagebox.showinfo("Success", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()

    def open_calculator(self):
        try:
            if os.name == "nt":
                subprocess.Popen("calc.exe")
            elif os.name == "posix":
                subprocess.Popen(["gnome-calculator"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Calculator: {e}")

    def open_notepad(self):
        try:
            if os.name == "nt":
                subprocess.Popen("notepad.exe")
            elif os.name == "posix":
                subprocess.Popen(["gedit"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Notepad: {e}")

    def open_chrome(self):
        try:
            if os.name == "nt":
                subprocess.Popen(["start", "chrome"], shell=True)
            elif os.name == "posix":
                subprocess.Popen(["google-chrome"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Google Chrome: {e}")

    def show_about(self):
        messagebox.showinfo("About", "MenuBar Application\nVersion 1.0\nCreated with Tkinter\nDeveloper: Nitin Makadiya\nPhone: 9313283528\nEmail: nitinmakadiya7424@gmail.com")

    def show_contact(self):
        messagebox.showinfo("Contact", "For support, contact: nitinmakadiya7424@gmail.com")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuBarApp(root)
    root.mainloop()
