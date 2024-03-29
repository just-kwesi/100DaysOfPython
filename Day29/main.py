from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#ffffff"
PADDING = 50


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def savePassword():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Please complete all fields", message="Please do not leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(END, string="kwesiossom@gmail.com")
            password_entry.delete(0, END)

            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                # working with the file
                with open("./passwords.json", mode="r") as passwords_file:
                    # read old data
                    passwords = json.load(passwords_file)
                    # add the new entries
                    passwords.update(new_data)

            except FileNotFoundError:
                with open("./passwords.json", mode="w") as passwords_file:
                    json.dump(new_data, passwords_file, indent=4)

            else:
                with open("./passwords.json", mode="w") as passwords_file:
                    json.dump(passwords, passwords_file, indent=4)

                    # passwords_file.write(f"{website} | {email} | {password}\n")


# ---------------------------- Search For password ------------------------------- #
def search():

    try:
        with open("./passwords.json", mode="r") as passwords_file:
            passwords = json.load(passwords_file)
            website = website_entry.get()

    except FileNotFoundError:
        messagebox.showwarning(title="Empty", message=f"No passwords have been stored")

    else:
        if website in passwords:
            entry = passwords[website]
            email = entry["email"]
            password = entry["password"]
            messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n")
        else:
            messagebox.showinfo(title="Not Found", message=f"The website: {website} was not found in memory")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=PADDING, pady=PADDING, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
photo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# buttons
generate_button = Button(text="Generate Password", command=generatePassword)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=savePassword, width=36)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)

# input fields / entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, string="kwesiossom@gmail.com")

password_entry = Entry(width=21, bg=WHITE)
password_entry.grid(column=1, row=3)

window.mainloop()
