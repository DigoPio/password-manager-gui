from tkinter import *
from tkinter import messagebox
from random import choice, shuffle



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global generated_password
    generated_password = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(6)]
    password_numbers = [choice(numbers) for _ in range(4)]
    password_symbols = [choice(symbols) for _ in range(2)]
    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    generated_password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = web_entry.get()
    user_email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Go back!", message="You need to fill all the fields before continue!")
    else:
        answer = messagebox.askyesno(title=f"{website}", message="Do you want to save your password?")
        if answer:
            output_data = f'Website: {website} | User/Email: {user_email} | Password: {password}\n'
            with open(f'passwords.txt', mode='a') as passwords_list:
                passwords_list.write(output_data)

            password_entry.delete(0, END)
            web_entry.delete(0, END)
            username_entry.delete(0, END)
            messagebox.showinfo(title="Information", message="Your password have been saved into passwords.txt file!"
                                                             " Check it out!")
        else:
            pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#entries
web_entry = Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generated_password = ''

#labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_and_user_label = Label(text='Email/Username:')
email_and_user_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#buttons
generate_password_button = Button(text="Generate Password", command=generate_password, justify='right')
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_password, width=38)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
