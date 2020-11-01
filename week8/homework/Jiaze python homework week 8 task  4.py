import tkinter

window = tkinter.Tk()
window.title('tkinter layout and widgets')
window.geometry('800x800')

# to display single line text
label = tkinter.Label(window, text='Tkinter Layout and Widgets')
label.pack()

entry = tkinter.Entry(window)
entry.pack()

button = tkinter.Button(window, text='Click me!')
button.pack()

label = tkinter.Label(window, text='Tkinter win and lost')
label.pack()

entry = tkinter.Entry(window)
entry.pack()

button = tkinter.Button(window, text='Click me!')
button.pack()

text = tkinter.Text(window)
text.pack()

listbox = tkinter.Listbox(window)
listbox.pack()

text = tkinter.Text(window)
text.pack()

tkinter.mainloop()
