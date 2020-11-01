import tkinter as tk

window=tk.Tk()
window.title('Hello world')
window.geometry('608x608')
window.bgcolor=('black')

label=tk.Label(window,text='this is a label')
label.pack(side='top',expand=True)

label=tk.Label(window,text='this is a label2')
label.pack(expand=True)

frame=tk.Frame(window)
frame.pack(side='top',padx=10,pady=10)


button=tk.Button(frame,text='please click me',width=30,height=2)
button.pack(side='left')

button=tk.Button(frame,text='click me too',width=10,height=2)
button.pack(side='right')

text=tk.Text(window)
text.pack(side='bottom',pady=80)

tk.mainloop()