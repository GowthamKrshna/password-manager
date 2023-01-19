import tkinter
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letter = [random.choice(letters) for char in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_numbers + password_symbol + password_letter
    random.shuffle(password_list)
    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    pwd_text.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    mail = email_text.get()
    password = pwd_text.get()
    new_data ={
        website:
            {'email': mail,
             'password':password}

    }
    if len(password)==0 or len(website)==0:
        messagebox.showerror(title='Warning', message='Hey! dont leave fields empty')

    else:
        is_ok = messagebox.askokcancel(title='Confirmation', message=f'Do you want to save the details you added?\n'
                                                                         f'Website: {website}\nPassword: {password}')
        if is_ok:
            try:
                with open('password.json', 'r') as file:
                    #read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open('password.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                #update old data with new
                data.update(new_data)
                with open('password.json', 'w') as file:
                    #write new data
                    json.dump(data, file, indent=4)
            finally:
                website_text.delete(0,tkinter.END)
                pwd_text.delete(0,tkinter.END)

def find_password():
    website= website_text.get()
    try:
        with open('password.json', 'r') as file:
            data= json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message=f'{website} not found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message= f"mail = {email}\n password={password}")
        else:
            messagebox.showerror(title='Error', message=f'{website} not found')

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)
canvas = tkinter.Canvas(width=210, height=210)
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(105, 105, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text='Website:', font=('Calibri', 12))
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text='Email/Username:', font=('Calibri', 12))
email_label.grid(row=2, column=0)
pwd_label = tkinter.Label(text='Password:', font=('Calibri', 12))
pwd_label.grid(row=3, column=0)

website_text = tkinter.Entry(width=35)
website_text.grid(row=1, column=1)
website_text.focus()
email_text = tkinter.Entry(width=50)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, 'gowtham.krishna@live.com')
pwd_text = tkinter.Entry(width=34)
pwd_text.grid(row=3, column=1)

search_button = tkinter.Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2)
pwd_button = tkinter.Button(text='Generate Password', command=generate_password)
pwd_button.grid(row=3, column=2)
add_button = tkinter.Button(text='Add', width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()