import tkinter as tk
import customtkinter


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

root_tk = customtkinter.CTk()  # create CTk window like the Tk window
root_tk.geometry("400x400")

def button_function():
    root_tk.destroy()

def button_f2():
    root_tk.call()

# Use CTkButton instead of tkinter Button
button1 = customtkinter.CTkButton(text="CLOSE", master=root_tk, command=button_function)
button1.place(relx=0.50, rely=0.35, anchor=tk.CENTER)

button2 = customtkinter.CTkButton(text="OPEN", master=root_tk, command=button_f2)
button2.place(relx=0.50, rely=0.55, anchor=tk.CENTER)

root_tk.mainloop()