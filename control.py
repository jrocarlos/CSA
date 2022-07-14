import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root_tk = customtkinter.CTk()  # create CTk window like the Tk window
root_tk.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_tk.mainloop()