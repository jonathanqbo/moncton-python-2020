import tkinter as tk
window=tk.Tk()
window.title('hello world')
window.geometry('800x600')

label = tk.Label(window, text='hello world',font=('Arial',24,'normal'))
label.pack()

label1 = tk.Label(window, text='hello world',font=('Arial',24,'normal'))
label1.pack()

frame=tk.Frame(window)
frame.pack(pady=10, fill=tk.X)

button=tk.Button(frame, text='click me')
button.pack(side='right')

entry=tk.Entry(frame)
entry.pack(side='left')

listbox=tk.Listbox(window)
listbox.pack()

tk.mainloop()