import tkinter as tk
import customtkinter as ct


ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")

root_tk = ct.CTk()  # create CTk window like the Tk window
root_tk.geometry("400x400")
root_tk.title('CSA CONTROL')

def button_function():
    root_tk.destroy()

def button_f2():
    root_tk.call("main.py")

# Use CTkButton instead of tkinter Button
button1 = ct.CTkButton(text="CLOSE", master=root_tk, command=button_function)
button1.place(relx=0.50, rely=0.35, anchor=tk.CENTER)

button2 = ct.CTkButton(text="OPEN", master=root_tk, command=button_f2)
button2.place(relx=0.50, rely=0.55, anchor=tk.CENTER)

root_tk.mainloop()