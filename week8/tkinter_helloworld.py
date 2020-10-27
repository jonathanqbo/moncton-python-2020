import tkinter as tk

window = tk.Tk()
window.title('Hello World')
window.geometry('800x600')

label_helloworld = tk.Label(window, text='Hello World')
label_helloworld.pack()

tk.mainloop()
