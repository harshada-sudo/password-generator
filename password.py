import random as rm
import tkinter as tk

def password():
    lowercase_char=['a','b','c','d','e']
    uppercase_char=['A','B','C','D','E']
    special_char=['!','#','&','@']
    numbers=['1','2','3','4','5']

    password_str=rm.choice(lowercase_char) + rm.choice(uppercase_char) + rm.choice(special_char) + rm.choice(numbers)
    password_str=password_str + rm.choice(lowercase_char) + rm.choice(uppercase_char) + rm.choice(special_char) + rm.choice(numbers)

    pass_lbl=tk.Label(password_wnd,text=password_str,font=("times new roman",10,"bold"))
    pass_lbl.grid(row=1,column=0,padx=10,pady=10)

    print(password)

password_wnd=tk.Tk()
password_wnd.title("Password Generator")    
password_wnd.geometry('400x200')

generate_pass_btn=tk.Button(password_wnd,text="Generate Password",width=30,command=password)
generate_pass_btn.grid(row=0,column=0,ipadx=80,padx=10,pady=10)

password_wnd.mainloop()