import tkinter
import turtle

window = tkinter.Tk()
window.title('tkinter layout and widgets')
window.geometry('800x800')

label = tkinter.Label(window, text='Tkinter Layout and Widgets', width=50, height=2, font=('Arial', 24, 'normal'))
label.pack(side='top', pady=5)

label = tkinter.Label(window, text='This is widget created in task3', width=50, height=2, font=('Arial', 16, 'normal'))
label.pack(side='top', pady=5)

frame = tkinter.Frame(window)
frame.pack(side='top', fill=tkinter.X, pady=10, padx=10)
entry = tkinter.Entry(frame, width=40)
entry.pack(side='left', fill=tkinter.X, padx=10, ipady=15)
button = tkinter.Button(frame, text='Click me!', width=20, height=3)
button.pack(side='left')

text = tkinter.Text(window, width=100, height=100, highlightbackground='silver')
text.pack(side='bottom', fill=tkinter.X, padx=10, pady=5)

tkinter.mainloop()

