from cProfile import label
import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

root_tk = customtkinter.CTk()  # create CTk window like the Tk window
root_tk.geometry("400x400")

def button_function():
    root_tk.destroy()

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(text="close", master=root_tk, command=button_function)
button.place(relx=0.35, rely=0.35, anchor=tk.CENTER)

root_tk.mainloop()