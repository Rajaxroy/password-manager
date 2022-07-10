from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

GREEN = "#FDFFA9"

# find password


def find_password():
    key = web_entry.get().title()
    try:
        with open("data.json") as data:
            datafile = json.load(data)

        r_email = datafile[key]["email"]
        r_password = datafile[key]["password"]
        messagebox.showinfo(key, f"Email:{r_email}\nPassword:{r_password}")
    except KeyError:
        messagebox.showinfo("Error", "Either Invalid key or file does not exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    new_list = letters_list + symbols_list + numbers_list

    random.shuffle(new_list)
    password_entry.delete(0, END)
    password = "".join(new_list)

    pyperclip.copy(password)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get().title()
    password = password_entry.get()
    email = email_entry.get()

    new_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# labels

web_label = Label(text="Website:", bg=GREEN)
web_label.config(pady=5)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=GREEN)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=GREEN)
password_label.config(pady=5)
password_label.grid(column=0, row=3)

# entry functions

web_entry = Entry(width=35, )
web_entry.focus()
web_entry.grid(column=1, row=1)

email_entry = Entry(width=53)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=35, )
password_entry.grid(column=1, row=3, )

# buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
