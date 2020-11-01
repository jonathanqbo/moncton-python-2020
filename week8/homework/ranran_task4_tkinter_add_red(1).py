import tkinter

window = tkinter.Tk()
window.title('Task 4 _ Tkinter WIDGETS and Frame')
window.geometry('1000x1000')

label = tkinter.Label(window, text='Tkinter Frame with Widget Task 4',
                      width=50, height=2, font=('Arial', 24, 'normal'))
label.pack(side='top', pady=5)

label2 = tkinter.Label(window, text='Tkinter Frame with Widget Task 4 _____ 2',
                       width=50, height=2, font=('Arial', 24, 'normal'))
label2.pack(side='top', pady=5)

frame = tkinter.Frame(window)
frame.pack(side='top', pady=10, padx=10)

button = tkinter.Button(frame, text='Click!', width=30, height=5)
button.pack(side='left', padx=30, pady=10)

button = tkinter.Button(frame, text='Click!', width=30, height=5)
button.pack(side='right', padx=30, pady=10)

text = tkinter.Text(window, width=100, height=100, highlightbackground='silver')
text.pack(side='bottom', fill=tkinter.X, padx=30, pady=20)

tkinter.mainloop()
