import tkinter

window = tkinter.Tk()
window.title('tkinter layout and widgets')
window.geometry('800x800')

label = tkinter.Label(window, text='Tkinter Layout and Widgets', background='yellow')
label.pack(side='top')

entry = tkinter.Entry(window, background='yellow')
entry.pack(side='left')

# background color doesn't work in mac
button = tkinter.Button(window, text='Click me!', highlightbackground='yellow')
button.pack(side='right')

text = tkinter.Text(window, background='yellow')
text.pack(side='bottom')

tkinter.mainloop()

