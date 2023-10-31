from tkinter import *
from tkinter import messagebox
import fileinput

root = Tk()
root.geometry("500x500")
root.title("Contact Management system")
root.configure(bg="lightblue")
f = None
f2 = None
f3 = None
f4 = None
f5 = None
f6 = None
name = None
phone = None
email = None
buttom = None
buttom_edit=None
label_add = None
label_view = None
label_edit = None
label_update=None
label_delete=None


def destroy():
    if f is not None:
        f.destroy()
    if f3 is not None:
        f3.destroy()
    if f2 is not None:
        f2.destroy()
    if f4 is not None:
        f4.destroy()
    if f6 is not None:
        f6.destroy()
    if buttom is not None:
        buttom.destroy()
    if buttom_edit is not None:
        buttom_edit.destroy()    
    if label_add is not None:
        label_add.destroy()
    if label_view is not None:
        label_view.destroy()
    if label_edit is not None:
        label_edit.destroy()
    if label_update is not None:
        label_update.destroy()
    if label_delete is not None:
        label_delete.destroy()
    if f5 is not None:
        f5.destroy()


def ADD():
    global Y, Name, Phone, Email
    Name = name.get()
    Phone = phone.get()
    Email = email.get()

    with open("contact.txt", "r") as f:
        x = f.read()
    data = f"Name: {Name}\nPhone: {Phone}\nEmail: {Email}\n"
    if data not in x:
        with open("contact.txt", "a") as f:
            f.write(data)
        messagebox.showinfo("Contact added", "Contact added")

    else:
        messagebox.showinfo("Contact added", "Contact added")
    name.delete(0,END)
    phone.delete(0,END)
    email.delete(0,END)

def add():
    global name, phone, email, f, f3, f2, buttom, f4, label_view, label_add, Y, l
    destroy()

    label_add = Label(text="\nADD CONTACT SECTION\n", bg="lightblue", font="bold")
    label_add.pack()
    f = Frame(root, bg="lightblue")
    f.pack()

    name_label = Label(f, text="Name        ", bg="lightblue")
    name_label.pack(side=LEFT)
    name = Entry(f)
    name.pack(side=LEFT, pady=5)

    f3 = Frame(root, bg="lightblue")
    f3.pack()

    Phone_label = Label(f3, text="Phone no.", bg="lightblue")
    Phone_label.pack(side=LEFT)
    phone = Entry(f3)
    phone.pack(side=LEFT, pady=5)

    f2 = Frame(root, bg="lightblue")
    f2.pack()

    Email_label = Label(f2, text="Email        ", bg="lightblue")
    Email_label.pack(side=LEFT)
    email = Entry(f2)
    email.pack(side=LEFT, pady=5)

    buttom = Button(text="ADD CONTACT", command=ADD)
    buttom.pack(pady=10)


def Search():
    global search

    S = search.get()
    detail = ""
    with open("contact.txt", "r") as f:
        a = f.readlines()
        for i in range(0, len(a), 3):
            if S in a[i]:
                detail += "".join(a[i : i + 3])
                messagebox.showinfo("Contact found", f"Contact found\n{detail}")
                break

        else:
            messagebox.showinfo("", "No result found")


def view():
    global f4, f, f2, f3, buttom, label_view, search
    destroy()

    label_view = Label(text="\nVIEW CONTACT SECTION \n", bg="lightblue", font="bold")
    label_view.pack()
    f4 = Frame(root, bg="lightblue")
    f4.pack()
    search_label = Label(f4, text="Name  ", bg="lightblue")
    search_label.pack(side=LEFT)
    search = Entry(f4, text="\n")
    search.pack(side=LEFT)
    buttom = Button(text="Search", command=Search)
    buttom.pack(pady=10)


def update():
    Name = name.get()
    Phone = phone.get()
    Email = email.get()
    Udata = f"Name: {Name}\nPhone: {Phone}\nEmail: {Email}\n"
    
    with open("contact.txt", "r") as f:
        c = f.read()
        c = c.replace(Odetail, Udata)
    with open("contact.txt", "w") as f:
        f.write(c)
        messagebox.showinfo("Contact Edited", "Contact Edited")



def Edit():
    global name, phone, email, Odetail,f3,f2,label_update,f,buttom
    Edit_name = edit_name.get()
    Odetail = ""
    with open("contact.txt", "r") as f:
        b = f.readlines()
        for i in range(0, len(b), 3):
            if Edit_name in b[i]:
                Odetail += "".join(b[i : i + 3])
                messagebox.showinfo("Contact found", f"Contact found\n{Odetail}")
                
                # with open("contact.txt", "w") as f:
                label_update = Label(text="\nUPDATE CONTACT SECTION\n", bg="lightblue", font="bold")
                label_update.pack()
                f = Frame(root, bg="lightblue")
                f.pack()

                name_label = Label(f, text="Name        ", bg="lightblue")
                name_label.pack(side=LEFT)
                name = Entry(f)
                name.pack(side=LEFT, pady=5)

                f3 = Frame(root, bg="lightblue")
                f3.pack()

                Phone_label = Label(f3, text="Phone no.", bg="lightblue")
                Phone_label.pack(side=LEFT)
                phone = Entry(f3)
                phone.pack(side=LEFT, pady=5)

                f2 = Frame(root, bg="lightblue")
                f2.pack()

                Email_label = Label(f2, text="Email        ", bg="lightblue")
                Email_label.pack(side=LEFT)
                email = Entry(f2)
                email.pack(side=LEFT, pady=5)

                buttom = Button(text="Update", command=update)
                buttom.pack()
                break
        else:
            messagebox.showinfo("", "No result found")


def edit():
    global label_edit, f5, edit_name,buttom_edit
    destroy()
    label_edit = Label(text="\nEDIT SECTION\n", bg="lightblue", font="bold")
    label_edit.pack()
    f5 = Frame(root, bg="lightblue")
    f5.pack()
    edit_label = Label(f5, text="Name ", bg="lightblue")
    edit_label.pack(side=LEFT)
    edit_name = Entry(f5)
    edit_name.pack(side=LEFT)
    buttom_edit = Button(text="Edit", command=Edit)
    buttom_edit.pack(pady=5)

def Delete():
    Delete_name = delete_name.get()
    detail = ""
    contact_found = False
    updated_contacts = []

    with open("contact.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            if Delete_name in lines[i]:
                detail = "".join(lines[i:i + 3])
                contact_found = True
            else:
                updated_contacts.extend(lines[i:i + 3])

    if contact_found:
        with open("contact.txt", "w") as f:
            f.writelines(updated_contacts)
        messagebox.showinfo("", "Contact deleted")
    else:
        messagebox.showinfo("", "Contact not found")

                


def delete():
    global delete_name,f6,label_delete,buttom
    destroy()
    label_delete = Label(text="\nDELETE SECTION\n",bg="lightblue",font="bold")
    label_delete.pack()
    f6=Frame(root,bg="lightblue")
    f6.pack()
    delete_label=Label(f6,text="Name ",bg="lightblue")
    delete_label.pack(side=LEFT,padx=5)
    delete_name=Entry(f6)
    delete_name.pack(side=LEFT)
    buttom=Button(text="Delete",command=Delete)
    buttom.pack(pady=8)


f1 = Frame(root, bg="lightblue")
f1.pack()
label = Label(
    f1, text="Welcome to the Abhishek's Contacts", bg="lightblue", font="bold"
)
label.pack()

label1 = Label(f1, text="\nWhat do you want to do:\n", bg="lightblue", font=8)
label1.pack()

buttom1 = Button(f1, text="ADD CONTACT", command=add)
buttom1.pack(side=LEFT, padx=10)

buttom2 = Button(f1, text="VIEW CONTACT", command=view)
buttom2.pack(side=LEFT, padx=10)

buttom3 = Button(f1, text="EDIT CONTACT", command=edit)
buttom3.pack(side=LEFT, padx=10)

buttom4 = Button(f1, text="DELETE CONTACT", command=delete)
buttom4.pack(side=LEFT, padx=10)


root.mainloop()
