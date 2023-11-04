from tkinter import  *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def psw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    print(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
    e3.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = e1.get()
    username = e2.get()
    password = e3.get()
    new_data ={website:{
                    "Username": username,
                    "Password": password
                    }
                }

    if website=="" or username=="" or password=="":
        # messagebox.Message("Please enter all the details!")
        messagebox.showwarning(title="Warning", message="Please enter all the details!")
    
    else:
        is_ok = messagebox.askokcancel(title="Are you sure", message=f"""Do you want to save your 
                                    \nusername: {username} \npassword: {password} 
                                    \nwebsite: {website}""")
        
        if is_ok:
            # with open("C:/Users/hp/Documents/Python Dev Udemy/Password Manager/manage.txt", mode="a+") as myfile:
            #     myfile.write(f"\n{website} || {username} || {password}")
            #     e1.delete(0,END)
            #     e3.delete(0,END)
            
            try:
                with open("C:/Users/hp/Documents/Python Dev Udemy/Password Manager/data.json", mode="r") as myfile:
                    #load the old data
                    data = json.load(myfile)
            except FileNotFoundError:
                with open("C:/Users/hp/Documents/Python Dev Udemy/Password Manager/data.json", mode="w") as myfile:
                    json.dump(new_data,myfile,indent=2)

            else:
                #read the old data
                data.update(new_data)
                with open("C:/Users/hp/Documents/Python Dev Udemy/Password Manager/data.json", mode="w") as myfile:
                    #write the new data
                    json.dump(data,myfile,indent=2)
            finally:
                e1.delete(0,END)
                e3.delete(0,END)
                
# ---------------------------- SEARCH  ------------------------------- #

def sch():
    web = e1.get()
    try:
        with open("C:/Users/hp/Documents/Python Dev Udemy/Password Manager/data.json",'r') as myfile:
            data=json.load(myfile)
            
    except FileNotFoundError:
        messagebox.showerror("Data file not found")

    else:
        if web in data:
            email=data[web]['Username']
            password=data[web]['Password']
            messagebox.showinfo(title="Your username and password",message=f"Your username: {email}]\n and password: {password}")
        else:
            messagebox.showerror("No data found for this website!")

        
# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20,pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="C:/Users/hp/Documents/Python Dev Udemy/Password Manager/logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=1,column=2)

l1 = Label(text="Website")
l1.grid(row=2,column=1)

l2 = Label(text="User Name")
l2.grid(row=3,column=1)

l3 = Label(text="Password")
l3.grid(row=4,column=1)

e1 = Entry(width=27)
e1.grid(row=2,column=2)
e1.focus()

b1 = Button(text="Search",command=sch)
b1.grid(row=2,column=3)

e2 = Entry(width=45)
e2.grid(row=3,column=2,columnspan=2)
e2.insert(0,"myemail@gmail.com")

e3 = Entry(width=27)
e3.grid(row=4,column=2)

e4 = Button(text="Generate Password",command=psw)
e4.grid(row=4,column=3)

e5 = Button(text="Add", width=36, command=save)
e5.grid(row=5,column=2,columnspan=2)

windows.mainloop()