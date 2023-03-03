from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    if website == "":
        messagebox.showerror(title="Error", message= "No website name has given.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="There is no saved password info.")
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showerror(title="Error", message=f"Password for '{website}' has never been saved.")
            else:
                messagebox.showinfo(title="Search Result", message= f"Here is your search info.\nWebsite: {website}\nemail: {email}\npassword:{password}\n password has been copied to your clipboard.")
                pyperclip.copy(password)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letter_list = [random.choice(letters) for letter in range(random.randint(8,10))]
    pw_number_list = [random.choice(numbers) for number in range(random.randint(2,4))]
    pw_symbol_list = [random.choice(symbols) for symbol in range(random.randint(2,4))]

    password_list=pw_letter_list+pw_symbol_list+pw_number_list
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD -----------p-------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email":email, "password":password}}

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message= "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details entered: \nWebsite: {website}\nEmail: {email}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your@email.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command= search)
search_button.grid(column=2, row=1)

window.mainloop()