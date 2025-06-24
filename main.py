import customtkinter
from tkinter import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


def add(task, window_to_close):


    f = customtkinter.CTkFrame(root)

    customtkinter.CTkLabel(f, text=task, wraplength=400, justify=LEFT).pack(anchor=NW, side=LEFT, padx=5, pady=5)

    customtkinter.CTkButton(f, image=img_del_task, text='', width=30, command=lambda: f.pack_forget()).pack(anchor=NE,side=RIGHT,padx=10,pady=5)
    f.pack(fill='x', padx=5, pady=5)

    window_to_close.destroy()


def add_task():
    window = customtkinter.CTkToplevel(root)
    window.title("Додати задачу")
    window.geometry("300x120")
    window.transient(root)
    window.grab_set()

    task_text = customtkinter.CTkEntry(window, width=250)
    task_text.pack(pady=5)

    customtkinter.CTkButton(window, text='Додати', font=('arial', 13, 'bold'),command=lambda: add(task_text.get(), window)).pack(pady=5)


root = customtkinter.CTk()
root.title('ToDoList')
root.geometry('700x500')
root.resizable(width=0, height=0)

img_del_task = ImageTk.PhotoImage(Image.open('del_task.png.png').resize((20, 20)))


btn_add_task = customtkinter.CTkButton(root, text='Додати задачу', font=('arial', 13, 'bold'), command=add_task)
btn_add_task.pack(anchor='center', side=BOTTOM, pady=5)

root.mainloop()