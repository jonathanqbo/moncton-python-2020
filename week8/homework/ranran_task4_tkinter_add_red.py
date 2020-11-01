import tkinter as init

window = init.Tk()
window.title('Task 4 _ Tkinter WIDGETS and Frame')
window.geometry('800x800')


def button_click():
    print('HelloWorld')


label = init.Label(window, text='Tkinter Frame with Widget Task 4',
                   width=50, height=2, font=('Arial', 24, 'normal'))
label.pack(side='top', pady=5)

label2 = init.Label(window, text='Tkinter Frame with Widget Task 4 _____ 2',
                    width=50, height=2, font=('Arial', 24, 'normal'))
label2.pack(side='top', pady=5)

frame = init.Frame(window)
frame.pack(side='top', pady=10, padx=10)

button = init.Button(frame, text='Click!', width=60, height=3)
button.pack(side='left', padx=30, pady=10)

button2 = init.Button(frame, text='Click!', width=20, height=3)
button2.pack(side='right', padx=30, pady=10)

text = init.Text(window, width=100, height=100, highlightbackground='silver')
text.pack(side='bottom', padx=30, pady=20)

init.mainloop()
